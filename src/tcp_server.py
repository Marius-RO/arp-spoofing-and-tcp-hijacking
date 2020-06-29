# TCP Server
import socket
import logging
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

port = 10040
adresa = '0.0.0.0'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
sock.listen(5)

# pentru acest experiment la server se va conecta un singur client
logging.info('Asteptam conexiuni...')
conexiune, address = sock.accept()
logging.info("Handshake cu %s", address)


try:
    while True:
        time.sleep(5)
        data = conexiune.recv(1024)

        logging.info('Content primit: "%s"', data)
        conexiune.send(b"Server a primit mesajul: " + data)
        logging.info(f"Content trimis: Server a primit mesajul: {data}")

except KeyboardInterrupt:
    print("except")
finally:
    conexiune.close()
    sock.close()
    exit(0)

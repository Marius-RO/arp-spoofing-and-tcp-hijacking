# TCP client
import socket
import logging
import time
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

port = 10040
adresa = '198.7.0.2'
server_address = (adresa, port)

# pentru acest experiment clientul se va conecta la un singur server
logging.info('Handshake cu %s', str(server_address))
sock.connect(server_address)
cnt_mesaj = 1

try:
    while True:
        time.sleep(5)
        mesaj = 'mesajul_' + str(cnt_mesaj)
        sock.send(mesaj.encode('utf-8'))
        logging.info('Mesaj trimis: "%s"', mesaj)
        data = sock.recv(1024)
        logging.info('Content primit: "%s"', data)
        cnt_mesaj += 1

except KeyboardInterrupt:
    print("except")

finally:
    logging.info('closing socket')
    sock.close()
    exit(0)

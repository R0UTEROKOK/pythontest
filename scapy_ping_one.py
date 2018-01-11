from scapy.all import * 

import sys

from random import randint

def scapy_ping_one(host):

	id_ip =randint(1,65535)

	id_ping = randint(1,65535)

	seq_ping = randint(1,65535)



	packet = IP(dst=host,ttl=64,id=id_ip)/ICMP(id=id_ping,seq=seq_ping)/b'welcome cisco'

	ping=(sr1(packet))

	#ping.show()



	if ping:

		os._exit(3)







if __name__ == '__main__':

	scapy_ping_one(sys.argv[1])


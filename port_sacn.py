import socket

ports = [22,23,80,445,3389]
hosts = ['172.17.135.11','172.17.135.6','172.17.135.126','172.17.135.19','172.17.135.20']


for host in hosts:
    for port in ports:
        try:
            s = socket.socket()
            print("connecting to "+"ipaddress: "+ str(host)+  " port: "+str(port))
            s.connect((host,port))
            s.send(b'Primal Security \n')
            banner = s.recv(1024)
            if banner:
                print("this port is open " + host +":"+ str(port))
            s.close()
        except:
            pass
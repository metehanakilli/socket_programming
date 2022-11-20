import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect((socket.gethostname(),12345))

file=open("kufurbaz_haydo.jpeg",'rb')


msg=file.read(2048)

while msg:
    s.send(msg)
    msg = file.read(2048)

file.close()
s.close()
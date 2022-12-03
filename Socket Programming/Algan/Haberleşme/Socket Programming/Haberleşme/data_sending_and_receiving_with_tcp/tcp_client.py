import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((socket.gethostname(),12345))

msg=s.recv(1024) #1 saniyede alınacak maksimum dosya boyutu (tampon boyutu) byte cinsinden belirtilir.

print(msg.decode("utf-8")) #Byte cinsinden alınan datanın string'e dönüştürülmesi ve ekrana yazdırılması


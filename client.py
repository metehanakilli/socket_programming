import socket

client_socket=socket.socket()

host="192.168.1.5"   #Bağlanılacak adres ve port
port=12345

try:
    client_socket.connect((host,port)) #connect ile bağlantı yapılır.

    yanit=client_socket.recv(1024) #1 sn'de alınacak maksimum dosya boyutunu ayarladım.
    print(yanit.decode("utf-8"))  #decode ile byte olarak alınan yanıtı string(utf-8) e çevirir.

    client_socket.close()

except socket.error as msg:
    print("[Server aktif değil!!!] Mesaj:",msg)
from socket import socket, AF_INET, SOCK_DGRAM


host="192.168.1.2"
port=12345

rec = socket(AF_INET, SOCK_DGRAM)
rec.bind((host, port))


while True:
    msg, addr = rec.recvfrom(8192)
    print("Mesajınız:%s" % msg)
    print(f"Mesaj {addr}'den alındı")


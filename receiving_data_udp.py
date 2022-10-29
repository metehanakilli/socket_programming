from socket import socket, AF_INET, SOCK_DGRAM


host="10.80.1.53"
port=12345

rec = socket(AF_INET, SOCK_DGRAM)
rec.bind((host, port))


while True:
    msg, addr = rec.recvfrom(8192)
    print("Mesajınız:%s" % msg)
    print(f"Mesaj {addr}'den alındı")


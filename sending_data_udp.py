from socket import socket, AF_INET, SOCK_DGRAM

host="10.80.1.53"
port=12345

serv= socket(AF_INET, SOCK_DGRAM)
# SOCK_DGRAM ile UDP kullanacağımızı AF_INET ile de IPV4 kullanacağımızı belirttik.

msg = ('Merhaba').encode('utf-8')
# sendto() fonksiyonu verileri byte olarak gönderir.Verileri göndermeden önce onları bu şekilde string'e çeviririz.


serv.sendto(msg, (host,port))   #Burada mesaj host ve port bilgisini gönderdim
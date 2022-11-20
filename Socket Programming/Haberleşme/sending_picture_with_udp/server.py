import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((socket.gethostname(),12345))

s.listen()

print("Bağlantı bekleniyor...")
clientsocket,address=s.accept()
print(f"{clientsocket,address} ile bağlantı kuruldu!")

file=open('kufurbaz_haydo.jpeg.jpeg','wb')  #dosyayı binary şekilde yazarak açar.

msg=s.recv(2048) #stream based protokolü kullanılarak görüntü küçük parçalar şeklinde alınıp birleştirilir.

while msg:
    print("Dosya gönderiliyor...")
    file.write(msg)
    msg = s.recv(2048)
    pass

print("Dosya gönderildi!!!")

file.close()
s.close()
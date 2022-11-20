import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP ve IPV4 kullanılacağı belirtildi.

s.bind((socket.gethostname(),12345)) #gethostname ile IPV4 adresi alınır ve port 12345 olarak atanır.

s.listen(5) #maksimum 5 bağlantı ile sınırlandırıldı
print("Bağlantı bekleniyor...")

while True:
    clientsocket,address=s.accept()  #Birisi bağlandığında onun bilgilerini alır.
    print(f"{clientsocket,address} ile bağlantı kuruldu!")

    clientsocket.send(bytes("MERHABA! SERVER'A HOŞGELDİNİZ!!!","UTF-8"))
    """bağlanan sockete istenilen data gönderilir. Burada bytes kullanılmasının sebebi isyenilen data
    string formatındadır fakat bilgiyi gönderirken bitler şeklinde göndermek gerekir bytes fonksiyonu ise
    string formatını bitlere dönüştürür."""

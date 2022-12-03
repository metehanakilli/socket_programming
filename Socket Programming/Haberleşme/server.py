import base64
import socket

import cv2
import imutils

BUFF_SIZE= 65536  #Alınacak olan verinin boyutu sınırlandırmak.

port=12345
host_ip='10.241.221.80'

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP VE IPV4 olduğu belirtildi.
server.bind((host_ip, port)) #Bind işlemi yapıldı.


server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE) #

host_name=socket.gethostname() #gethostname() ile IPV4 adresi alındı ve host_name değişkenine atandı.
socket_address=(host_ip, port)

print("Bağlantı bekleniyor...")

vid=cv2.VideoCapture(0)

fps, st, frames_to_count, cnt=(0, 0, 20, 0) #fps, zaman, sayılan frameler gibi verileri almak için tanımladık
while True:
    msg,client_addr=server.recvfrom(BUFF_SIZE)
    print("Bağlantı kuruldu:",client_addr)
    WIDTH=400
    while(vid.isOpened()):
        _,frame=vid.read()
        frame= imutils.resize(frame, width=WIDTH)

        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        #cv2.imencode kullanılarak video istenilen formatta ve kalitede "sıkıştırılarak" alınır.
        #cv2.IMWRITE_JPEG_QUALITY dosyaya görüntüyü alırken istenilen kalitede sıkıştırmak için kullanılmıştır.

        message=base64.b64encode(buffer) #string olarak gelen veriyi binary olarak çevirir

        server.sendto(message, client_addr)
        cv2.imshow("Video Aktarılıyor...", frame) #Görüntülenecek pencerenin adı ve gösterilecek görüntü
        key=cv2.waitKey(1) & 0xFF #waitKey 'q' tuşuna basana kadar pencereyi kapatmaz.
        if key == ord('q'):
            server.close()
            break


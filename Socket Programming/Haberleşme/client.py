import socket
import cv2, imutils
import base64
import numpy as np
import time

BUFF_SIZE= 65536  #Alınacak olan verinin boyutu sınırlandırmak.

port=12345
host_ip='10.241.221.80'
message=b'Hello'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP VE IPV4 olduğu belirtildi.

client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE) #

host_name = socket.gethostname() #gethostname() ile IPV4 adresi alındı ve host_name değişkenine atandı.

client.sendto(message, (host_ip, port))
fps, st, frames_to_count, cnt = (0, 0, 20, 0)

while True:
    packet, _ = client.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet, " /") #binary text i normal forma dönüştürme
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1) #görüntü verilerini okumak ve görüntü biçimine dönüştürmek için kullanılır.
    frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #putText metodu herhangi bir görüntü üzerine text yazabilmek için kullanılır.
    cv2.imshow("RECEIVING VIDEO", frame) #Görüntülenecek pencerenin adı ve gösterilecek görüntü
    key = cv2.waitKey(1) & 0xFF #waitKey 'q' tuşuna basana kadar pencereyi kapatmaz.
    if key == ord('q'):
        client.close()
        break
    if cnt == frames_to_count:
        try:
            fps = round(frames_to_count / (time.time() - st))
            st = time.time()
            cnt = 0
        except:
            pass
    cnt += 1

import json
import requests
import socket
import zlib

import base64
import cv2
import imutils
import numpy as np


class server_TCP():
    def __init__(self):
        super(server_TCP, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bagli = 0
        self.ses = requests.Session()

    def baglan(self, host, port):
        self.s.bind((host, port))
        self.s.listen()
        print("dinleniyor")
        self.c, self.addr = self.s.accept()
        print('Gelen baglanti:', self.addr)
        return self.c

    def telemetri_gonder(self, mesaj):
        self.mesaj = json.dumps(mesaj)
        self.c.send(self.mesaj.encode("utf-8"))

    def telemetri_al(self):
        self.yanit = self.c.recv(512)
        self.result = json.dumps(self.yanit.decode("utf-8"))
        self.result = json.loads(self.result)
        return self.result

    def sunucuya_giris(self, url, kadi, sifre):
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.giris = {
            "kadi": kadi, "sifre": sifre}

        self.gidecek = json.dumps(self.giris)
        print(self.gidecek)

        self.giden = self.ses.post(url + '/api/giris', self.gidecek, headers=self.headers)

        return self.giden.status_code, self.giden.text

    def sunucuya_postala(self, url, mesaj):
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.mesaj = json.dumps(mesaj)
        self.rakip = self.ses.post(url + '/api/telemetri_gonder', self.mesaj, headers=self.headers)

        return self.rakip.status_code, self.rakip.text

    def sunucu_saati_al(self, url):
        self.sunucu_saati = self.ses.get(url + '/api/sunucusaati')

        return self.sunucu_saati.status_code, self.sunucu_saati.text

    def kilitlenme_postala(self, url, mesaj):
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.mesaj = json.dumps(mesaj)
        print(self.mesaj)
        self.kilit = self.ses.post(url + '/api/kilitlenme_bilgisi', self.mesaj, headers=self.headers)

        return self.kilit.status_code

    def kamikaze_gonder(self, url, mesaj):
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        # mesaj=mesaj.decode("utf-8")
        self.mesaj = json.dumps(mesaj)
        print(self.mesaj)
        self.kamikaze = self.ses.post(url + '/api/kamikaze_bilgisi', self.mesaj, headers=self.headers)

        return self.kamikaze.status_code

    def qr_koordinat_al(self, url):
        self.qr_koordinat = self.ses.get(url + '/api/qr_koordinati')
        return self.qr_koordinat.status_code, self.qr_koordinat.text

    def sunucudan_cikis(self, url):
        self.durum = self.ses.get(url + '/api/cikis')
        return self.durum


class client_TCP():
    def __init__(self):
        super(client_TCP, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def baglan(self, host, port):
        self.s.connect((host, port))
        return self.s

    def telemetri_gonder(self, mesaj):
        self.mesaj = json.dumps(mesaj)
        self.s.sendall(self.mesaj.encode("utf-8"))

    def telemetri_al(self):
        self.yanit = self.s.recv(2048)
        self.result = json.dumps(self.yanit.decode("utf-8"))
        self.result = json.loads(self.result)

        return self.result


class server_UDP():
    def __init__(self):
        super(server_UDP, self).__init__()
        self.BUFF_SIZE = 65536
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        self.host_name = socket.gethostname()

    def baglan(self, host, port):
        self.socket_address = (host, port)
        self.s.bind(self.socket_address)
        print('Listening at:', self.socket_address)
        return self.s

    def video_al(self):
        self.packet, self.server = self.s.recvfrom(self.BUFF_SIZE)
        self.video_z = zlib.decompress(self.packet)
        self.data = base64.b64decode(self.video_z, ' /')
        self.npdata = np.fromstring(self.data, dtype=np.uint8)
        self.frame = cv2.imdecode(self.npdata, 1)

        return self.frame

    def mesaj_al(self):
        self.mesaj, self.server = self.s.recvfrom(1024)
        return self.mesaj

    def mesaj_gonder(self, mesaj):
        if isinstance(mesaj, dict):
            mesaj = str(mesaj)
        self.mesaj = json.dumps(mesaj)
        mesaj = str.encode(self.mesaj)
        self.s.sendto(mesaj, self.server)


class client_UDP():
    def __init__(self):
        super(client_UDP, self).__init__()
        self.BUFF_SIZE = 65536
        self.WIDTH = 800
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        self.host_name = socket.gethostname()

    def baglan(self, host, port):
        self.client_addr = (host, port)
        # self.s.bind(self.client_addr)
        return self.client_addr, self.s

    def video_gonder(self, frame):
        self.frame = imutils.resize(frame, width=800)
        self.encoded, self.buffer = cv2.imencode('.jpg', self.frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        self.message = base64.b64encode(self.buffer)
        self.video_zlib = zlib.compress(self.message, 6)
        self.s.sendto(self.video_zlib, self.client_addr)

    def mesaj_al(self):
        self.mesaj, self.server = self.s.recvfrom(1024)
        self.mesaj = self.mesaj.decode('utf-8')
        return self.mesaj

    def mesaj_gonder(self, mesaj):
        self.mesaj = str.encode(str(mesaj))
        self.s.sendto(mesaj, self.client_addr)

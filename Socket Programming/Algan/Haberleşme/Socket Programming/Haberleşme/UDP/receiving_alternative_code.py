from socketserver import BaseRequestHandler, UDPServer

# HATA VERİYOR ÜZERİNDE ÇALIŞ

class MyHandler(BaseRequestHandler):
    def handle(self):
        print("Bağlantı sağlandı:%s" % self.client_address)
        msg, rec = self.request
        print("Bunu söyledi:%s" % msg)
        rec.sendto("Mesaj alındı!".encode(), self.client_address)


serv = UDPServer(('localhost', 12345), MyHandler)
serv.serve_forever()

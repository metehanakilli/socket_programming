import socket

host = "10.241.24.70"  # içerideki ip adresi localhost olarak geçer.
port = 12345

try:  # try ile kod bloğunu hatalara karşı denetlemeye aldım.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET ile IPV4 adresleme SOCK_STREAM ile de TCP bağlantı tipini belirtiriz.

    server_socket.bind((host, port))  # bind ile bağlantı yaptık.
    print("socket {} nolu porta bağlandı".format(port))

    server_socket.listen(5)  # Aynı anda en fazla 5 bağlantıya izin verdik.
    print("socket dinleniyor")

except socket.error as msg:
    print("HATA", msg)

# client ile bağlantı kurulursa

conn, addr = server_socket.accept()
# accept koduna gelince python bağlantı kurulana kadar bekler.
# Burada c connection addr ise address'tir.
print("Gelen bağlantı:", addr)

mesaj = "Bağlantı için teşekkürler"
conn.send(mesaj.encode("utf-8"))

conn.close

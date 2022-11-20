import sys
from socket import socket


def create_socket():
    try:
        global host, port, server_socket  # ip adresi port nosu ve server(s)'ı global olarak tanımladım

        host = "192.168.1.2"
        port = 12345

        server_socket = socket((host, port))

    except socket.error as msg:
        print("Soket oluştururken hata oluştu:" + str(msg))


def bind():
    try:
        print("socket {} nolu porta bağlandı".format(port))
        server_socket.bind((host, port))  # bind ile bağlantı yaptık.
        server_socket.listen(5)

    except socket.error as msg:
        print("Soketler bind edilirken hata oluştu:" + str(msg) + "\n" + "Bağlantı kurulmaya çalışılıyor")


def socket_accept():
    conn, addr = server_socket.accept()
    print("Bağlantı kuruldu" + "   IP:" + addr[0] + "   Port:" + str(addr[1]))

    send_command(conn)
    conn.close()


def send_command(self, conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            server_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main(self):
    create_socket()
    bind()
    socket_accept()

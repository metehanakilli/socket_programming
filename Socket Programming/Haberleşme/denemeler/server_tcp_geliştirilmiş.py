import cmd
from socket import socket


class Server_TCP():

    def __int__(self):  # soket oluşturmak için init fonksiyonunu kullandım
        try:
            global host, port, server_socket  # ip adresi port nosu ve server(s)'ı global olarak tanımladım

            self.host = "10.80.1.53"
            self.port = 12345

            self.server_socket = socket((host, port))

        except self.socket.error as msg:
            print("Soket oluştururken hata oluştu:" + str(msg))

    def bind(self):
        try:
            self.server_socket.bind((host, port))  # bind ile bağlantı yaptık.
            self.server_socket.listen(5)
            print("socket {} nolu porta bağlandı".format(port))

        except self.socket.error as msg:
            print("Soketler bind edilirken hata oluştu:" + str(msg) + "\n" + "Bağlantı kurulmaya çalışılıyor")

    def socket_accept(self):
        self.conn, addr = server_socket.accept()
        print("Bağlantı kuruldu" + "   IP:" + addr[0] + "   Port:" + str(addr[1]))

        self.send_command(self.conn)
        self.conn.close()

    def send_commands(self, conn):
        while True:
            self.cmd = input()
            if cmd == "quit":
                self.conn.close()
                self.server_socket.close()
                self.sys.exit()
            if len(str.encode(cmd)) > 0:
                self.conn.send(str.encode(cmd))
                self.client_response = str(conn.recv(1024), "utf-8")
                print(self.client_response, end="")

    def main(self):
        self.bind()
        self.socket_accept(self)


server = Server_TCP()
server.main()

import socket
import threading

from sockhandler import SocketHandler


class WebServer():
    sock = None

    def __init__(self, ip='127.0.0.1', port=7853):
        self.ip = ip
        self.port = port

        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)
        print("WebServer is started............................")

    def start(self):
        while True:
            skt, addr = self.sock.accept()

            if skt:
                print("Received a socket {0} from {1} ................. ".format(skt.getpeername(), addr))
                sockHandler = SocketHandler(skt)
                thr = threading.Thread(target=sockHandler.startHandler , args=( ) )
                thr.setDaemon(True)
                thr.start()
                thr.join()

                skt.close()
                print("Socket {0} handling is done............".format(addr))




if __name__ == '__main__':
    ws = WebServer()
    ws.start()

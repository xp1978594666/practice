from sockethandlercontent import SocketHandlerContent

class SocketHandler:

    def __init__(self, sock):
        self.sock = sock
        self.headInfo = set()

    def startHandler(self):
        self.headHandler()
        self.sendRsp()
        return None

    def headHandler(self):
        self.headInfo = self.__getAllLine()
        print(self.headInfo)
        return None

    def sendRsp(self):
        data = "HELLO WORLD"
        self.__sendRspAll(data)
        return None

#####################################3

    def __getLine(self):

        b1 = self.sock.recv(1)
        b2 = 0
        data = b''

        while  b2 != b'\r' and b1 != b'\n' :
            b2 = b1
            b1 = self.sock.recv(1)
            if not b1:
                return str(data)
            data += bytes(b2)

        return data.strip(b'\r')


    def __getAllLine(self):

        data = b''
        dataList = list()
        data = b''

        while True:
            data = self.__getLine()
            if data:
                dataList.append(data)
            else:
                return dataList

        return None

    def __sendRspLine(self,data):

        data += "\r\n"
        self.sock.send(data.encode("ASCII"))
        return None


    def __sendRspAll(self, data):

        self.__sendRspLine(SocketHandlerContent.head_protocal +
                           SocketHandlerContent.head_code_200 +
                           SocketHandlerContent.head_status_OK)

        strRsp = SocketHandlerContent.head_content_length
        strRsp += str(len(data))
        self.__sendRspLine( strRsp )

        self.__sendRspLine(SocketHandlerContent.head_content_type +
                           SocketHandlerContent.content_type_html)


        self.__sendRspLine( SocketHandlerContent.blank_line)
        self.__sendRspLine(data)


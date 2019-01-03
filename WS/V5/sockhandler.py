import os
from sockethandlercontent import SocketHandlerContent

class SocketHandler:

    def __init__(self, sock):
        self.sock = sock
        self.headInfo = dict()

    def startHandler(self):
        self.headHandler()
        print(self.headInfo["uri"])
        self.reqRoute()
        return None

    def reqRoute(self):

        uri = self.headInfo.get("uri","BadReq")



        if uri == "/":
            self.sendWebPage("index.html")
        if uri == "/favicon.ico":
            self.sendStaticIco("favicon.ico")
        if uri == "/index.html":
            self.sendWebPage("index.html")

        return None



    def headHandler(self):
        tmpHead = self.__getAllLine()
        for line in tmpHead:
            if  ":" in line:
                infos = line.split(": ")
                self.headInfo[infos[0]] = infos[1]
            else:
                infos = line.split(" ")
                self.headInfo["protocal"] = infos[2]
                self.headInfo["method"] = infos[0]
                self.headInfo["uri"] = infos[1]

        return None


    def sendWebPage(self, path):
        fp =  os.path.join(SocketHandlerContent.base_path, path)
        with open(fp,mode='r') as f:
            html = f.read()
            self.__sendRspAll(html)

    def sendStaticIco(self, path):
        fp =  os.path.join(SocketHandlerContent.base_path, "static", path)
        with open(fp,mode='rb') as f:
            ico = f.read()
            self.__sendRspAll(ico, SocketHandlerContent.content_type_ico)
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
                dataList.append(data.decode("ascii"))
            else:
                return dataList

        return None

    def __sendRspLine(self,data):

        if type(data) == bytes:
            self.sock.send(data)
        else:
            data += "\r\n"
            self.sock.send(data.encode("utf-8"))
        return None


    def __sendRspAll(self, data, content_type = SocketHandlerContent.content_type_html):

        self.__sendRspLine(SocketHandlerContent.head_protocal +
                           SocketHandlerContent.head_code_200 +
                           SocketHandlerContent.head_status_OK)

        strRsp = SocketHandlerContent.head_content_length
        strRsp += str(len(data))
        self.__sendRspLine( strRsp )

        self.__sendRspLine(SocketHandlerContent.head_content_type +
                           content_type)


        self.__sendRspLine( SocketHandlerContent.blank_line)
        self.__sendRspLine(data)


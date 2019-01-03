import socket


def getLine(sock):

    b1 = sock.recv(1)
    b2 = 0
    data = b''

    while  b2 != b'\r' and b1 != b'\n' :
        b2 = b1
        b1 = sock.recv(1)
        if not b1:
            return str(data)
        data += bytes(b2)

    return data.strip(b'\r')


def getAllLine(sock):

    data = b''
    dataList = list()
    data = b''

    while True:
        data = getLine(sock)
        if data:
            dataList.append(data)
        else:
            return dataList


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ("127.0.0.1", 9999))
sock.listen() # 参数backlog表明阻塞队列的长度， n+1

skt,addr = sock.accept()

lines = getAllLine(skt)
for line in lines:
    print(line)

rsp = "hello world"
byteRsp = rsp.encode('ASCII')
skt.send(byteRsp)

skt.close()
sock.close()
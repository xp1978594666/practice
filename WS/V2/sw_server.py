import socket




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ("127.0.0.1", 9999))
sock.listen() # 参数backlog表明阻塞队列的长度， n+1

skt,addr = sock.accept()

lines = getAllLine(skt)
for line in lines:
    print(line)

hw = "Hello World"
sendRspAll(skt, hw)

skt.close()
sock.close()
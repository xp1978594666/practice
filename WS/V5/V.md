
# 1 实验目的
- 增加路由功能
- 增加对静态文件的支持

# 2 路由功能
- 增加路由功能需要先对http协议头进行分析，分析出对方请求的文件路径
- 需要修改对http传入信息的读取功能，将所有传入请求信息分析后存入数据结构
- 修改后代码如下：
```python
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
```

- 增加函数reqRoute,对传入请求添加简单路由功能
- 代码如下：
```python


    def startHandler(self):
        self.headHandler()
        self.reqRoute()
        return None

    def reqRoute(self):

        uri = self.headInfo.get("uri","BadReq")
        if uri == "/":
            self.sendWebPage("index.html")
        
        return None
```

# 3 增加对静态ico的处理
- 由于浏览器的固定设置，每次请求完资源后会发送一个对 favicon.ico的请求
- 根据需要，需要增加静态文件favicon.ico 
- 在主目录下建立static文件夹，放入favicon.ico
- 路由模块中添加sendStaticIco
- 会出现错误：
```pytException in thread Thread-12:
Traceback (most recent call last):
  File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/threading.py", line 914, in _bootstrap_inner
    self.run()
  File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/threading.py", line 862, in run
    self._target(*self._args, **self._kwargs)
  File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 13, in startHandler
    self.reqRoute()
  File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 22, in reqRoute
    self.sendStaticIco("favicon.ico")
  File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 52, in sendStaticIco
    ico = f.read()
  File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start bytehon

```
- 解决方案：
    1. 打开文件以 rb形式打开
    2. 发送内容的时候不需要编码，直接发送
    3. 内容不需要附加'\r\n'结尾字符

- 代码如下：
```python

    def reqRoute(self):

        uri = self.headInfo.get("uri","BadReq")
        if uri == "/":
            self.sendWebPage("index.html")
        if uri == "/favicon.ico":
            self.sendStaticIco("favicon.ico")

        return None


    def sendStaticIco(self, path):
        fp =  os.path.join(SocketHandlerContent.base_path, "static", path)
        with open(fp,mode='rb') as f:
            ico = f.read()
            self.__sendRspAll(ico, SocketHandlerContent.content_type_ico)

    def __sendRspLine(self,data):

        if type(data) == bytes:
            self.sock.send(data)
        else:
            data += "\r\n"
            self.sock.send(data.encode("utf-8"))
        return None
```
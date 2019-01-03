
# 1 实验目的
- 添加404反馈
- 添加500反馈
# 2 修改结构和相应代码
- 创建文件夹web
- 其余所有html网页放入web文件夹下
- 修改相应reqRoute代码
- 代码修改后如下：
```python

    def reqRoute(self):

        uri = self.headInfo.get("uri","BadReq")

        if uri == "/":
            self.sendWebPage("web/index.html")
        if uri == "/favicon.ico":
            self.sendStaticIco("static/favicon.ico")
        if uri == "/index.html":
            self.sendWebPage("web/index.html")

        return None
```
- 修改相应的sendWebPage 和 sendStaticIco 代码
- 测试修改后运行情况

# 2 添加404 反馈
- 制作404 静态网页并放入web文件夹
- 修改路由函数，如果访问资源不存在就返回404页面
- 代码如下：
```python

    def reqRoute(self):

        uri = self.headInfo.get("uri", "BadReq")

        htmlUri = os.path.join(SocketHandlerContent.base_path, "web", uri)
        icoUri = os.path.join( SocketHandlerContent.base_path, "static", uri)

        if not os.path.exists(htmlUri) and not os.path.exists(icoUri):
            print('ERROR')
            self.sendWebPage("web/404.html")

        if uri == "/":
            self.sendWebPage("web/index.html")
        if uri == "/favicon.ico":
            self.sendStaticIco("static/favicon.ico")
        if uri == "/index.html":
            self.sendWebPage("web/index.html")

        return None
```

# 3 添加505反馈
- 添加505页面
- 异常处理中添加505反馈
- 示例只采用一个异常处理
- 代码如下：
```python

    def reqRoute(self):

        try:
            uri = self.headInfo['uri']
            #uri = self.headInfo.get("uri")
        except Exception:
            self.sendWebPage(SocketHandlerContent.file_500)
            return None

        htmlUri = os.path.join(SocketHandlerContent.base_path, "web", uri)
        icoUri = os.path.join( SocketHandlerContent.base_path, "static", uri)

        if not os.path.exists(htmlUri) and not os.path.exists(icoUri):
            self.sendWebPage(SocketHandlerContent.file_404)

        if uri == "/":
            self.sendWebPage(SocketHandlerContent.file_index)
        if uri == "/favicon.ico":
            self.sendStaticIco(SocketHandlerContent.file_ico)
        if uri == "/index.html":
            self.sendWebPage(SocketHandlerContent.file_index)

        return None
```

# 4 添加特殊返回时的返回头信息
- 重构函数 sendWebPage
- 重构函数 sendRspAll
- 代码如下：
```python

    def sendWebPage(self, path, code="200"):
        fp =  os.path.join(SocketHandlerContent.base_path, path)
        with open(fp,mode='r') as f:
            html = f.read()
            self.__sendRspAll(html, code=code)
            
    def __sendRspAll(self,
                     data,
                     content_type = SocketHandlerContent.content_type_html,
                     code="200"):

        if code == "404":
            self.__sendRspLine(SocketHandlerContent.head_protocal +
                               SocketHandlerContent.head_code_404 +
                               SocketHandlerContent.head_status_NOTFOUND)
        if code == "500":
            self.__sendRspLine(SocketHandlerContent.head_protocal +
                               SocketHandlerContent.head_code_500 +
                               SocketHandlerContent.head_status_INTERNAL_ERROR)
        if code == "200":
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
```

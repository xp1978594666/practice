class SocketHandlerContent:
    head_protocal = "HTTP/1.1 "
    head_code_200 = "200 "
    head_status_OK = "OK"

    head_code_404 = "404"
    head_status_NOTFOUND = "NOT_FOUND"
    head_code_500 = "500"
    head_status_INTERNAL_ERROR = "INTERNAL_SERVER_ERROR"

    head_content_length = "Content-Length: "
    head_content_type = "Content-Type: "
    content_type_html = "text/html"
    content_type_ico = "application/x-ico"
    content_type_pic = "application/x-pic"

    blank_line = ""

    base_path = r'/home/augsnano/workspace/WS/webapp'

    file_index = "web/index.html"
    file_500 = "web/500.html"
    file_404 = "web/404.html"
    file_ico = "static/favicon.ico"
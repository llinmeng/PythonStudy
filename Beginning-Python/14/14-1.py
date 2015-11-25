# -*- coding: utf-8 -*-
# 小型服务器

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind(host, port)

s.listen(5)
while True:
    c, addr = s.accept()

from django.test import TestCase

# Create your tests here.


# 服务端

# import socket
#
# sk = socket.socket()
#
# sk.bind(("127.0.0.1",8080))
# sk.listen(5)
#
# while True:
#     conn,address = sk.accept()
#     conn.sendall(bytes("欢迎光临我爱我家",encoding="utf-8"))
#
#     size = conn.recv(1024)
#     size_str = str(size,encoding="utf-8")
#     file_size = int(size_str)
#
#     conn.sendall(bytes("开始传送", encoding="utf-8"))
#
#     has_size = 0
#     f = open("db_new.jpg","wb")
#     while True:
#         if file_size == has_size:
#             break
#         date = conn.recv(1024)
#         f.write(date)
#         has_size += len(date)
#
#     f.close()

# 客户端

# import socket
# import os
#
# obj = socket.socket()
#
# obj.connect(("127.0.0.1",8080))
#
# ret_bytes = obj.recv(1024)
# ret_str = str(ret_bytes,encoding="utf-8")
# print(ret_str)
#
# size = os.stat("yan.jpg").st_size
# obj.sendall(bytes(str(size),encoding="utf-8"))
#
# obj.recv(1024)
#
# with open("yan.jpg","rb") as f:
#     for line in f:
#         obj.sendall(line)
#
# # 案例二 上传文件

#
# import socket
#
# sk = socket.socket()
# sk.bind(("127.0.0.1",8080))
# sk.listen(5)
#
# conn,address = sk.accept()
# sk.sendall(bytes("Hello world",encoding="utf-8"))

# server



# import socket
#
# obj = socket.socket()
# obj.connect(("127.0.0.1",8080))
#
# ret = str(obj.recv(1024),encoding="utf-8")
# print(ret)



import  socketserver
# 服务端

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request
        conn.sendall(bytes("你好，我是机器人",encoding="utf-8"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes,encoding="utf-8")
            if ret_str == "q":
                break
            conn.sendall(bytes(ret_str+"你好我好大家好",encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),Myserver)
    server.serve_forever()

# 客户端

import socket

obj = socket.socket()

obj.connect(("127.0.0.1",8080))

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str)

while True:
    inp = input("你好请问您有什么问题？ \n >>>")
    if inp == "q":
        obj.sendall(bytes(inp,encoding="utf-8"))
        break
    else:
        obj.sendall(bytes(inp, encoding="utf-8"))
        ret_bytes = obj.recv(1024)
        ret_str = str(ret_bytes,encoding="utf-8")
        print(ret_str)

# 案例一 机器人聊天




from django.shortcuts import render

# Create your views here.


# 服务端

import socket

sk = socket.socket()

sk.bind(("127.0.0.1",8080))
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.sendall(bytes("欢迎光临我爱我家",encoding="utf-8"))

    size = conn.recv(1024)
    size_str = str(size,encoding="utf-8")
    file_size = int(size_str)

    conn.sendall(bytes("开始传送", encoding="utf-8"))

    has_size = 0
    f = open("db_new.jpg","wb")
    while True:
        if file_size == has_size:
            break
        date = conn.recv(1024)
        f.write(date)
        has_size += len(date)

    f.close()

# 客户端

import socket
import os

obj = socket.socket()

obj.connect(("127.0.0.1",8080))

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str)

size = os.stat("yan.jpg").st_size
obj.sendall(bytes(str(size),encoding="utf-8"))

obj.recv(1024)

with open("yan.jpg","rb") as f:
    for line in f:
        obj.sendall(line)

# 案例二 上传文件
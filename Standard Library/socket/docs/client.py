import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

s = socket.socket()
s.connect((HOST, PORT))
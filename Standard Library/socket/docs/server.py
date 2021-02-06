import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print(conn)
print(addr)
print(socket.getnameinfo(addr, socket.NI_DGRAM))

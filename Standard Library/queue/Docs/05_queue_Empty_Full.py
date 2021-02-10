import queue
import sys

q = queue.Queue(5)

try:
    for i in range(1, 7):
        q.put(i, block=False)
except queue.Full as err:
    print("Queue is Full mate cant insert no more!!")
try:
    for i in range(7):
        print(q.get(block=False))
except queue.Empty as err:
    print("Got nothing to show yaa!!")

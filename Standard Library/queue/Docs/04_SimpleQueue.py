import queue
import sys

q = queue.SimpleQueue()
try:
    for i in range(1, 5):
        q.put(i)
except queue.Full as err:
    print("Queue is Full...")
    sys.exit()

while not q.empty():
    print(q.get())

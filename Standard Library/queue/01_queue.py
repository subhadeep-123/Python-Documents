import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

for i in range(10):
    print(q.get())

import queue

q = queue.Queue(10)

for i in range(10):
    q.put(i)
print(f"The size of the queue is - {q.qsize()}")
print(f"Check if Empty - {q.empty()}")
print(f"Check if Full - {q.full()}")

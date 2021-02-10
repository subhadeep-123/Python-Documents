import queue

q = queue.Queue(5)
try:
    for i in range(1, 10):
        q.put(i)
except Exception as err:
    print(err)
while not q.empty():
    print(q.get())
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)

# The terminal will stop to work them upperbound lim is excedded

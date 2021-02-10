from queue import LifoQueue

q = LifoQueue(5)
n = 6
while n != 0:
    q.put(n)
    n -= 1

while not q.empty():
    print(q.get())

# Same if the max size exceded the terminal will freeze to DEATHHHH

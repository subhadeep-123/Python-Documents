import queue
q = queue.PriorityQueue()
q.put((2, "Hello World"))
q.put((11, 11))
q.put((5, 8.55))
q.put((1, True))

while not q.empty():
    print(q.get()[1])

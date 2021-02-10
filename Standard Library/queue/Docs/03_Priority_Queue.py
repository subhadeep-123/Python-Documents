from queue import PriorityQueue
a = [99, 1, 20, 11]
data = ["Subhadeep", "Saanvi", "Ria", "Richard", "Pranab"]

q = PriorityQueue(4)
n = len(a)
while n != 0:
    q.put((a[n-3], data[n-3]))
    n -= 1

while not q.empty():
    print(q.get())

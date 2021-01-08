import threading
import time

ls = []

start = time.time()


def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)


def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)


x = threading.Thread(target=count, args=(10,))
x.start()

y = threading.Thread(target=count2, args=(5,))
y.start()

x.join()
y.join()
end = time.time()
print(f"Total Time{end-start}")
print(ls)

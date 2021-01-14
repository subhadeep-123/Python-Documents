import time
import threading

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = threading.Thread(target=countdown, args=(COUNT//2,))
t2 = threading.Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Total Time Taken - {end - start}")

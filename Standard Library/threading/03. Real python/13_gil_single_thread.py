import time
import threading

COUNT = 10000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print(f"Time Taken in sec - {end-start}")

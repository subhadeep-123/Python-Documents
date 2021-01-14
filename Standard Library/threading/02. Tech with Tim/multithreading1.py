import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}\n")
        print_time(self.name, self.counter, 5)
        print(f"Exiting {self.name}\n")


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{threadName}, {time.ctime(time.time())}, {counter}\n")
        counter -= 1


# Create New thread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1.5)

# Start New Thread
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")

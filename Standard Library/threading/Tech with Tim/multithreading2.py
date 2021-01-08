import time
import threading


class myThread(threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count

    def run(self):  # This does need to be called run
        print(f"Starting...{self.name}\n")
        print_time(self.name, 1, self.count)
        print(f"Exiting...{self.name}\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print(f"{name}, {time.ctime(time.time())}, {count}\n")
        count -= 1


# Creating New Threads
t1 = myThread(1, "Thread-1", 10)
t2 = myThread(2, "Thread-2", 5)
# Running the threads
t1.start()
t2.start()
t1.join()
t2.join()
print("Exiting Main Thread")

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
        # This means do not let any other thread run until this thread is finished
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()  # When the above thread is finished then release this thread
        print(f"Exiting...{self.name}\n")


class myThread2(threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count

    def run(self):  # This does need to be called run
        print(f"Starting...{self.name}\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print(f"Exiting...{self.name}\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print(f"{name}, {time.ctime(time.time())}, {count}\n")
        count -= 1


# Setting a locking object
threadLock = threading.Lock()

# Creating New Threads
t1 = myThread(1, "Payment", 5)
t2 = myThread2(2, "Sending Email", 10)
t3 = myThread2(3, "Loading Page", 3)
# Running the threads
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Exiting Main Thread")

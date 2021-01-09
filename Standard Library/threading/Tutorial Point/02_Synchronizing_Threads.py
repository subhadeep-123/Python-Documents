import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        # Get the Lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # print(f"Exiting {self.name}")
        # Free lock to release next thread
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{threadName}, {time.ctime(time.time())}")
        counter -= 1


threadLock = threading.Lock()
threads = []
# Create new thread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Thread
thread1.start()
thread2.start()
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")

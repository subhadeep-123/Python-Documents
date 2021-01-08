"""
The two threads have interleaving access to a single shared object, 
overwriting each other’s results. Similar race conditions can arise 
when one thread frees memory or closes a file handle before the other 
thread is finished accessing it.

A Lock is an object that acts like a hall pass. Only one thread at a 
time can have the Lock. Any other thread that wants the Lock must wait
until the owner of the Lock gives it up.

The basic functions to do this are .acquire() and .release(). A thread
will call my_lock.acquire() to get the lock. If the lock is already held,
the calling thread will wait until it is released. There’s an important
point here. If one thread gets the lock but never gives it back, your 
program will be stuck. You’ll read more about this later.

Fortunately, Python’s Lock will also operate as a context manager, 
so you can use it in a with statement, and it gets released automatically
when the with block exits for any reason.
"""
import concurrent.futures
import threading
import logging
import time


class FakeDatabase(object):
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info(f"Thread {name} Starting Update")
        logging.debug(f"Thread {name} about to lock")
        with self._lock:
            logging.debug(f"Thread {name} has locked")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug(f"Thread {name} about to release lock")
        logging.debug(
            f"Thread {name} after release lock")
        logging.info(f"Thread {name} finishing update")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    database = FakeDatabase()
    logging.info(
        f"Testing update. Starting value is {database.value}"
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info(
        f"Testing update. Ending value is {database.value}"
    )

"""
the big change here is to add a member called ._lock, which is a threading.Lock() object.
This ._lock is initialized in the unlocked state and locked and released by the with statement.

In this output you can see Thread 0 acquires the lock and is still holding it when it goes to sleep. 
Thread 1 then starts and attempts to acquire the same lock. Because Thread 0 is still holding it, 
Thread 1 has to wait. This is the mutual exclusion that a Lock provides.
"""

import time
import logging
import concurrent.futures

# Using threadpoolexucuter make the job of handling multiple threads very easy and convinent


def thread_func(name):
    logging.info(f"Thread {name} starting...")
    time.sleep(2)
    logging.info(f"Thread {name} finishing...")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executer:
        executer.map(thread_func, range(3))
# The end of the with block causes the threadpoolexucutor to do a .join() on each of the threads in the pool.
# It is strongly recommended that you use ThreadPoolExecutor as a context manager when you can so that you never forget to .join() the threads.

# THe scheduling of threads is done by the operating system making the code execute in a weird fashion

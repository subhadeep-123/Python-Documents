# Race conditions can occur when two or more threads access a shared piece of data or resource
import concurrent.futures
import logging
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info(f"Thread {name} starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info(f"Thread {name} finishing update")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    database = FakeDatabase()
    logging.info(f"Testing update. Starting value is {database.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # .submit() has a signature that allows both positional and named
            # arguments to be passed to the function running in the thread:
            # .submit(function, *args, **kwargs)
            executor.submit(database.update, index)
    logging.info(f"Testing update. Ending value is {database.value}")

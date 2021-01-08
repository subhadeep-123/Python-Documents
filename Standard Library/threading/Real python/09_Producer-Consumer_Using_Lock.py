"""
Since this is an artice about python threading and since you just
read about the Lock primitive, let's try to solve this problem with
two threads using a Lock or two.

The general design is that there is a producer thread that reads from
the fake network and puts the message into a Pipeline:
"""
import random
import logging
import threading
import concurrent.futures

SENTINEL = object()


class Pipeline:
    """
    Class to allow a single element pipeline
    between producer and consumer.
    """

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug(f"{name} about to acquire getLock")
        self.consumer_lock.acquire()
        logging.debug(f"{name} Have getLock")
        message = self.message
        logging.debug(f"{name} About to release setLock")
        self.producer_lock.release()
        logging.debug(f"{name} setLock released")
        return message

    def set_message(self, message, name):
        logging.debug(f"{name} about to acquire setLock")
        self.producer_lock.acquire()
        logging.debug(f"{name} have setLock")
        self.message = message
        logging.debug(f"{name} About to release getLock")
        self.consumer_lock.release()
        logging.debug(f"{name} getLock released")


def producer(pipeline):
    """
    Pretend that we are getting a message from the network.
    """
    for _ in range(10):
        message = random.randint(1, 101)
        logging.info(f"Producer got message {message}")
        pipeline.set_message(message, "Producer")
    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """
    Pretend we're saving a number in the database.
    """
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info(f"Consumer Storing message {message}")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)

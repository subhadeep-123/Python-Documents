"""
Python’s standard library has a queue module which, in turn, has a Queue class. Let’s change the Pipeline 
to use a Queue instead of just a variable protected by a Lock. You’ll also use a different way to stop 
the worker threads by using a different primitive from Python threading, an Event.

Let’s start with the Event. The threading.Event object allows one thread to signal an event while many 
other threads can be waiting for that event to happen. The key usage in this code is that the threads 
that are waiting for the event do not necessarily need to stop what they are doing, they can just check 
the status of the Event every once in a while.

The triggering of the event can be many things. 
In this example, the main thread will simply sleep for a while and then .set() it:
"""
import concurrent.futures
import threading
import logging
import random
import queue
import time


class Pipeline(queue.Queue):

    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug(f"{name} About to get from queue")
        value = self.get()
        logging.debug(f"{name} got {value} from queue")
        return value

    def set_message(self, value, name):
        logging.debug(f"{name} about to add {value} to queue")
        self.put(value)
        logging.debug(f"{name} added {value} to queue")


def producer(pipeline, event):
    """
    Pretend we're getting a number from the network.
    """
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info(f"Producer got message {message}")
        pipeline.set_message(message, "Producer")
    logging.info("Producer received EXIT event. Exiting")


def consumer(pipeline, event):
    """
    Pretend we're saving a number in the database.
    """
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            f"Consumer Storing message {message} queue size = {pipeline.qsize()}"
        )
    logging.info(f"Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main:     About to set event")
        event.set()
"""
The core devs who wrote the standard library knew that a Queue is frequently used in multi-threading 
environments and incorporated all of that locking code inside the Queue itself. Queue is thread-safe.
"""

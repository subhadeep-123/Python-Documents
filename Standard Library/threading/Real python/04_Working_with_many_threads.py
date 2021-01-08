import time
import logging
import threading


def thread_func(name):
    logging.info(f"Thread {name} starting...")
    time.sleep(2)
    logging.info(f"Thread {name} finishing...")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = []
    for index in range(3):
        logging.info(f"Main      :Create and Start Thread {index}")
        x = threading.Thread(target=thread_func,
                             args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main      :Before Joinig Thread {index}")
        thread.join()
        logging.info(f"Main      :Thread {index} done")

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
    logging.info("Main      :Before Creating Thread")
    x = threading.Thread(target=thread_func, args=(1,))
    logging.info("Main      :After Creating Thread")
    x.start()
    name = threading.get_ident()  # this function retuns a unique name for each thread
    logging.info("Main      :Wait for the thread to finish")
    logging.info("Main      :All done!")
    print(name)

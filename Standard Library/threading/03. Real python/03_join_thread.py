#
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
    x = threading.Thread(target=thread_func,
                         args=(1,),
                         daemon=True)
    logging.info("Main      :After Creating Thread")
    x.start()
    name = threading.get_ident()
    logging.info("Main      :Wait for the thread to finish")
    x.join()
    logging.info("Main      :All done!")
    print(name)
# No matter is we have daemon set True or not adding .join() will
# always make the thread wait for the program to finish before ending.

"""
A daemon is a process that runs in the background
"""
# Python threading has a more specific meaning for daemon.
# A daemon thread will shut down immediately when the program exits.
# One way to think about these definations is to consider the daemon thread
# a thread that runs in the background without worrying about shutting down
# If a program is running threads that is not daemon, then the program will wait
# for those threads to complete before it terminates THreads that are daemons,
# however are just killed whenever they are when the program is exiting

# When a program ends, part of the shutdown process is to clean up the threading routine.
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
    name = threading.get_ident()  # this function retuns a unique name for each thread
    logging.info("Main      :Wait for the thread to finish")
    logging.info("Main      :All done!")
    print(name)
# The diff is a non daomonic thread will wait for the thread to finish
# Wherer a daemon thread will exit as soon as the program is complete

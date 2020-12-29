# This is an example where we learn how to run code concurrenty
# For running code in parallel we need to use multiprocessing
# We can benifit from threading when our task are I/O bound.
# When the task is CPU Bound , multi processing makes more sense.
import threading
import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 sec..')
    time.sleep(1)
    print('Done Sleeping..')


# we are passing in the function in the func only, unexecuted
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t1.start()
t2.start()

# THis is to makesure the threads completes before it moves on to calculating the finish time
t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

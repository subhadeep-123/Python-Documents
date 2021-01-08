import threading
import time


def func():
    print("ran\n")
    time.sleep(1)
    print('done')
    time.sleep(1)
    print('Done Sleeping..')


x = threading.Thread(target=func)
x.start()
print(threading.active_count())
time.sleep(1.2)
print("Finally")
print(threading.active_count())

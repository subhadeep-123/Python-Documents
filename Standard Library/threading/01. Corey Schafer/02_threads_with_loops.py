import time
import threading

start = time.perf_counter()


def do_something():
    print('Sleeping 1 sec..')
    time.sleep(1)
    print('Done Sleeping..')


# thread.join() loop is a bad idea and it means we are basically running it synchrounously
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

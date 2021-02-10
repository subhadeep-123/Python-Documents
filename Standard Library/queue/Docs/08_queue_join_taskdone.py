import threading
import queue

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f"Working on Item - {item}")
        print(f"Finished - {item}")
        q.task_done()


# turn-on the worker thread
thread = threading.Thread(target=worker, daemon=True)
thread.start()

# send thirty task request to the worker
for item in range(30):
    q.put(item)
print('All task request are sent\n', end='')

# block untill all task are done
q.join()
print('All work Completed')

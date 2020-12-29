import concurrent.futures
import time
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'


with concurrent.futures.ThreadPoolExecutor() as executer:
    results = [executer.submit(do_something, 1) for i in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

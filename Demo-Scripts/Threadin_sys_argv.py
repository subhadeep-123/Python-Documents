import os
import sys
import time
import threading

def doStuff():
	if os.path.exists(sys.argv[1]):
		mode = 'a'
	else:
		mode = 'w'
	with open(sys.argv[1], mode) as f:
		f.write(sys.argv[2])
		f.write('\n')
	time.sleep(1)

def doMoreStuff():
        if os.path.exists(sys.argv[1]):
                mode = 'a'
        else:
                mode = 'w'
        with open(sys.argv[1], mode) as f:
                f.write(sys.argv[2])
                f.write('\n')
        time.sleep(1)

if __name__ == '__main__':
	threads = []
	for _ in range(10):
		thread1 = threading.Thread(target=doStuff)
		thread2 = threading.Thread(target=doMoreStuff)
		thread1.start()
		thread2.start()
		threads.append(thread1)
		threads.append(thread2)
	for thread in threads:
		thread.join()
#	doStuff()

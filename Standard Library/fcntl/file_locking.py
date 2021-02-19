import fcntl
import time
import sys

while True:
	try:
		with open(sys.argv[1], 'a') as file:
			fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
			file.write(f"{sys.argv[2]}\n")
			fcntl.flock(file, fcntl.LOCK_UN)
			break
	except IOError as err:
		time.sleep(0.05)

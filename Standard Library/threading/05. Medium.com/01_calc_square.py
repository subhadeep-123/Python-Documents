import time
import threading


def calc_sq(num):
    print("Calculate Square numbers: ")
    for n in num:
        time.sleep(1)
        print(f"Square {n*n}\n")


def calc_cube(num):
    print("Calculate Cube numbers: ")
    for n in num:
        time.sleep(1)
        print(f"Cube {n*n*n}\n")


arr = [2, 3, 8, 9]
start = time.time()

t1 = threading.Thread(target=calc_sq, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print(f"In the main thread, time taken {end-start}")

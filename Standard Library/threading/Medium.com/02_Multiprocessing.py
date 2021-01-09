import time
import multiprocessing


def calc_square(number):
    for n in number:
        time.sleep(5)  # artificial time-delay
        print('square: ', str(n*n))


def calc_cube(number):
    for n in number:
        time.sleep(5)
        print('cube: ', str(n*n*n))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    # creating two Process here pt1 & p2
    p1.start()
    p2.start()
    # starting Processes here parallelly by usign start function.
    p1.join()
    # this join() will wait until the cal_square() function is finised.
    p2.join()
    # this join() will wait unit the cal_cube() function is finised.
    print("Successed!")

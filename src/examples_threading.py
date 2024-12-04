import os
import threading
import time


def print_cube(num):
    print("Cube: {}, Thread: {}, Process: {}".format(num * num * num, threading.current_thread().name, os.getpid()))

    # {}
    # ".format(threading.current_thread().name))


def print_square(num):
    time.sleep(1)  # simulate the computation latency
    print("Square: {}, Thread: {}, Process: {}".format(num * num, threading.current_thread().name, os.getpid()))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,), name="t1")
    t2 = threading.Thread(target=print_cube, args=(10,), name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

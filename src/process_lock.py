# Python program to illustrate
# the concept of race condition
# in multiprocessing
import multiprocessing
import os


# function to withdraw from account
def withdraw(balance):
	for _ in range(10000):
		balance.value = balance.value - 1

# function to deposit to account
def deposit(balance):
	for _ in range(10000):
		balance.value = balance.value + 1

def perform_transactions():

	# initial balance (in shared memory)
	balance = multiprocessing.Value('i', 100)

	# creating new processes
	p1 = multiprocessing.Process(target=withdraw, args=(balance,))
	p2 = multiprocessing.Process(target=deposit, args=(balance,))

	# starting processes
	p1.start()
	p2.start()

	# wait until processes are finished
	p1.join()
	p2.join()

	# print final balance
	print("Final balance = {}, pid={}".format(balance.value, os.getpid()))


def withdraw_lock(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

# function to deposit to account
def deposit_lock(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_transactions_lock():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating a lock object
    lock = multiprocessing.Lock()

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw_lock, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit_lock, args=(balance, lock))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes are finished
    p1.join()
    p2.join()

    # print final balance
    print("Final balance locked = {}, pid={}".format(balance.value, os.getpid()))

if __name__ == "__main__":

    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions_lock()
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()



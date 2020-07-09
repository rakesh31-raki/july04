"""thread sync using semaphore pool"""

import threading
from time import sleep
from random import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


class Pool:
    def __init__(self):
        self.pool = []

    def add(self, thread_name):
        self.pool.append(thread_name)
        logging.debug(f'added to the pool : {self}')

    def remove(self, thread_name):
        self.pool.remove(thread_name)
        logging.debug(f'removed from the pool : {self}')

    def __str__(self):
        return str(self.pool)


def worker(pool, sema):
    """thread function"""
    t_name = threading.current_thread().name
    # sleep(random())
    logging.debug(f'waiting to join the pool: {pool}')

    with sema:
        # critical section
        pool.add(t_name)
        sleep(2)
        print(f'{t_name}: finished the Critical Section of the code')
        pool.remove(t_name)


def main():
    """main thread"""
    pool = Pool()
    sema = threading.Semaphore(3)  # sync using semaphore
    list_of_threads = []

    for item in range(1, 8):
        t = threading.Thread(target=worker, args=(pool, sema))
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()  # blocked  main thread to wait for the child threads to terminate

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()


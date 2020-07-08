""" multithreading """

import threading
from time import sleep
from random import random


def worker(delay):
    """child thread function"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    # sleep(delay)
    print(t_name, ' waited for the :', delay)


def main():
    """main thread"""

    list_of_threads = []

    for item in range(1, 6):
        interval = random()
        t = threading.Thread(target=worker, args=(interval,), name=f't{item}')
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()  # blocked  main thread to wait for the child threads to terminate

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()

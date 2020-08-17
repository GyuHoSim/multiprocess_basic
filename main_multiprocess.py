import os
from multiprocessing import Process


def do_something(x):
    pid = os.getpid()
    print(f'[{pid} start]')
    for item in x:
        result = item ** 2
        print(f'[{pid}] result: {result}')


def do_something_2(x):
    pid = os.getpid()
    print(f'[{pid} start]')
    for item in x:
        result = item * 2
        print(f'[{pid}] result: {result}')


def main_1():
    item = [[2, 2], [3], [6, 2, 3, 4], [544, 2, 3], [3]]
    procs = []

    for item in item:
        proc = Process(target=do_something, args=(item,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


def main():
    items = [do_something, do_something_2]
    x = [2, 3, 6, 544, 3]
    procs = []

    for item in items:
        proc = Process(target=item, args=(x,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    main_1()

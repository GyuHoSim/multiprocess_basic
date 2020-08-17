from multiprocessing import Pool
import os
import time


def do_something(x):
    print('%s' % os.getpid())
    time.sleep(1)
    return x*x


if __name__ == '__main__':
    pool = Pool(5)
    print(pool.map(do_something, range(0, 10)))

import os

from multiprocessing import Process, Queue

SENTINEL = -1


def creator(data, q):
    """
    creates data to be consumed and waits for consumer
    to finish processing -> use SENTINEL

    :param data:
    :param q:
    :return:
    """
    pid = os.getpid()
    print(f'[{pid}]Creating data and putting in on the queue')

    for item in data:
        q.put(item)


def consumer(q):
    """
    consumes some data and works on it
    :param q:
    :return:
    """
    pid = os.getpid()
    while True:
        data = q.get()
        if data is SENTINEL:
            print("end process")
            break

        print(f'[{pid}]data found to be processed: {data}')
        processed = data * 2
        print(processed)


def main():
    q = Queue()
    data = [4, 24, 22, 12, -1]

    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=consumer, args=(q,))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()


if __name__ == '__main__':
    main()

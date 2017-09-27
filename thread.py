from multiprocessing import Process, Pool, Queue
import os
import time
import random


def child_do(name):
    print('child\'s ID is ' + str(os.getpid()) + ' name is ' + name)


def do_work(name):
    print('work ' + name + str(os.getpid()) + ' is doing')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('work ' + name + ' takes ' + str(end - start))


def write(queue):
    print('write proccess ID is ' + str(os.getpid()))
    for value in ['a', 'b', 'c']:
        print('put value ' + value + ' in queue')
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    print('read proccess ID is ' + str(os.getpid()))
    while True:
        result = queue.get(True)
        print('get value ' + result)
        if result == 'c':
            break


if __name__ == '__main__':
    print('parent\'s ID is ' + str(os.getpid()))
    queue = Queue()
    pw = Process(target=write, args=(queue,))
    pr = Process(target=read, args=(queue,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(func=do_work, args=(str(i),))
    # print('Let\'s begin!')
    # p.close()
    # p.join()
    # p = Process(target=child_do, args=('text',))
    # p.start()
    # p.join()
    print('All proccess are done')


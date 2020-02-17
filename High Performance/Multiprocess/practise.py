import os
from multiprocessing import Queue, Pool, Process
import subprocess
import time
import random


def run_fast(name):
    print('Fast Run process %s (%s)' % (name, os.getpid()))


def run_slow(name):
    time.sleep(1)
    print('Slow Run process %s (%s)' % (name, os.getpid()))


def run_rand(name):
    time.sleep(random.random()*3)
    print('Random Run process %s (%s)' % (name, os.getpid()))


def write(q: 'Queue'):
    for _ in ['A', 'B', 'C', 'D']:
        q.put(_)
        print('process %s write %s into queue.' % (os.getpid(), _))
        time.sleep(random.random())


def read(q: 'Queue'):
    while True:
        p = q.get(True)
        print('process %s read %s from queue.' % (os.getpid(), p))


if __name__ == '__main__':
    # print('example one')
    # p1 = Process(target=run_fast, args=('哈哈',))
    # p2 = Process(target=run_slow, args=('呵呵',))
    #
    # print('-------------start slow run p2---------------')
    # p2.start()
    # print('-------------end slow run p2---------------')
    #
    # print('-------------start fast run p1---------------')
    # p1.start()
    # p1.join()
    # print('-------------end fast run p1---------------')
    #
    # time.sleep(1)
    # # print('\nexample two')
    # # subprocess.call(['nslookup', 'localhost:8080'])
    #
    # print('\nexample three')
    # p = subprocess.Popen('nslookup', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, *_ = p.communicate(b'localhost:8080')
    # print(output.decode('gbk'))
    # print('exit code:', p.returncode)

    # print('\nexample four')
    # p = Pool(8)
    # for i in range(8):
    #     print('start run', i)
    #     p.apply_async(run_rand, args=(str(i),))
    #     print('end run', i)
    # print('Waiting for all process done.')
    # p.close()
    # p.join()

    print('\nexample five')
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))

    print('start write----------')
    p1.start()
    print('start read----------')
    p2.start()

    p1.join()
    p2.terminate()
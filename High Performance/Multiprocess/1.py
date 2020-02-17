from multiprocessing import Process
import os
import time


# 子进程要执行的代码
def run_proc(name):
    time.sleep(1)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    # 例1
    print('---------------------------------')
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    # 启动子进程
    p.start()
    # join() 方法，可以让其它进程等待该子进程执行；若注释掉，则因为sleep(1)，main进程将不等待子进程执行完毕
    p.join()
    print('Child process end.')
    print('---------------------------------')

    # 例2
    print('---------------------------------')
    p1 = Process(target=run_proc, args=('p1', ))
    p2 = Process(target=run_proc, args=('p2', ))
    print('Child process 1 will start.')
    p1.start()
    print('Child process 1 end.')
    print('Child process 2 will start.')
    p2.start()
    print('Child process 2 end.')
    print('---------------------------------')

    p1.join()
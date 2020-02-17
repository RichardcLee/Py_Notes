import threading
import time


exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ', self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting ', self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.current_thread().exit()   # 当前进程退出
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


t1 = MyThread(1, 'Thread-1', 1)
t2 = MyThread(2, 'Thread-2', 2)

t1.start()
t2.start()

t1.join()
t2.join()

print('Exit Main Thread')
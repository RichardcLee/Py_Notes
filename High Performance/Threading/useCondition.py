from threading import Thread, Condition
import time

'''
    Condition（条件变量）通常与一个锁关联。
    需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。
    可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，
    直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
    
    
'''

items = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
       Thread.__init__(self)

    def consume(self):
        global condition
        global items

        condition.acquire()  # 调用关联的锁的相应方法
        if len(items) == 0:
            print('Consumer notify : no item to consume')
            condition.wait()  # 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
        items.pop()
        print('Consumer notify : consumed 1 item')
        print('Consumer notify : items to consume are ' + str(len(items)))
        condition.notify()  # 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。
        condition.release()  # 调用关联的锁的相应方法, 释放占用的共享资源

    def run(self):
        for i in range(0, 20):
            # time.sleep(2)
            time.sleep(4)
            self.consume()


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            print('Producer notify : items produced are ' + str(len(items)))
            print('Producer notify : stop the production!!')
            condition.wait()
        items.append(1)
        print('Producer notify : total items produced ' + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            # time.sleep(4)
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()


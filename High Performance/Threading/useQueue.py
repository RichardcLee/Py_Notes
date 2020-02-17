from threading import Thread, Event
from queue import Queue
import time
import random


class Producer(Thread):
    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)      # 队列满则阻塞
            print('Producer notify : item N°%d append to queue by %s \n' % (item, self.name))
            time.sleep(1)


class Consumer(Thread):
    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()     # 队列空则阻塞
            print('Consumer notify : %d popped from queue by %s\n' % (item, self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
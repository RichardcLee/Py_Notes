from threading import Thread
from time import sleep
from os import getpid


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello python cookbook!\n'

    def print_message(self):
        print(self.message)

    def run(self):
        print('Thread %s starting!\n' % self.getName())
        x = 0
        while x < 10:
            self.print_message()
            sleep(2)
            x += 1
        print('Thread %s ended!' % self.getName())


print('Process %d Started!' % getpid())

hello_py = CookBook()

hello_py.start()
hello_py.join()

print('Process %d ended!' % getpid())

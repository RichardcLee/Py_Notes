import threading
import time

balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        # 先要获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 执行完毕，不要忘了释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
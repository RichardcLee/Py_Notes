from threading import Thread


class threads_object(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        function_to_run()


class nothreads_object(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()


def threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


# first try
# def function_to_run():
#     pass

# second try
# def function_to_run():
#     a, b = 0, 1
#     for i in range(10000):
#         a, b = b, a+b
#         # yield a

# third try
# def function_to_run():
#     with open('data.dat', 'rb') as f:
#         size = 1024
#         for i in range(2000):
#             f.read(size)

# fourth try
def function_to_run():
    import requests
    for i in range(2):
        res = requests.get('http://www.baidu.com', timeout=2)


def show_results(func_name, results):
    print('%-23s %4.6f seconds' % (func_name, results))


if __name__ == '__main__':
    import sys
    from timeit import Timer

    repeat = 100
    number = 1
    number_threads = [1, 2, 4, 8]

    print('Starting tests')
    for i in number_threads:
        t = Timer('non_threaded(%s)' % i, 'from __main__ import non_threaded')
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results('non_threaded (%s iters)' % i, best_result)

        t = Timer('threaded(%s)' % i, 'from __main__ import threaded')
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results('threaded (%s threads)' % i, best_result)

    print('Iteration completes')
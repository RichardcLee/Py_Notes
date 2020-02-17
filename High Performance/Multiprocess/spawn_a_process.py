import multiprocessing


def foo(i):
    print('called function in process: %s' % i)
    return


if __name__ == '__main__':
    # Process_jobs = []
    # for i in range(5):
    #     p = multiprocessing.Process(target=foo, args=(i,))
    #     Process_jobs.append(p)
    #     p.start()
    #     p.join()

    # 结果同上
    from target_function import function
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
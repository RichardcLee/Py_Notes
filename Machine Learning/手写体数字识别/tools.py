'''
project: 工具包
author: 李云浩
date: 2018.1.16
'''

import time


# 装饰器，用于增加提示信息和报时
def timer(prompt1: str=None, prompt2: str=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if prompt1 is not None:
                print(prompt1)
            start = time.time()
            func(*args, *kwargs)
            end = time.time()
            if prompt2 is not None:
                print(prompt2, end=' ')
            print('共耗时：', end-start, 's')
        return wrapper
    return decorator


if __name__ == '__main__':
    @timer('开始处理', '处理完毕，')
    def hhe(a=0, b=10000):
        for i in range(a, b):
            time.sleep(0.1)


    hhe(0, 10)
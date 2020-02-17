'''
简要

yield是生成器中的一个关键字,他的作用和返回差不多,但是又有很大的区别:

1.下一次迭代时，从上一次迭代遇到的yield后面的代码开始执行



2.简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始。



3.第一次调用时必须先next()或send(None)，否则会报错，send后之所以为None是因为这时候没有上一个yield。可以认为，next()等同于send(None)。

 ----next()和send(None)会是生成器函数执行一遍,然后到yield的地方停下,下一次使用next(),send(None)时,从这个地方开始



4.send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，而yield的参数是返回给调用者的值。
'''

"-------------------yield from"
def chain(*args):
    for it in args:
        yield from it
print(list(chain("1234", "AB", [1, 2, 3, 4, 5])))


"-------------------理解yield from"
def yield_test(n):
    for i in range(n):
        yield call(i)
        print('生成器中的i=', i)
    print('do something...')
    print('end')
def call(i):
    return i*2
for i in yield_test(5):
    print('for中的i=', i)


"-------------------扁平化处理嵌套型数据"
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x, end=' ')
print()
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x, end=' ')
print()


"-------------------使用yield from 写一个异步爬虫"
import requests
from collections import namedtuple

# 类名ｒｓ，属性ｕｒｌ和ｓｔａｔｕｓ
Response = namedtuple('response', 'url status res')

# 子生成器
def fetch():
    res = []
    while 1:
        url = yield  # 执行到这里时先yield，然后转出到main的ul.send()处，此时url=还未执行
        # 从main转来，继续执行，注意上面url的此时已被赋值了！
        if url is None:
            break
        req = requests.get(url)
        res.append(Response(url=url, status=req.status_code, res=req))
    return res

# 委派生成器
def url_list(l, key):
    while 1:
        l[key] = yield from fetch()   # 从main转来，启动下一次迭代，转到fetch

# 调用方
def main(urls):
    l = {}
    u = urls
    for index, url in enumerate(u):
        if index == 0:
            ul = url_list(l, index)  # 注意这一步！调用后返回的是一个迭代器对象！而不会立即进入url_list函数执行！
            next(ul)  # 执行next或send(None)后，转入url_list执行！
            # ul.send(None)  # 同样的效果
        ul.send(url)  # 从fetch处转来，执行这条语句，send一个url到fetch方法的url = yield处，但先转到url_list处
    ul.send(None)
    return l


if __name__ == '__main__':
    res = main(["http://www.baidu.com", "http://www.cnblogs.com", "http://www.segmentfault.com", "http://www.4399.com"])
    print(res)

    res = main(["http://www.cctv.com", "http://m.weibo.com", "http://www.youku.com"])
    print(res)




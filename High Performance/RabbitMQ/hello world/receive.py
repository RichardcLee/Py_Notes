import pika

# 与本地机器建立代理连接
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 我们需要确认队列是存在的。我们可以多次使用queue_declare命令来创建同一个队列，但是只有一个队列会被真正的创建
''' 你也许要问: 为什么要重复声明队列呢 —— 我们已经在前面的代码中声明过它了。
如果我们确定了队列是已经存在的，那么我们可以不这么做，比如此前预先运行了send.py程序。
可是我们并不确定哪个程序会首先运行。这种情况下，在程序中重复将队列重复声明一下是种值得推荐的做法。
'''
channel.queue_declare(queue='hello')
# cmd: rabbitmqctl list_queues


# 为队列定义一个回调（callback）函数, 当我们获取到消息的时候，Pika库就会调用此回调函数。
# 这个回调函数会将接收到的消息内容输出到屏幕上
def callback(ch, method, properties, body):
    print('[x] Received %r' % body)


# 我们需要告诉RabbitMQ这个回调函数将会从名为"hello"的队列中接收消息：
channel.basic_consume('hello', callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



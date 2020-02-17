# 创建一个工作队列（Work Queue），它会发送一些耗时的任务给多个工作者（Worker）。
'''工作队列（又称：任务队列——Task Queues）是为了避免等待一些占用大量资源、时间的操作。
当我们把任务（Task）当作消息发送到队列中，一个运行在后台的工作者（worker）进程就会取出任务然后处理。
当你运行多个工作者（workers），任务就会在它们之间共享。
这个概念在网络应用中是非常有用的，它可以在短暂的HTTP请求中处理一些复杂的任务。
'''
import pika

MESSAGE = ['1...', '2....', '3....', '4.', '5...', '6..', '7.', '8....', '9...', '10..', '11.....', '12......',
           '13...', '14.....', '15.', '16..', '17.', '18.', '19..', '20...', '21.......', '22..', '23...', '24.....',
           '25.....']


# 与本地机器建立代理连接
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)

# 创建一个队列
channel.queue_declare(queue='hello', durable=True)

# message = ''.join(sys.argv[1:]) or "Hello World!"
for i in range(len(MESSAGE)):
    message = MESSAGE[i]
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(" [x] Sent %r" % (message,))

# 在退出程序之前，我们需要确认网络缓冲已经被刷写、消息已经投递到RabbitMQ。通过安全关闭连接可以做到这一点
connection.close()
import pika

# 与本地机器建立代理连接
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 创建一个队列
channel.queue_declare(queue='hello')

message = input('send message: ')
# 在RabbitMQ中，消息是不能直接发送到队列中的，这个过程需要通过交换机（exchange）来进行, ''代表默认交换机
channel.basic_publish(exchange='', routing_key='hello', body=message)
print("[x] send '%s'" % message)


# 在退出程序之前，我们需要确认网络缓冲已经被刷写、消息已经投递到RabbitMQ。通过安全关闭连接可以做到这一点
connection.close()





import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 持久化
channel.queue_declare(queue='hello', durable=True)
# cmd: rabbitmqctl list_queues


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(str(body).count('.'))
    print(" [x] Done")
    # ch.basic_ack(delivery_tag=method.delivery_tag)


# 我们需要告诉RabbitMQ这个回调函数将会从名为"hello"的队列中接收消息：
channel.basic_consume('hello', callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()





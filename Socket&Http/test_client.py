import codecs
import socket
import threading


# 客户端
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.connect(('127.0.0.1', 2333))

s2.sendto('hello'.encode('utf-8'), ('127.0.0.1', 2333))

print(s2.recv(1024).decode('utf-8'))
print(s1.recv(1024).decode('utf-8'))
choice = input()
s1.send(choice.encode('utf-8'))
data = s1.recv(1100000)
if choice == '3':
	with open('pic_from_server.jpg', 'wb') as f:
		f.write(data)
else:
	print(data.decode('utf-8'))


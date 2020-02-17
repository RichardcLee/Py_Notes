import threading
import socket
import codecs


# 服务器端

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDP 和 TCP不冲突
s1.bind(('127.0.0.1', 2333))
s2.bind(('127.0.0.1', 2333))

s1.listen(5)


def processTCP(socket, addr):
	print('tcp connected with %s:%s' % addr)
	socket.send('请选择：\n1.对话\t 2.背诗\t 3.下载图片\t exit.关闭服务器'.encode('utf-8'))
	data = socket.recv(1024)
	if not data or data.decode('utf-8') == 'exit':
		return False
	data = data.decode('utf-8')
	if data == '1':
		socket.send('hello! boy/girl?'.encode('utf-8'))
	elif data == '2':
		socket.send('黄河之水天上来，迸流到海不复还'.encode('utf-8'))
	elif data == '3':
		with open('pic_in_server.png', 'rb') as f:
			socket.sendfile(f)
	return True
	

def processUDP():
	data, addr = s2.recvfrom(1024) 
	print('udp connected with %s:%s' % addr)
	print('upd receive %s' % data.decode('utf-8'))
	s2.sendto('Welcome!'.encode('utf-8'), addr)

print('waiting for connection...')
while True:
	socket, addr1 = s1.accept()
	processUDP()
	res = processTCP(socket, addr1)
	if res == False:
		break
	t1 = threading.Thread(name='tcp-thread', target=processTCP, args=(socket, addr1))
	t2 = threading.Thread(name='udp-thread', target=processUDP, args=())
	t1.start()
	t2.start()
	
	
	
	
	
	
	
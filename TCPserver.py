def serve(c,h):
	print("connected to host  " + h)
	while True:
		
		message=c.recv(1024)
		message=str(message.decode("ascii"))
		if message=="bye" +"\n":
			break
		
		print ("From client " + host +" ->  " + message)
		capital=message.upper()
		b=bytes(capital,'utf-8')
		c.send(b)
	c.close()	
		
		
	
from socket import *
from _thread import *
import threading
serverPort = 11115
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print ('The server is ready to receive')
while 1:
	connectionSocket, (host,port) = serverSocket.accept()
	start_new_thread(serve, (connectionSocket,host,))
	

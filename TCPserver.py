def serve(c,h):
	print("connected to host  " + h)
	message=c.recv(1024)
	message=str(message.decode("ascii"))
	
		
	print ("From client " + host +" ->  " + message)
		
	b=bytes(message,'utf-8')
	c.send(b)
	c.shutdown(1)			
		
		
		
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
	

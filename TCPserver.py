def serve(c,h,port):
	print("connected to host  " + h + "  port " +str(port))
	#c.settimeout(5.0)
	
	message=c.recv(1024)
	if not message:
		c.close()
	message=str(message.decode("ascii"))		
	print ("From client " + host + " port "+str(port) +"  ->  " + message)		
	b=bytes(message,'utf-8')
	c.send(b)
		
	c.close()				
		
		
		
	
from socket import *
from _thread import *
import threading
serverPort = 11115
serverIP="10.64.10.243"
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverIP,serverPort))
serverSocket.listen(10)
connection=False
print ('The server is ready to receive')

while 1:
	try:
		connectionSocket, (host,port) = serverSocket.accept()
		connection=True
		start_new_thread(serve, (connectionSocket,host,port,))
	except KeyboardInterrupt:
		break	
if connection:
	print("closing connection")
	connectionSocket.close()
	serverSocket.close()	

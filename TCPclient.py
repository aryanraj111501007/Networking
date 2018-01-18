def sendmsg(c):
	while True:
		
		message=input()
		message+="\n"
		b = bytes(message, 'utf-8')
		c.send(b)
		
		 






from _thread import *
import threading
from socket import *
serverName = '10.64.10.243 '
serverPort = 11115
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
start_new_thread(sendmsg, (clientSocket,))
while True:	
		
	Sentence = clientSocket.recv(1024)
	if not Sentence:
		break
	print ( str(Sentence.decode('ascii')))
clientSocket.close()	





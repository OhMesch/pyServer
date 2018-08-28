import socket

HOST = "73.218.10.56"
PORT = 80

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST, PORT))

while True:
	command = input(">")
	clientsocket.send(command.encode("utf-8"))
	response = clientsocket.recv(1024)
	sresponse = response.decode("utf-8")
	print(sresponse)
	if command == "quit" or command == "exit": break
	print("")
import socket

PORT = 80
MAX_CONNECTIONS = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', PORT))
serversocket.listen(MAX_CONNECTIONS)

connection, address = serversocket.accept()
print("Connected to:", address[0] + ":" + str(address[1]))
while True:
    buf = connection.recv(1024)
    command = buf.decode("utf-8")
    print("Recieved: ", command)
    if command == "quit" or command == "exit":
    	connection.close()
    	break
    else:
    	connection.send(("Server Recieved: " + command).encode("utf-8"))

print("Connection Terminated")
import socket

PORT = 8080
MAX_CONNECTIONS = 4

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', PORT))
print("Binded to " + socket.gethostname() + " Port " + str(PORT))
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

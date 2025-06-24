import socket
print(" Starting a new client : Client 2")

HOST = "localhost"
PORT = 3000
# Create a client socket
client_socket = socket.socket()
client_socket.connect((HOST, PORT)) # clint needs to connect to the server socket
client_socket.sendall(b" Hello from client 2")

response_from_server = client_socket.recv(2048)
print(response_from_server)


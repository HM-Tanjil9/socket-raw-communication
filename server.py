import socket
import threading

def connect_a_client(conn, addr):
    print("New client has been connected")
    data = conn.recv(2048)
    print("Data received from client is:", data)
    conn.sendall(b"Server has received your data thanks")

HOST = "localhost"
PORT = 3000

# create a new server socket object
server_socket = socket.socket()

# bind host & port to the server socket object
server_socket.bind((HOST, PORT))

# listening for new connection
server_socket.listen()
print("Server is listening on", HOST, PORT)

while True: # wait for new connection acceptance (keep alive)
    conn, addr = server_socket.accept() # it is accepting a new connection
    t = threading.Thread(target=connect_a_client, args=(conn, addr)) # Preparing a new thread
    t.start() # it starts the thread
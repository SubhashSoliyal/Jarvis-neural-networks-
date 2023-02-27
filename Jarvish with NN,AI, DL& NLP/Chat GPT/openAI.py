import socket


# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local IP address and port
server_socket.bind(("127.0.0.1", 8000))

# Listen for incoming connections
server_socket.listen()

# Accept a connection
client_socket, client_address = server_socket.accept()

# Receive messages from the client
while True:
    message = client_socket.recv(1024)
    if not message:
        break
    print(f"Received message: {message.decode('utf-8')}")

# Close the sockets
client_socket.close()
server_socket.close()

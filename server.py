# Simple LAN Chat Server using TCP Sockets
# -------------------- CN Concepts -----------------------
# 1. Application Layer protocol using TCP socket
# 2. Server binds to IP + port (Layer 3 + 4)
# 3. Uses threads for full-duplex (bi-directional) comm
# --------------------------------------------------------

import socket
import threading

# Store all connected clients
clients = []

# Handle a client connection
def handle_client(client_socket):
    while True:
        try:
            # Receive message from one client
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Send message to all clients except sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

# ------------------- Server Setup -----------------------

# Create a TCP socket (SOCK_STREAM = TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all available network interfaces (for LAN use)
server.bind(("00.000.00.00", 8000))  # YOUR IP

# Listen for connections
server.listen()

print("[SERVER STARTED] Listening on port 8000...")

# Accept clients forever
while True:
    client_socket, client_address = server.accept()
    print(f"[CONNECTED] {client_address}")
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()

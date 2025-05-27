import socket
import sys
import os
import platform

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

def receive_messages(sock):
    while True:
        try:
            username_header = sock.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = sock.recv(username_length).decode('utf-8')

            message_header = sock.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = sock.recv(message_length).decode('utf-8')

            print(f"\n{username} > {message}")
        except Exception as e:
            print("Error receiving message:", str(e))
            sys.exit()

my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

if os.name == "nt" or platform.system() == "Windows":
    # Windows: usar hilos
    import threading
    client_socket.setblocking(True)
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    while True:
        message = input(f"{my_username} > ")
        if message:
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)
else:
    # Unix: usar select
    import select
    while True:
        sockets_list = [sys.stdin, client_socket]
        read_sockets, _, _ = select.select(sockets_list, [], [])
        for notified_socket in read_sockets:
            if notified_socket == sys.stdin:
                message = input(f"{my_username} > ")
                if message:
                    message = message.encode('utf-8')
                    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                    client_socket.send(message_header + message)
            else:
                receive_messages(client_socket)
import socket
import select
import threading

HEADER_LENGTH = 10

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No necesita ser accesible, solo para obtener la IP local
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

IP = get_local_ip()
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print(f"Servidor escuchando en {IP}:{PORT}")

sockets_list = [server_socket]

clients = {}

# Guardar las direcciones de los clientes
client_addresses = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False 

def command_listener():
    while True:
        cmd = input()
        if cmd.strip() == "showPublic":
            print("Clientes conectados (IP pública):")
            for sock, addr in client_addresses.items():
                user = clients.get(sock)
                username = user['data'].decode('utf-8') if user else "Desconocido"
                print(f"{username}: {addr[0]}:{addr[1]}")
        else:
            print("Comando no reconocido.")

# Iniciar el hilo para escuchar comandos
threading.Thread(target=command_listener, daemon=True).start()

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            client_addresses[client_socket] = client_address  # Guardar dirección

            print(f"Accepted connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                del client_addresses[notified_socket]  # Eliminar dirección
                continue

            user = clients[notified_socket]
            print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        del client_addresses[notified_socket]
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    # El valor dentro de recv es el tamaño del buffer de datos
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
    
print(full_msg)
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    message = b'hola'
    addr = ("127.0.0.1", 3001)
    print("message sended: ", message)
    s.sendto(message, addr)

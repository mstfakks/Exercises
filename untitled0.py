import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1028))
server.listen()

untitled1_socket, untitled1_address = server.accept()

file = open('newkırmızı alan.jpeg', 'wb')
image_chunk = untitled1_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = untitled1_socket.recv(2048)

file.close()
untitled1_socket.close()

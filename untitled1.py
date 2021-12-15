import socket

untitled1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
untitled1.connect(('localhost',1028))

file = open('kırmızı alan.jpeg', 'rb')

image_data = file.read(2048)

while image_data:
    untitled1.send(image_data)
    image_data = file.read(2048)
    

file.close()
untitled1.close()
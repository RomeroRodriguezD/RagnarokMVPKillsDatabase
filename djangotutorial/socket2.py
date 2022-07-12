import socket


host = "127.0.0.1"
port = 5000

mysock = socket.socket()
mysock.connect(('serebii.net', 80))
cmd = 'GET https://www.serebii.net HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) <1:
        break
    print(data.decode(), end='')

mysock.close()
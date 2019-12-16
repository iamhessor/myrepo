import socket

sock = socket.socket()
sock.connect(('localhost', 10000))
sock.close()


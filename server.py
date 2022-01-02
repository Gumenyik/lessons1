import socket

HOST = '127.0.0.1'
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
sock.close

# Клиент сообщений, действующий по протоколу UDP
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello World', ('localhost',10000))
resp, addr = s.recvfrom(256)
print(resp)
s.sendto(b'Spam', ('localhost',10000))
resp, addr = s.recvfrom(256)
print(resp)
s.close()
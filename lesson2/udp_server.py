# Сервер сообщений, действующий по протоколу UDP
# Принимает небольшие пакеты и отправляет их обратно
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost',10000))
while True:
    data, address = s.recvfrom(256)
    print('Получены данные с адреса %s' % str(address))
    s.sendto(b'echo:' + data, address)
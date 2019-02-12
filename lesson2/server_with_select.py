import select
from socket import socket, AF_INET, SOCK_STREAM
def read_requests(clients):
    ''' Чтение запросов из списка клиентов '''
    requests = {} # Словарь ответов сервера вида {сокет:запрос}

    for sock in clients:
        try:
            data = sock.recv(1024).decode('ascii')
            requests[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(),
        
            sock.getpeername()))
        
            clients.remove(sock)
    return requests

def write_responses(requests, clients):
    ''' Эхо-ответ сервера клиентам, от которых были
    запросы '''
    for sock in clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode('ascii')
                test_len = sock.send(resp.upper())
            except: # Сокет недоступен, клиент отключился
                print('Клиент {} отключился'.format(sock.getpeername()))
                sock.close()
                clients.remove(sock)

def mainloop():
    ''' Основной цикл обработки запросов клиентов '''
    address = ('', 10000)
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2) # Таймаут для операций с сокетом
    while True:
        try:
            conn, addr = s.accept() # Проверка подключений
        except OSError as e:
            pass # timeout вышел
        else:
            print("Получен запрос на соединение с %s" % str(addr))

            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass # Ничего не делать, если какой-то

    requests = read_requests(r)

    write_responses(requests, w)

print('Эхо-сервер запущен!')
mainloop()
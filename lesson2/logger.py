import logging
logging.basicConfig(
    filename = "app.log",
    format = "%(levelname)-10s %(asctime)s %(message)s",
    level = logging.INFO
)
log = logging.getLogger("app")
# Записать сообщение, используя позиционные аргументы форматирования
host = 'localhost'
port = 7777
log.critical("Can't connect to %s at port %d", host, port)
# Записать сообщение, используя словарь значений
parms = { 'host' : 'www.python.org',
'port' : 80
}
log.critical("Can't connect to %(host)s at port %(port)d", parms)
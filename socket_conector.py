from xmlrpc.client import ServerProxy
from _thread import *
import json, socket


def on_new_client(clientsocket, addr):
    while True:
        opcion = clientsocket.recv(1024)
        if opcion == b'1':
            server.send(s.listTile)  # traer noticias
        if opcion == b'2':
            print('en desarrollo')  # eliminar
        if opcion == b'3':
            print('en desarrollo')  # editar


server = socket.socket()
print('Server started!')
print('Waiting for clients...')
server.bind(('localhost', 1100))  # -----------------------------------------------------------------server
s = ServerProxy('http://localhost:8000', allow_none=True)
server.listen(100)
threadID = 1
while True:
    c, addr = server.accept()
    addr = c.getpeername()
    print('Got connection from', addr)
    start_new_thread(on_new_client, (c, addr))
    print("thread#= ", threadID)
    threadID += 1

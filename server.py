#!/usr/bin/python3
from socket import *
import hashlib
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 10123))
password = ''
serverSock.listen(1)
while True:
    clientSock, addr = serverSock.accept()
    print(str(addr), 'connected')
    data = clientSock.recv(1024)
    if password == data.decode('utf-8'):
        clientSock.send('I am a server'.encode('utf-8'))
    password = data.decode('utf-8')
    clientSock.close()
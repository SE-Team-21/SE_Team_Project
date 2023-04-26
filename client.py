from socket import *
import encryption as E
from datetime import datetime

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('13.210.238.200', 10123))

print('연결 확인 됐습니다.')
while True:
    clientSock.send(E.Encrypt_S(input("Enter Password : ")))
    print(datetime.now())
    data = clientSock.recv(1024).decode('utf-8')
    print(datetime.now())
    print('받은 데이터 : ', data)
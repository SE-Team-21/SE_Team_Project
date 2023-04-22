from socket import *
import encryption as E
from datetime import datetime

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('comunix.seoultech.ac.kr', 10123))

print('연결 확인 됐습니다.')
while True:
    clientSock.send(E.Encrypt(input("Enter : ")).encode('utf-8'))
    print(datetime.now())

    data = clientSock.recv(1024)
    print('받은 데이터 : ', data.decode('utf-8'))
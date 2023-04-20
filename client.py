from socket import *
import encryption as E

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('comunix.seoultech.ac.kr', 10123))

print('연결 확인 됐습니다.')
clientSock.send(E.Encrypt('I am a client').encode('utf-8'))
print('메시지를 전송했습니다.')

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))
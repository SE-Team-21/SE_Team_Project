#!/usr/bin/python3
from socket import *
from datetime import datetime
import select
import encryption as E

def Check(input, output): # 패스워드 확인
        return input == output

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 10123))
password = None
serverSock.listen(3)
players = []
num = 0
while True:
    readable, _, _ = select.select([serverSock], [], [], 0)
    for sock in readable:
        if sock is serverSock:
            connection, address = serverSock.accept()
            players.append(connection)
            num += 1

    for player in players:
        readable, _, _ = select.select([player], [], [], 0)
        try:
            for sock in readable:
                data = E.Decrypt_A(sock.recv(1024))
                if data["Type"] == "pw":
                    if Check(data["Password"], password):
                        player.send(str(datetime.now()).encode('utf-8'))
                    else:
                        player.send('Password initialize or incorrect'.encode('utf-8'))
                    if password == None:
                        password = data["Password"]
        except:
            players.remove(player)
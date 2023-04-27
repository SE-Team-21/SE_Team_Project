#!/usr/bin/python3
from socket import *
from datetime import datetime
import select
import encryption as E

def Check(input, output): # 패스워드 확인
        return input == output

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 10123))
serverSock.listen(3)
players = []
rooms = []
num = 0

class Room:
    def __init__(self, pw, add, top):
        self.password = pw
        self.address = add
        self.players = []
        self.players.append(top)


while True:
    readable, _, _ = select.select([serverSock], [], [], 0)
    for sock in readable:
        if sock is serverSock:
            #connection, address = serverSock.accept()
            players.append(serverSock.accept())
            num += 1

    for player in players:
        readable, _, _ = select.select([player[0]], [], [], 0)
        try:
            for sock in readable:
                data = E.Decrypt_A(sock.recv(1024))
                if data["Type"] == "mkr":
                    rooms.append(Room(data["Password"], player[1][0], player))
                    player[0].send(E.Encrypt_A({"Type": "ip", "address": player[1][0]}))
                elif data["Type"] == "pw":
                    if Check(data["Password"], rooms[0].password):
                        player[0].send(str(datetime.now()).encode('utf-8'))
                    else:
                        player[0].send('Password initialize or incorrect'.encode('utf-8'))
                elif data["Type"] == "grs":
                    player[0].send(player[1][0].encode('utf-8'))
                    data = {"Type": "rs", "Num": len(rooms)}
                    for idx, room in enumerate(rooms):
                        data[idx] = [room.address, len(room.players)]
                    player[0].send(E.Encrypt_A(data))
                    pass
        except:
            players.remove(player)
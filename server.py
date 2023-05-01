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
    def __init__(self, pw, add, port, top):
        self.password = pw
        self.address = add
        self.port = port
        self.players = []
        self.players.append(top)
        self.num_of_com = 0


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
                    rooms.append(Room(data["Password"], player[1][0], player[1][1], player))
                    player[0].send(E.Encrypt_A({"Type": "ip", "address": player[1][0]}))
                elif data["Type"] == "pw":
                    for room in rooms:
                        if room.address == data["Host_IP"] and room.port == data["Host_PORT"]:
                            if Check(data["Password"], room.password):
                                if room.num_of_com + len(room.players) <= 6:
                                    room.players.append(player)
                                    player[0].send(E.Encrypt_A({"Type": "Correct"}))
                                else: # 방에 자리가 없을 때
                                    pass
                            else: # 비밀번호가 틀렸을 때
                                player[0].send(E.Encrypt_A({"Type": "Incorrect"}))
                        else: # 방을 찾지 못했을 때
                            pass
                elif data["Type"] == "grs":
                    player[0].send(player[1][0].encode('utf-8'))
                    data = {"Type": "rs", "Num": len(rooms)}
                    for idx, room in enumerate(rooms):
                        data[idx] = [room.address, len(room.players), room.port]
                    player[0].send(E.Encrypt_A(data))
                elif data["Type"] == "gma":
                    player[0].send(E.Encrypt_A({"Type": "myip", "address": player[1][0]}))
                elif data["Type"] == "exit":
                    for room in rooms:
                        if player in room.players:
                            room.players.remove(player)
                            if len(room.players) == 0:
                                rooms.remove(room)
                            else: # 다른 사람에게 방장 넘겨줌
                                pass
                            break

        except:
            players.remove(player)
            for room in rooms:
                if player in room.players:
                    room.players.remove(player)
                    if len(room.players) == 0:
                                rooms.remove(room)
                    else: # 다른 사람에게 방장 넘겨줌
                        pass
                    break
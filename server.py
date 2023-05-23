#!/usr/bin/python3
from socket import *
from datetime import datetime
import select
import encryption as E
from uno.game.Game import UnoGame

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
        self.game = None
        self.players = [top, None, None, None, None, None]
        self.num_of_com = 0

    def broadcast_update(self):
        data = {"Type": "update"}
        if self.game == None:
            for idx, p in enumerate(self.players):
                if p is None:
                    data[idx] = None
                elif p.is_computer:
                    data[idx] = ["Computer"+str(idx)]
                else:
                    data[idx] = [p.name]
            print(data)
        else:
            for idx, p in enumerate(self.players):
                if p is None or p.is_computer: # 빈자리거나 컴퓨터일 때
                    pass
                else:
                    data[idx] = [p.name, len(p.hand)]
        for p in self.players:
            if p is None or p.is_computer: # 빈자리거나 컴퓨터일 때
                pass
            else:
                p = p.sock
                p[0].send(E.Encrypt_A(data))


class Player:
    def __init__(self, sock, name, is_computer = False):
        self.sock = sock
        self.name = name
        self.is_computer = is_computer
        self.room = None
while True:
    readable, _, _ = select.select([serverSock], [], [], 0)
    for sock in readable:
        if sock is serverSock:
            #connection, address = serverSock.accept()
            players.append(serverSock.accept())
            num += 1

    for idx, player in enumerate(players):
        readable, _, _ = select.select([player[0]], [], [], 0)
        try:
            for sock in readable:
                data = E.Decrypt_A(sock.recv(1024))
                pid = player[0].fileno()
                print(data["Type"])
                room = None
                if data["Type"] == "game_start":
                    for r in rooms:
                        if r.address == player[1][0] and r.port == player[1][1]:
                            room = r
                    room.game = UnoGame(len(room.players)) # + 콤퓨타)
                    g = room.game
                    for idx, p in enumerate(room.players):
                        p = p.sock
                        if p is None or p.is_computer: # 빈자리거나 컴퓨터일 때
                            pass
                        else:
                            print(p[0])
                            data = {"Type": "game_start", "Num": len(g.players[idx].hand)}
                            for i, card in enumerate(g.players[idx].hand):
                                data[i] = [card.color, card.card_type]
                            data["top"] = [str(g.current_card.color), str(g.current_card.card_type)]
                            p[0].send(E.Encrypt_A(data))
                            print("s")
                            #p[0].send(E.Encrypt_A({"Type": "game_start", "current_player": g.current_player.player_id, "deck": str(g.players[idx].hand).replace('[', '',).replace(']', '',).replace('<UnoCard object: ', '', 999).replace('>', '').split(', '), "top": str(g.current_card)}))
                elif data["Type"] == "action":
                    for room in rooms:
                        if player in room.players:
                            pass
                elif data["Type"] == "add_computer":
                    for room in rooms:
                        if player in room.players:
                            print("exist")
                            room.players[data["Index"]] = Player(1, 1, True)
                            room.broadcast_update()
                elif data["Type"] == "mkr":
                    temp = Room(data["Password"], player[1][0], player[1][1], Player(player, data["Name"]))
                    temp.players[0].room = temp
                    rooms.append(temp)
                    player[0].send(E.Encrypt_A({"Type": "ip", "address": player[1][0]}))
                elif data["Type"] == "pw":
                    for room in rooms:
                        if room.address == data["Host_IP"] and room.port == data["Host_PORT"]:
                            if Check(data["Password"], room.password):
                                if room.num_of_com + len(room.players) <= 6:
                                    print(room.players)
                                    temp = Player(player, data["Name"])
                                    temp.room = room
                                    for idx, i in enumerate(room.players):
                                        if i is None:
                                            room.players[idx] = temp
                                            print(1)
                                            break
                                    player[0].send(E.Encrypt_A({"Type": "Correct"}))
                                    room.broadcast_update()

                                else: # 방에 자리가 없을 때
                                    pass
                            else: # 비밀번호가 틀렸을 때
                                player[0].send(E.Encrypt_A({"Type": "Incorrect"}))
                        else: # 방을 찾지 못했을 때
                            pass
                elif data["Type"] == "grs":
                    #player[0].send(player[1][0].encode('utf-8'))
                    data = {"Type": "rs", "Num": len(rooms)}
                    for idx, room in enumerate(rooms):
                        data[idx] = [room.address, len(room.players), room.port]
                    player[0].send(E.Encrypt_A(data))
                elif data["Type"] == "gma":
                    player[0].send(E.Encrypt_A({"Type": "myip", "address": player[1][0]}))
                elif data["Type"] == "update":
                    for room in rooms:
                        for p in room.players:
                            if p.sock[1][0] == player[1][0] and p.sock[1][1] == player[1][1]:
                                room.broadcast_update()
                elif data["Type"] == "exit":
                    for room in rooms:
                        for p in room.players:
                            if p.is_computer:
                                pass
                            else:
                                if p.sock[1][0] == player[1][0] and p.sock[1][1] == player[1][1]:
                                    room.players.remove(p)
                                if len(room.players) == 0:
                                    rooms.remove(room)
                                else: # 다른 사람에게 방장 넘겨줌
                                    pass
                                break



        except:
            pass
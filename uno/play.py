from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.game.Game import UnoGame
import random

class Playing(Display):
    game = None
    game_mode = 0
    def __init__(self):
        super().__init__()
        self.Card_list = []
        self.x = 0
        self.y = 0
        self.stage = 0
        self.num_of_players = 1
        self.is_game_start = False
        self.is_computer_activated = [False, False, False, False, False]
        self.Player_list = []
        self.Player_list.append(Button((600, 100), (80, 80), 'Computer1 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 200), (80, 80), 'Computer2 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 300), (80, 80), 'Computer3 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 400), (80, 80), 'Computer4 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 500), (80, 80), 'Computer5 ', lambda x, y: self.computer_add_remove(x, y)))
        self.start_button = Button((100, 100), (60, 60), 'Game Start', lambda: self.game_start())

        self.choice_card_idx = None

    def computer_add_remove(self, idx, item):
        if self.is_computer_activated[idx]:
            self.is_computer_activated[idx] = False
            self.num_of_players -= 1
        else:
            self.is_computer_activated[idx] = True
            self.num_of_players += 1

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        for item in self.Card_list:
            item.update(mouse_pos)
        for item in self.Player_list:
            item.update(mouse_pos)
        self.start_button.update(mouse_pos)
        
    def next_screen(self):
        pass
    
    def game_start(self):
        self.is_game_start = True

    def player_action(self, running):
        player = self.game.current_player
        player_id = player.player_id
        if player.can_play(self.game.current_card):
            
            # if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
            if self.choice_card_idx is not None:
                card = Playing.game.players[0].hand[self.choice_card_idx]
                if self.game.current_card.playable(card):
                    if card.color == 'black':
                        new_color = random.choice(C.COLORS)
                    else:
                        new_color = None
                    print("Player {} played {}".format(player, card))
                    self.game.play(player=player_id, card=self.choice_card_idx, new_color=new_color)
                    
                self.choice_card_idx = None
        
        else:
            print("Player {} picked up".format(player))
            self.game.play(player=player_id, card=None)
            pg.time.wait(200)

    def game_handler(self, running):
        if Playing.game == None:
            Playing.game = UnoGame(self.num_of_players)
        self.top = C.ALL_CARDS[str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type)]
        for i in Playing.game.players[0].hand:
            myCard = C.ALL_CARDS[str(i.color) + str(i.card_type)]
            self.Card_list.append(myCard)
            '''
                if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
                    self.Card_list.append(myCard)
                    self.screen.blit(myCard.img, (self.x, self.y))
                self.x += 50
            '''
            myCard.draw(self.screen, self.x, self.y)
            self.x += 50
            self.screen.blit(self.top.img, (150,100))
            self.backCard = C.ALL_CARDS["Back"]
            self.screen.blit(self.backCard.img, (100, 100))

            player = self.game.current_player
            player_id = player.player_id
            if player_id == 0:
                self.player_action(running)
            else:
                if player.can_play(self.game.current_card):
                    for i, card in enumerate(player.hand):
                        if self.game.current_card.playable(card):
                            if card.color == 'black':
                                new_color = random.choice(C.COLORS)
                            else:
                                new_color = None
                            print("Computer {} played {}".format(player, card))
                            self.game.play(player=player_id, card=i, new_color=new_color)
                            break
                else:
                    print("Computer {} picked up".format(player))
                    self.game.play(player=player_id, card=None)
                    pg.time.wait(200)

    def single_mode(self, running):
        self.screen.fill((255, 255, 255))
        self.Card_list = []
        self.x = 0
        self.y = 300

        if self.is_game_start:
            self.game_handler(running)
        else:
            self.start_button.draw(self.screen)

        for idx, item in enumerate(self.Player_list):
            if self.is_computer_activated[idx]:
                item.change_text(item.button_text.replace(" ", "_activated"))
                item.draw(self.screen)
            else:
                item.change_text(item.button_text.replace("_activated", " "))
                item.draw(self.screen)
        '''
        self.x_ = 0
        self.y_ = 0
        for player in Playing.game.players:
            self.screen.blit(self.backCard.img, (self.x_, self.y_))
            self.y_ = self.y_ + 100
        '''
            
        self.update_screen(pg.mouse.get_pos())
        pg.display.update()
        for event in pg.event.get():
            self.tmp_event = event
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.mode[C.NEXT_SCREEN] = C.STOP
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.tmp_event.type == pg.QUIT:
                    running[0] = False
                    return
                elif self.tmp_event.type == pg.KEYUP:
                    if self.tmp_event.key == pg.K_ESCAPE:
                        self.mode[C.NEXT_SCREEN] = C.STOP
                elif self.tmp_event.type == pg.MOUSEBUTTONDOWN:
                    if Playing.game:
                        for idx, item in enumerate(self.Card_list):
                            if item.above:
                                print(idx)
                                self.choice_card_idx = idx
                                break
                for idx, item in enumerate(self.Player_list):
                    if item.above and not self.is_game_start:
                        item.click((idx, item))
                if self.start_button.above and not self.is_game_start:
                    self.start_button.click()

    def story_mode(self, stage, running):
        pass

    def main_loop(self, running):
        # # game inst
        if Playing.game_mode == 0:
            self.single_mode(running)
        elif Playing.game_mode == 1:
            self.story_mode(self.stage, running)
from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.game.Game import UnoGame
from uno.Text_Class import Text
import random
from uno.CardButton_Class import CardButton

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
        self.Player_list.append(Button((710, 60), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 178), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 296), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 414), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 532), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Text_list.append(Text((690, 60), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 178), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 296), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 414), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 532), 20, '', C.BLACK))
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
        for idx, item in enumerate(self.Player_list):
            if self.is_computer_activated[idx]:
                item.INACTIVE_COLOR = C.GRAY
                item.locate = True
                item.change_text('Computer'+str(idx+1))
            else:
                item.INACTIVE_COLOR = C.WHITE
                item.locate = False
                item.change_text('empty')
            item.update(mouse_pos)
            item.draw(self.screen)
            item.change_size(Display.display_idx)
        for item in self.Card_list:
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
        self.top = CardButton(str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type), C.ALL_CARDS[str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type)])
        for i in Playing.game.players[0].hand:
            myCard = CardButton(str(i.color) + str(i.card_type), C.ALL_CARDS[str(i.color) + str(i.card_type)])
            self.Card_list.append(myCard)
            '''
                if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
                    self.Card_list.append(myCard)
                    self.screen.blit(myCard.img, (self.x, self.y))
                self.x += 50
            '''
            myCard.draw(self.screen, self.x, self.y)
            self.x += 50
            if self.x >= 500:
                self.x = 0
                self.y += 100
            self.top.draw(self.screen, 150, 100)
            self.backCard = CardButton("Back", C.ALL_CARDS["Back"])
            self.backCard.draw(self.screen, 100, 100)

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
        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
        self.Card_list = []
        self.x = 0
        self.y = 300

        if self.is_game_start:
            self.game_handler(running)
        else:
            self.start_button.draw(self.screen)

        self.update_screen(pg.mouse.get_pos())
        
        if self.is_game_start:
            x_ = 640
            y_ = 40
            index = 0
            for idx in range(5):
                if self.is_computer_activated[idx]:
                    self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (30,60)), (x_, y_))
                    self.Text_list[idx].change_text('+' + str(len(Playing.game.players[index].hand)-1))
                    self.Text_list[idx].draw(self.screen)
                    index += 1
                y_ += 118
            
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

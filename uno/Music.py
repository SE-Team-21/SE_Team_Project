import pygame as pg

class Background_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.background_music = music_list[idx]
        
    def play(self):
        pg.mixer.music.load(self.background_music)
        pg.mixer.music.play(-1)
        
    def stop(self):
        pg.mixer.music.stop()


music_list = ["assets/sounds/bg.wav", "assets/sounds/bg_music.wav", "assets/sounds/card_drawn.wav", "assets/sounds/card_played.wav", 
              "assets/sounds/Minecraft-hat.wav", "assets/sounds/Recording.wav", "assets/sounds/shuffle.wav", "assets/sounds/victory.wav"]
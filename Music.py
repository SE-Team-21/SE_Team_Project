import pygame as pg
from uno.KeySettings import Data

music_list = ["assets/sounds/bg.wav", "assets/sounds/bg_music.wav", "assets/sounds/card_drawn.wav", "assets/sounds/card_played.wav", 
              "assets/sounds/Minecraft-hat.wav", "assets/sounds/Recording.wav", "assets/sounds/shuffle.wav", "assets/sounds/victory.wav"]

class Background_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.music = pg.mixer.Sound(music_list[idx])
        self.channel = pg.mixer.Channel(0)
        self.v_size = Data.data.Master_Volume * Data.data.Music_Volume
        
    def play(self):
        self.channel.play(self.music, loops=-1)

    def volume(self, v):
        self.v_size = v
        self.channel.set_volume(v)
    
    def stop(self):
        self.channel.stop()
    

        
class Effect_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.effect_music = pg.mixer.Sound(music_list[idx])
        self.channel = pg.mixer.Channel(1)
        self.v_size = Data.data.Master_Volume * Data.data.Effect_Volume
        
    def play(self):
        self.channel.play(self.effect_music, loops=1)

    def volume(self,v):
        self.v_size = v
        self.channel.set_volume(v)
        
    def stop(self):
        self.channel.stop()

bg_music = Background_Music(0)
ef_music = Effect_Music(4)

bg_music.play()

def master_volume(v_size):
    bg_music.volume(v_size)
    ef_music.volume(v_size)
    
def bg_volume(v_size):
    bg_music.volume(v_size)
    
def ef_volume(v_size):
    ef_music.volume(v_size)


import pygame as pg
from uno.KeySettings import Data

class Background_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.music = music_list[idx]
        self.channel = pg.mixer.Channel(0)
        self.volume = Data.data.Music_Volume
        
    def play(self):
        pg.mixer.music.load(self.music)
        pg.mixer.music.play(-1)
        
    def volume(self, v):
        self.volume = v
        self.channel.set_volume(self.volume * Data.data.Music_Volume)
    
    def stop(self):
        pg.mixer.music.stop()
        
class Effect_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.effect_music = music_list[idx]
        self.channel = pg.mixer.Channel(1)
        self.volume = Data.data.Effect_Volume
        
    def play(self):
        effect = pg.mixer.Sound(self.effect_music)
        effect.play(1)
        
    def volume(self,v):
        self.volume = v
        self.channel.set_volume(self.volume * Data.data.Effect_Volume)
        
    
    def stop(self):
        effect = pg.mixer.Sound(self.effect_music)
        effect.stop()
        
def master_volume(v_value):
    Background_Music.volume(v_value)
    Effect_Music.volume(v_value)
    
def bg_volume(v_value):
    Background_Music.volume(v_value)
    
def ef_volume(v_value):
    Effect_Music.volume(v_value)


music_list = ["assets/sounds/bg.wav", "assets/sounds/bg_music.wav", "assets/sounds/card_drawn.wav", "assets/sounds/card_played.wav", 
              "assets/sounds/Minecraft-hat.wav", "assets/sounds/Recording.wav", "assets/sounds/shuffle.wav", "assets/sounds/victory.wav"]
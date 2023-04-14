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
        self._volume = 0.5
        
    def play(self):
        #pg.mixer.music.load(self.music)
        #pg.mixer.music.play(-1)
        self.channel.play(self.music)

    def volume(self, v):
        self._volume = v
        self.channel.set_volume(v)
        print(self.channel.get_volume())
    
    def stop(self):
        pg.mixer.music.stop()
        
class Effect_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.effect_music = pg.mixer.Sound(music_list[idx])
        self.channel = pg.mixer.Channel(1)
        self._volume = 0.5
        
    def play(self):
        #effect = pg.mixer.Sound(self.effect_music)
        #effect.play(1)
        self.channel.play(self.effect_music)

    def volume(self,v):
        self._volume = v
        self.channel.set_volume(v)
        
    
    def stop(self):
        effect = pg.mixer.Sound(self.effect_music)
        effect.stop()

bg_music = Background_Music(0)
ef_music = Effect_Music(4)

bg_music.play()
ef_music.play()

def master_volume(v_value):
    bg_music.volume(v_value)
    ef_music.volume(v_value)
    
def bg_volume(v_value):
    bg_music.volume(v_value)
    
def ef_volume(v_value):
    ef_music.volume(v_value)


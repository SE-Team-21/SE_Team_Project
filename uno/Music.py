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
        
    def play(self):
        self.channel.set_volume(Data.data.Master_Volume * Data.data.Music_Volume)
        self.channel.play(self.music, loops=-1)

    def volume(self, mst, back):
        self.channel.set_volume(mst * back)
        #print("bg : ", self.channel.get_volume())
    
    def stop(self):
        pg.mixer.music.stop()
        
class Effect_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.effect_music = pg.mixer.Sound(music_list[idx])
        self.channel = pg.mixer.Channel(1)        
        
    def play(self):
        self.channel.set_volume(Data.data.Master_Volume * Data.data.Effect_Volume)
        self.channel.play(self.effect_music, loops=0)

    def volume(self, mst, ef):
        self.channel.set_volume(mst * ef)
        #print("ef : ",  self.channel.get_volume())
        
    
    def stop(self):
        effect = pg.mixer.Sound(self.effect_music)
        effect.stop()

Data.load_settings()

bg_music_main = Background_Music(0)
bg_music_play = Background_Music(1)
ef_music_draw = Effect_Music(2)
ef_music_set = Effect_Music(3)


def master_volume(v_value):
    bg_music_main.volume(v_value, Data.data.Music_Volume)
    bg_music_play.volume(v_value, Data.data.Music_Volume)
    ef_music_draw.volume(v_value, Data.data.Effect_Volume)
    ef_music_set.volume(v_value, Data.data.Effect_Volume)
    Data.save_sound(0, v_value)
    
def bg_volume(v_value):
    bg_music_main.volume(v_value, Data.data.Music_Volume)
    bg_music_play.volume(v_value, Data.data.Music_Volume)
    Data.save_sound(1, v_value)
    
def ef_volume(v_value):
    ef_music_draw.volume(v_value, Data.data.Effect_Volume)
    ef_music_set.volume(v_value, Data.data.Effect_Volume)
    Data.save_sound(2, v_value)


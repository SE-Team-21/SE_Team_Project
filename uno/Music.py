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
        if Data.data.Music_Volume != 0.5:
            self._volume = Data.data.Music_Volume
        
    def play(self):
        #pg.mixer.music.load(self.music)
        #pg.mixer.music.play(-1)
        self.volume(Data.data.Music_Volume)
        self.channel.set_volume(self._volume)
        self.channel.play(self.music)

    def volume(self, v):
        self._volume = Data.data.Master_Volume * v
        self.channel.set_volume(self._volume)
        print("bg : ", self.channel.get_volume())
        Data.save_sound(1, self._volume)
    
    def stop(self):
        pg.mixer.music.stop()
        
class Effect_Music:
    def __init__(self, idx):
        pg.init()
        pg.mixer.init()
        self.effect_music = pg.mixer.Sound(music_list[idx])
        self.channel = pg.mixer.Channel(1)        
        if Data.data.Effect_Volume != 0.5:
            self._volume = Data.data.Effect_Volume
        
    def play(self):
        #effect = pg.mixer.Sound(self.effect_music)
        #effect.play(1)
        self.volume(Data.data.Effect_Volume)
        self.channel.set_volume(self._volume)
        self.channel.play(self.effect_music)

    def volume(self,v):
        self._volume = Data.data.Master_Volume * v
        self.channel.set_volume(self._volume)
        print("ef : ",  self.channel.get_volume())
        Data.save_sound(2, self._volume)
        
    
    def stop(self):
        effect = pg.mixer.Sound(self.effect_music)
        effect.stop()

Data.load_settings()
bg_music = Background_Music(0)
ef_music = Effect_Music(4)

bg_music.play()
ef_music.play()

def master_volume(v_value):
    Data.save_sound(0, v_value)
    bg_music.volume(Data.data.Music_Volume)
    ef_music.volume(Data.data.Effect_Volume)
    
def bg_volume(v_value):
    bg_music.volume(v_value)
    
def ef_volume(v_value):
    ef_music.volume(v_value)


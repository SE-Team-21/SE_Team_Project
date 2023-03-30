import pygame as pg

class Background_Music:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.background_music = "assets/sounds/bg_music.wav"
        
    def main_music(self):
        pg.mixer.music.load(self.background_music)
        pg.mixer.music.play(-1)
        
    def stop_music(self):
        pg.mixer.music.stop()
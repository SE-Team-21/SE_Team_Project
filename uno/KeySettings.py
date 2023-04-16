import pygame as pg
import dill

class Data:
    data = None
    def __init__(self):
        self.KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_ESCAPE, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5]
        self.Resolution = 0
        self.Story = 0
        self.Color = -1
        self.name = 'You'
        self.load_settings()
        #self.Master_Volume = 0.5
        #self.Music_Volume = 0.5
        #self.Effect_Volume = 0.5

    @staticmethod
    def save():
        with open('data.pkl', 'wb') as f:
            dill.dump(Data.data, f)
    
    @staticmethod
    def save_key(idx, key):
        Data.data.KEY_Settings[idx] = key
        Data.save()

    @staticmethod
    def save_resolution(idx):
        Data.data.Resolution = idx
        Data.save()

    @staticmethod
    def save_color(idx):
        Data.data.Color = idx
        Data.save()

    @staticmethod
    def save_sound(idx, sz):
        if idx == 0:
            Data.data.Master_Volume = sz
        elif idx == 1:
            Data.data.Music_Volume = sz
        else:
            Data.data.Effect_Volume = sz
        Data.save()
    
    @staticmethod
    def save_story(idx):
        Data.data.Story = idx
        Data.save()

    @staticmethod
    def save_name(name):
        Data.data.name = name
        Data.save()

    @staticmethod
    def default():
        Data.data.KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_ESCAPE, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5]
        Data.data.Resolution = 0
        Data.data.Color = -1
        Data.data.Master_Volume = 0.5
        Data.data.Music_Volume = 0.5
        Data.data.Effect_Volume = 0.5
        Data.save()


    @staticmethod
    def load_settings():
        try: # data 파일이 있을 때 로드한다 (rb)
            with open("data.pkl","rb") as fr:
                Data.data = dill.load(fr)
            if(Data.data == None):
                Data.data = Data()
                Data.save()
                
        except: # data 파일이 없다면 기본값을 초기화 하고 만든다 (wb)
            Data.data = Data()
            Data.save()

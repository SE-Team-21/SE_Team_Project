import pygame as pg
import dill

class Data:
    KEY_Settings = []
    Display = 0
    story = 0
    Colorblind_Mode = 0
    Master_Volume = 1
    Music_Volume = 1
    Effect_Volume = 1
    @staticmethod
    def save_settings(idx, key):
        Data.KEY_Settings[idx] = key
        with open('data.pkl', 'wb') as f:
            dill.dump(Data, f)
        with open("data.pkl","rb") as fr:
            Data.KEY_Settings = dill.load(fr).KEY_Settings

    @staticmethod
    def load_settings():
        try: # data 파일이 있을 때 로드한다 (rb)
            with open("data.pkl","rb") as fr:
                Data.KEY_Settings = dill.load(fr).KEY_Settings
            if(len(Data.KEY_Settings) == 0):
                Data.KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_ESCAPE, pg.K_1, pg.K_2, pg.K_3, pg.K_4]
                with open('data.pkl', 'wb') as f:
                    dill.dump(Data, f)
            
                
        except: # data 파일이 없다면 기본값을 초기화 하고 만든다 (wb)
            Data.KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_ESCAPE, pg.K_1, pg.K_2, pg.K_3, pg.K_4]
            with open("data.pkl", "wb") as fw:
                dill.dump(Data.KEY_Settings, fw)
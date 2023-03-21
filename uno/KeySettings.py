import pygame as pg
import pickle

KEY_Settings = []

def save_settings(idx, key):
    global KEY_Settings
    KEY_Settings[idx] = key
    with open('data.pickle', 'wb') as f:
        pickle.dump(KEY_Settings, f)
    with open("data.pickle","rb") as fr:
        KEY_Settings = pickle.load(fr)
    print(KEY_Settings)

def load_settings():
    global KEY_Settings
    try: # data 파일이 있을 때 로드한다 (rb)
        with open("data.pickle","rb") as fr:
            KEY_Settings = pickle.load(fr)
        if(len(KEY_Settings) == 0):
            KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_KP_ENTER]
            with open('data.pickle', 'wb') as f:
                pickle.dump(KEY_Settings, f)
        
            
    except: # data 파일이 없다면 기본값을 초기화 하고 만든다 (wb)
        KEY_Settings = [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RETURN, pg.K_KP_ENTER]
        with open("data.pickle", "wb") as fw:
            pickle.dump(KEY_Settings, fw)
        
        
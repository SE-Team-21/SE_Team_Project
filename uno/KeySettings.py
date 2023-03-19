import pygame as pg
import pickle

UpKey = pg.K_UP
LeftKey = pg.K_LEFT
DownKey = pg.K_DOWN
RightKey = pg.K_RIGHT
ReturnKey = pg.K_RETURN
EnterKey = pg.K_KP_ENTER

KEY_Settings = {
    'UpKey': UpKey,
    'LeftKey': LeftKey,
    'DownKey' : DownKey,
    'RightKey' : RightKey,
    'ReturnKey' : ReturnKey,
    'EnterKey' : EnterKey,
}

def save_settings():
    global KEY_Settings
    with open('data.pickle', 'wb') as f:
        pickle.dump(KEY_Settings, f)
    

def load_settings():
    global UpKey, LeftKey, DownKey, RightKey, ReturnKey, EnterKey, KEY_Settings
    try:
        with open("data.pickle","rb") as fr:
            KEY_Settings = pickle.load(fr)
            UpKey = KEY_Settings['UpKey']
            LeftKey = KEY_Settings['LeftKey']
            DownKey = KEY_Settings['DownKey']
            RightKey = KEY_Settings['RightKey']
            ReturnKey = KEY_Settings['ReturnKey']
            EnterKey = KEY_Settings['EnterKey']
            
    except:
        UpKey = pg.K_UP
        LeftKey = pg.K_LEFT
        DownKey = pg.K_DOWN
        RightKey = pg.K_RIGHT
        ReturnKey = pg.K_RETURN
        EnterKey = pg.K_KP_ENTER
        settings = {
            'UpKey': UpKey,
            'LeftKey': LeftKey,
            'DownKey' : DownKey,
            'RightKey' : RightKey,
            'ReturnKey' : ReturnKey,
            'EnterKey' : EnterKey,
        }
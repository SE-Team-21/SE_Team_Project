import KeySettings
import pickle

with open("data.pickle","rb") as fr:
    KEY_Settings = pickle.load(fr)
print(KEY_Settings)
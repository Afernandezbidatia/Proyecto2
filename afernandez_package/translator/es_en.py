import os 
import json

HERE = os.path.abspath(os.path.dirname(__file__))

with open(f'{HERE}/../data/es_en.json','r') as f:
    TRANSALATIONS = json.loads(f.read())

def translate_word(word):
    if word not in TRANSALATIONS.keys():
        return "No se encuentra la palabra"
    else:
        return TRANSALATIONS[word]
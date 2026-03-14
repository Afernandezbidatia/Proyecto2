import sys
import os
import json
from afernandez_package.translator import en_es, es_en

HERE = os.path.abspath(os.path.dirname(__file__))

with open(f'{HERE}\data\_translator-types.json','r') as f:
      TRANSLATION_TYPES = json.loads(f.read())

if __name__ == "__main__":
    translatio_type = sys.argv[1]
    word = sys.argv[2]

    if translatio_type == "en_es":
            print(en_es.translate_word(word))
    elif translatio_type == "es_en":
          print(es_en.translate_word(word))
    else:
          print(f"tanslation not suppored {translatio_type}. Tipos disponibles: {TRANSLATION_TYPES}")
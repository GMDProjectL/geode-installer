import json
import os

locales_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(locales_dir, 'en.json')) as f:
    en = json.load(f)

with open(os.path.join(locales_dir, 'ru.json')) as f:
    ru = json.load(f)


def get_text(key, locale='en_US.UTF-8'):
    if locale.startswith('en'):
        return en.get(key, '')
    
    if locale.startswith('ru'):
        return ru.get(key, '')

    return en.get(key, '')
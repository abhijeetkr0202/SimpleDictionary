import os
import requests

def get_meaning(lang,word):
    url="https://api.dictionaryapi.dev/api/v2/entries/"+lang+"/"+word
    r=requests.get(url)
    mean=r.json()
    return mean


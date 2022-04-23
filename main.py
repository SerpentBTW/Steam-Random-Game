from msilib.schema import AppId
from textwrap import indent
from webbrowser import get
import requests;
import json
import sys
import random
from types import SimpleNamespace


authKey = input("Insert Key Here");
authID = input('Insert ID Here');

response = requests.get(url =' http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+authKey+'&steamid='+authID+'&format=json&include_appinfo=true&include_played_free_games=true')

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

responeJson = json.loads(response.text)


gameCount = responeJson['response']['game_count']
gameList = [];

x = 0
while (x < gameCount):
    gameList.append(responeJson['response']['games'][x]['name'])
    x+=1


rand = random.randint(0, len(gameList))
print(gameList[rand])


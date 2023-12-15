import bot
import json 
import os 
from json import JSONDecodeError
if __name__ == '__main__':
    
    if(os.path.isfile("./serverConfig.json")): 
        arg = 'r+'
    else: 
        arg = 'w+'
    with open("serverConfig.json", arg) as f: 
        jsonDict = json.load(f) 
        kitty = bot.CatBot(jsonDict, f)
        kitty.runDiscordBot()

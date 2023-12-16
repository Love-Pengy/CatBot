import bot
import json 
import os 
from json import JSONDecodeError
CONFIGFILE = 'serverConfig.json'
if __name__ == '__main__':
    
    if(os.path.isfile(CONFIGFILE)): 
        arg = 'r+'
    else: 
        arg = 'w+'
    with open(CONFIGFILE, arg) as f: 
        jsonDict = json.load(f) 
        kitty = bot.CatBot(jsonDict, CONFIGFILE)
        kitty.runDiscordBot()

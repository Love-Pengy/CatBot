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

        try: 
            jsonDict = json.load(f) 
            kitty = bot.CatBot(jsonDict, CONFIGFILE)
            kitty.runDiscordBot()
        except JSONDecodeError: 
            print("JSON is empty")
            exception = 1

        if(exception): 
            kitty = bot.CatBot(None, CONFIGFILE)
            kitty.runDiscordBot()

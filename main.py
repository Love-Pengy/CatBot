import bot
import json 
import os 
from json import JSONDecodeError

class TokenException(Exception): 
    pass

CONFIGFILE = 'serverConfig.json'
TOKENFILE = 'tokens.json'

if __name__ == '__main__':
    
    if(os.path.isfile(CONFIGFILE)): 
        arg = 'r+'

    else: 
        arg = 'w+'

    channelId = ""
    token = ""
    channelExcept = 0
    

    with open(TOKENFILE, 'r') as t: 
        try: 
            idJson = json.load(t)
            channelId = idJson[0]["channelId"]
        except JSONDecodeError: 
            print("CHANNELID was not specified")
            channelId = None
            channelExcept = 1

    with open(TOKENFILE, 'r') as t: 
        try: 
            idJson = json.load(t)
            token = str(idJson[0]["token"])
        except Exception: 
            raise TokenException("TOKEN was not specified")
        


    with open(CONFIGFILE, arg) as f: 
            try: 
                jsonDict = json.load(f) 
                kitty = bot.CatBot(jsonDict, CONFIGFILE, token, channelId)
                kitty.runDiscordBot()
            except JSONDecodeError: 
                print("JSON is empty")
                configExcept = 1

            if(configExcept): 
                kitty = bot.CatBot(None, CONFIGFILE, token, channelId)
                kitty.runDiscordBot()

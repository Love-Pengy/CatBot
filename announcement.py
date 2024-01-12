import discord 
import json
from time import time
import asyncio
from datetime import datetime
import os

 
async def sendMessage(client, message, channelId=None):
    await client.get_channel(channelId).send(message)



class TokenException(Exception): 
    pass

class ConfigException(Exception): 
    pass

async def main(): 
    token = ""
    ANFILE = 'announcement'
    TOKENFILE = 'tokens.json'
    CONFIGFILE = 'serverConfig.json'

    with open(TOKENFILE, 'r') as t: 
        try: 
            idJson = json.load(t)
            token = str(idJson[0]["token"])
        except json.JSONDecodeError as e: 
            print(e)
            quit()
        except Exception: 
            raise TokenException("TOKEN was not specified")

        

    if(os.path.isfile(ANFILE)): 
        with open(ANFILE, 'r') as f: 
            announceMessage = f.readline()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    await client.start(token)
    print(f"{client.user} is now running")

    if(os.path.isfile(CONFIGFILE)): 
        with open(CONFIGFILE, 'r') as f: 
            configJson = json.load(f)
            for element in configJson: 
               sendMessage(client, announceMessage, element["channelId"])
    else: 
        raise ConfigException("Config File Not Found")

    
    
asyncio.run(main())

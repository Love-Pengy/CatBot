import discord 
import json
from time import time
import asyncio
from datetime import datetime
import os
import re

async def sendMessage(client, message, channelId=None):
    print(f"got to sending message part: {message=} {channelId=}")
    await client.get_channel(channelId).send(embed=message)
    print("after?")



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
            announceMessage = re.sub("\n", "", announceMessage)
            announceMessage = "**" + announceMessage + "**"
            embed = discord.Embed()
            embed.color = discord.Color.from_rgb(255,192,203)
            embed.add_field(name="", value=f"{announceMessage}")
            announceMessage = embed


    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready(): 
        print(f"{client.user} is now running")
        if(os.path.isfile(CONFIGFILE)): 
            with open(CONFIGFILE, 'r') as f: 
                configJson = json.load(f)
                for element in configJson: 

                    channel = discord.utils.get(client.get_all_channels(), guild__name=f'{element["server"]}', name=f'{element["channel"]}')
                    if(channel is None): 
                        val = element["server"]
                        print(f"channel for {val} does not exist anymore")
                        continue
                    else: 
                        print(f"announcement start send: {element}")
                        await sendMessage(client, announceMessage, element["channelId"])
            print("announcement sent")
            exit(0)
        else: 
            raise ConfigException("Config File Not Found")

    await client.start(token)


if __name__ == "__main__": 
    asyncio.run(main())


import responses
import discord 
import json
from time import time
from discord.ext import tasks

DAY = 86400
LOG = 0
TOKEN = "PUT TOKEN HERE"



class CatBot: 

    def __init__(self, config: list, fileName): 
        if(config is None): 
            self.config = list()
            self.fileName = fileName
        else: 
            self.config = config
            self.fileName = fileName 

    async def sendMessage(self, message, user_message): 

        try: 
            response = responses.getResponse(user_message)
            if(response is None): 
                await message.channel.send("Error Has Occured Please Try Again :3")
            elif(isinstance(response, discord.Embed)): 
                await message.channel.send(embed=response)
            else: 
                await message.channel.send(response) 

        except Exception as e: 
            print(e)

        
    def runDiscordBot(self): 
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready(): 
            print(f"{client.user} is now running")
            await catTimer()

        @client.event
        async def on_message(message): 

            if(message.author == client.user): 
                return

            username = str(message.author)
            userMessage = str(message.content)
            channel = str(message.channel)
            server = str(message.channel.guild)
            
            if(LOG):  
                print(f"{username=}, {userMessage=}, {channel=}")

            if(userMessage == ":3 setup"): 
                self.channelSetup(channel, server)

            elif(userMessage == ":3 cat"): 

                for i, d in enumerate(self.config): 
                    try: 
                        if((server == d["server"]) and (d["channel"] == channel)): 
                            await self.sendMessage(message, userMessage)
                            break
                    except KeyError: 
                        continue

                else: 
                    await self.sendMessage(message, "Invalid Channel")

            elif(userMessage.startswith(":3 timer")): 
                #SET INTERVAL FOR THE SERVER TO WHATEVER IS SPECIFIED
                try: 
                    for d, i in enumerate(self.config): 
                        if((d["server"] == server) and (d["channel"] == channel)): 
                            d["interval"] = int(userMessage[9:])
                            break 
                    else: 
                        await self.sendMessage(message, "Invalid Timer Channel")

                except KeyError as e: 
                    print(e)
                
            else: 
                await self.sendMessage(message, userMessage)
             
        @client.event
        async def catTimer(): 
            if(self.config is not None): 
                for i, d in enumerate(self.config):
                    print(d)
                    if(time() - (d["lastTime"]/d["interval"])): 
                        message = discord.Message()
                        message.channel = d["channel"]
                        message.guild = d["server"]
                        await self.sendMessage(message, ":3 cat")
                        print("time has elapsed")



        client.run(TOKEN)

    def channelSetup(self, channel, server):

        for i, d in enumerate(self.config): 
            try: 
                #print(f"{d[server]=}, {server=}")
                print(f"{i=}", d["server"])
                if(d["server"] == server): 
                    if(channel != d["channel"]): 
                        print(channel)
                        self.config[i]["channel"] = channel
                        with open(self.fileName, 'w') as f: 
                            json.dump(self.config, f, separators=(',', ':'))
                            break
                    else: 
                        break

            except KeyError as key: 
                print("error with", key) 
                pass

        else: 
            newDict = dict()
            newDict["server"] = server 
            newDict["channel"] = channel
            newDict["interval"] = 1
            midnight = (int(time() // 86400)) * 86400
            newDict["lastTime"] = midnight
            self.config.append(newDict)
            with open(self.fileName, 'w') as f: 
                json.dump(self.config, f, separators=(',', ':'))

        


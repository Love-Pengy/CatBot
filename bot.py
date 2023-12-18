import responses
import discord 
import json
from time import time
import asyncio
from datetime import datetime


DAY = 86400
LOG = 0
TOKEN = "PUT TOKEN HERE"
MAXDAILYCATS = 1440
STARTUPCHANNELID = "PUT ID INT HERE"



class CatBot: 

    def __init__(self, config: list, fileName): 
        if(config is None): 
            self.config = list()
            self.fileName = fileName
        else: 
            self.config = config
            self.fileName = fileName 

    async def sendMessage(self, message, user_message, channelId=None):

        if(message is not None): 
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
        else: 
            response = responses.getResponse(user_message)
            if(response is None): 
                pass
            elif(isinstance(response, discord.Embed)): 
                await self.client.get_channel(channelId).send(embed=response)
            else: 
                await self.client.channelId.send(response) 
            

        
    def runDiscordBot(self): 
        intents = discord.Intents.default()
        intents.message_content = True
        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready(): 
            await self.client.get_channel(STARTUPCHANNELID).send(f"[{datetime.now()}] ~ Meow")
            print(f"{self.client.user} is now running")

        @self.client.event
        async def on_message(message): 

            if(message.author == self.client.user): 
                return

            username = str(message.author)
            userMessage = str(message.content)
            channel = str(message.channel)
            server = str(message.channel.guild)
            channelId = int(message.channel.id)
            
            if(LOG):  
                print(f"{username=}, {userMessage=}, {channel=}")

            if(userMessage == ":3 setup"): 
                self.channelSetup(channel, server, channelId)
                embed = discord.Embed()
                embed.color = discord.Color.pink()
                embed.add_field
                embed.add_field(name="", value="Cats Will Now Be Sent In This Channel! :3")
                await message.channel.send(embed=embed)
                

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
                floatChecker = float(userMessage[9:]).is_integer()
                timerNum = int(float(userMessage[9:]))
                if((timerNum <= MAXDAILYCATS) and (timerNum != 0) and floatChecker and not(timerNum < 0)):
                    try: 
                        for i, d in enumerate(self.config): 
                            if((d["server"] == server) and (d["channel"] == channel)): 
                                d["interval"] = int(userMessage[9:])
                                with open(self.fileName, 'w') as f: 
                                    json.dump(self.config, f, separators=(',', ':'))
                                embed = discord.Embed()
                                embed.color = discord.Color.pink()
                                interval = d["interval"]
                                if(d["interval"] <= 12): 
                                    embed.add_field(name="", value=f"Cats Will Now Be Sent Every **{(1440/interval)/60}** Hours! :3")
                                else:  
                                    embed.add_field(name="", value=f"Cats Will Now Be Sent Every **{(1440/interval)}** Minutes! :3")

                                await message.channel.send(embed=embed)
                                break 
                        else: 
                            await self.sendMessage(message, "Invalid Timer Channel")
                                

                    except KeyError as e: 
                        print(e)
                else: 
                    if(timerNum == 0): 
                        await self.sendMessage(message, "Interval Of 0")

                    elif(timerNum < 0): 
                        await self.sendMessage(message, "Negative Interval")

                    elif(not floatChecker):                         
                        await self.sendMessage(message, "Invalid Interval Type")

                    else: 
                        embed = discord.Embed()
                        embed.color = discord.Color.pink()
                        embed.add_field(name="", value=f"Value Exceeds Max Daily Cat Value Of: **{MAXDAILYCATS}**! :3")
                        await message.channel.send(embed=embed)
                
            else: 
                await self.sendMessage(message, userMessage)
             
        @self.client.event
        async def catTimer(): 
            while True: 
                try: 
                    if(self.config is not None): 
                        for i, d in enumerate(self.config):
                            if((d["lastTime"] + (DAY/d["interval"]) < time())): 
                                d["lastTime"] = time()
                                with open(self.fileName, 'w') as f: 
                                    json.dump(self.config, f, separators=(',', ':'))
                                await self.sendMessage(None, ":3 cat", d["channelId"])
                                print("time has elapsed")
                except AttributeError as e: 
                    print(e)
                    asyncio.sleep(30)
                    continue
                await asyncio.sleep(10)

        async def main(): 
            async with self.client: 
                asyncio.create_task(catTimer())
                await self.client.start(TOKEN)

        asyncio.run(main())

    def channelSetup(self, channel, server, channelId=None):

        for i, d in enumerate(self.config): 
            try: 
                #print(f"{d[server]=}, {server=}")
                print(f"{i=}", d["server"])
                if(d["server"] == server): 
                    if(channel != d["channel"]): 
                        print(channel)
                        self.config[i]["channel"] = channel
                        if(channelId): 
                            self.config[i]["channelId"] = channelId
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
            newDict["channelId"] = channelId
            self.config.append(newDict)
            with open(self.fileName, 'w') as f: 
                json.dump(self.config, f, separators=(',', ':'))




        


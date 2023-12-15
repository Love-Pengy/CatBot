import responses
import discord 
import json
LOG = 0
TOKEN = "PUT TOKEN HERE" 

class CatBot: 
    def __init__(self, servers: dict, fp): 
        self.validChannels = servers.copy
        print(type(self.validChannels))
        self.file = fp 

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
            else: 
                if((server in self.validChannels) and (self.validChannels[server] == channel)): 
                    await self.sendMessage(message, userMessage)
                else:
                    self.channelSetup(channel, server)


        client.run(TOKEN)

    def channelSetup(self, channel, server):
        if(server in self.validChannels): 
            self.validChannels = channel
        else: 
            self.validChannels[server] = channel
        print(type(self.validChannels))
        json.dump(self.validChannels, self.file)

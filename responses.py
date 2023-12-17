import requests
import discord


def counter(): 
    num = 0
    while True: 
        yield num 
        num += 1
catCounter = counter()

def getResponse(message) -> str: 

    userMessage = message.lower()
    
    if(userMessage == ":3"): 
        return(":3")

    if(userMessage == "invalid channel"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value = "Invalid Channel! Type **:3 help** for help! :3")
        return(embed)

    if(userMessage  == "meow"): 
        return("mrow! :3")
    
    if(userMessage == ":3 help"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="Prefix", value = "**:3**", inline=False)
        embed.add_field(name="Setup", value="**:3 setup**: Set channel to allow cat requests within", inline=False)
        embed.add_field(name="Usage", value="**:3 cat**: Request another cat!", inline=False)
        return(embed)
    
    if(userMessage == ":3 cat"): 
    
        currCat = next(catCounter)
        url = getRandomCatImageUrl()
        if(url is not None): 
            embed = discord.Embed(
                title = f'Meow Meow Maruader #{currCat}', 
                color = discord.Color.pink()
            )
            embed.set_image(url=url)
            return(embed)
        else: 
            return(None)
    
    if(userMessage.startswith(":3 timer")): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value = f"Images Will Be Sent *{int(userMessage[9:])}* Times A Day! :3")
        return(embed)

    return

def getRandomCatImageUrl(): 

    request = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png')
    json = request.json()
    try: 
        url = json[0]['url']
    except Exception as e: 
        print(e)
        return(None)
    return(url)  

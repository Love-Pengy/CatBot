import requests
import discord
import asyncio
from datetime import datetime

def counter(): 
    try: 
        with open("numCats", "r") as f: 
            num = f.readline() 
            if(num == ''): 
                num = str(0)
            num = int(num) + 1

    except Exception as e: 
        print(e)
        num = 0
        with open("numCats", "w") as f: 
            f.write(str(0))

    while True: 
        yield num 
        num += 1
        with open("numCats", "w") as f: 
            f.write(str(num))

catCounter = counter()

def getResponse(message) -> str: 
    userMessage = message.lower()
    
    if(userMessage == ":3"): 
        return(":3")

    if(userMessage == "invalid channel"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value = "Invalid Channel! Type **:3 help** for help! :3")
        return(embed)
    if(userMessage == "invalid timer channel"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value = "Please Try Again In The Channel That Is Setup For Cats! :3")
        return(embed)

    if(userMessage  == "meow"): 
        return("mrow! :3")

    if(userMessage == "nyan"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.set_image(url="https://media1.tenor.com/m/9fV87rRDzDgAAAAC/ansubin0925hellomynameissoobin.gif")
        embed.title = "Cat! :3"
        return(embed)
    
    if(userMessage == ":3 help"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="Prefix", value = "**:3**", inline=False)
        embed.add_field(name="Setup", value="**:3 setup**: Set Channel To Allow Cat Requests Within!", inline=False)
        embed.add_field(name="Interval", value="**:3 timer {time}**: Set Amount Of Times Per Day Cats Are Automatically Sent!", inline=False)
        embed.add_field(name="", value="**:3 timer remove**: Disable The Automatic Sending Of Cats! :3", inline=False)
        embed.add_field(name="", value="**:3 timer current**: See The Rate At Which The Automatic Sending Of Cats Occurs! :3", inline=False)
        embed.add_field(name="Usage", value="**:3 cat or :3 meow**: Request Another Cat!", inline=False)        
        embed.add_field(name="", value="**:3 dog or :3 woof**: Request A Dog Friend!", inline=False)
        embed.add_field(name="Response Messages", value="nyan, meow, :3, woof, and arf!", inline=False)
        return(embed)

    if(userMessage == "timer value not specified"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value="Interval Not Specified. Please Try Again! :3", inline=False)        
        return(embed)


    if(userMessage == "invalid interval type"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value="Please Enter An Integer For The Cat Interval! :3")
        return(embed)

    
    if((userMessage == ":3 cat") or (userMessage == ":3 meow")): 
        currCat = next(catCounter)
        url = getRandomCatImageUrl()
        if(url is not None): 
            embed = discord.Embed(
                title = f'Meow Meow Maruader #{currCat}', 
                color = discord.Color.from_rgb(255,192,203)
            )
            embed.set_image(url=url)
            return(embed)
        else: 
            return(None)
    if(userMessage == "woof"): 
       return("meeeoof!...I'm Still Working On It :3")

    if(userMessage == "arf"): 
       return("mearf!...Look At Me I'm Getting Good! :3")

    if((userMessage == ":3 dog") or (userMessage == ":3 woof")): 
        url = getRandomDogImageUrl()
        if(url is not None): 
            embed = discord.Embed()
            embed.title = "Check Out My Friend! :3"
            embed.color = discord.Color.from_rgb(255,192,203)
            embed.set_image(url=url)
            return(embed)

    if(userMessage == "negative interval"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value="You're Smart! But Uh I Can't Do Math... Please Enter A Non-Negative Number! :3")
        return(embed)

    if(userMessage == "interval of 0"): 
        embed = discord.Embed()
        embed.color = discord.Color.from_rgb(255,192,203)
        embed.add_field(name="", value="You Can't Have 0 Cats Silly! Please Try Again! :3")
        return(embed)

    return

def getRandomCatImageUrl(): 
    request = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png')
    try: 
        json = request.json()
    except json.decoder.JSONDecodeError as e: 
       print(e, datetime.now())
       asyncio.sleep(5) 
       return(getRandomCatImageUrl())

    except json.RequestsJSONDecodeError as e: 
        print(e, datetime.now())
        asyncio.sleep(5)
        return(getRandomCatImageUrl())

    try: 
        url = json[0]['url']
    except Exception as e: 
        print(e)
        return(None)
    return(url)  


def getRandomDogImageUrl(): 
    request = requests.get('https://api.thedogapi.com/v1/images/search?mime_types=jpg,png')
    try:  
        json = request.json()
    except json.decoder.JSONDecodeError as e: 
       print(e, datetime.now())
       asyncio.sleep(5) 
       return(getRandomDogImageUrl())

    except json.RequestsJSONDecodeError as e: 
        print(e, datetime.now())
        asyncio.sleep(5)
        return(getRandomCatImageUrl())

    try: 
        url = json[0]['url']
    except Exception as e: 
        print(e)
        return(None)
    return(url)  







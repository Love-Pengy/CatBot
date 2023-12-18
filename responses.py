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
    if(userMessage == "invalid timer channel"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value = "Please Try Again In The Channel That Is Setup For Cats! :3")
        return(embed)

    if(userMessage  == "meow"): 
        return("mrow! :3")
    
    if(userMessage == ":3 help"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="Prefix", value = "**:3**", inline=False)
        embed.add_field(name="Setup", value="**:3 setup**: Set Channel To Allow Cat Requests Within", inline=False)
        embed.add_field(name="Interval", value="**:3 timer {time}**: Set Amount Of Times Per Day Cats Are Automatically Sent", inline=False)
        embed.add_field(name="", value="**:3 timer remove**: Disable The Automatic Sending Of Cats! :3", inline=False)
        embed.add_field(name="Usage", value="**:3 cat**: Request Another Cat!", inline=False)        
        return(embed)

    if(userMessage == "timer value not specified"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value="Interval Not Specified. Please Try Again! :3", inline=False)        
        return(embed)


    if(userMessage == "invalid interval type"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value="Please Enter An Integer For The Cat Interval! :3")
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

    if(userMessage == "negative interval"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value="You're Smart! But Uh I Can't Do Math... Please Enter A Non-Negative Number! :3")
        return(embed)

    if(userMessage == "interval of 0"): 
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.add_field(name="", value="You Can't Have 0 Cats Silly! Please Try Again! :3")
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

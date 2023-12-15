import requests
import discord
global num 

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

    if(userMessage  == "meow"): 
        return("mrow! :3")
    
    if(userMessage == ":3 help"): 
        return("`help message :3`")
    
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

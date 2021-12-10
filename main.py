import discord, requests, asyncio, json
from time import sleep
from colorama import Fore, init
from discord.ext import commands
https://youtu.be/Fw3RB7xnb80
init()
bot = commands.Bot(
  command_prefix='duck!',
  self_bot=True
) 
bot.remove_command('help')
def logo():
  print(Fore.YELLOW + """
                                                                                  
                                  ****,,,,.                                     
                                *******,,,,**.                                  
                              #****, @@,,,,****                                 
                         (((*(//(((,,***,,,,****                                
                        (((((((/(/(((/******////,                               
                        ,(((#((#(((#/***////////                                
                         /(((((((((####(///////.                                
                             (((((((#/////////      ,**,                        
                             ,////////******/*********/**                       
                         *************,*******************                      
                       ***************,,,******************                     
                      ********,,,,*****************////////*                    
                     ****************************///////////                    
                     ,*******************//////////////////.                    
                      ***************/*///////////////////                      
                         ****************3\ **********
  """)
  print(Fore.RED + """
  

 ______   __   __  _______  ___   _  _______  _______  ______    ______  
|      | |  | |  ||       ||   | | ||       ||       ||    _ |  |      | 
|  _    ||  | |  ||       ||   |_| ||       ||   _   ||   | ||  |  _    |
| | |   ||  |_|  ||       ||      _||       ||  | |  ||   |_||_ | | |   |
| |_|   ||       ||      _||     |_ |      _||  |_|  ||    __  || |_|   |
|       ||       ||     |_ |    _  ||     |_ |       ||   |  | ||       |
|______| |_______||_______||___| |_||_______||_______||___|  |_||______| 


  """)
  
sleep(1)
with open("config.json") as file:
    info = json.load(file)
    TOKEN = info["token"] 
    CITY = info["city"] 
if TOKEN == "your token goes here":
  f = open("config.json", "r")
  json_object = json.load(a_file)
  tkn = input("Your discord token: ")
  json_object["token"] = tkn
  a_file = open("config.json", "w")
  json.dump(json_object, a_file)
  a_file.close()
elif CITY == "your city goes here":  
  f = open("config.json", "r")
  json_object = json.load(a_file)
  tkn = input("Your city: ")
  json_object["city"] = tkn
  a_file = open("config.json", "w")
  json.dump(json_object, a_file)
  a_file.close()

print(Fore.GREEN + f"Welcome, {bot.user.name}!")
playsound('quack.mp3')
print(Fore.RESET + "Use [duck help] to see all commands")


@bot.event
async def on_message(msg):
  if msg.author == bot.user:
    if msg.content == "duck help":
      embed = discord.Embed(title="DuckCord Help", description="`duck help` - Shows this message\n`duck pic` - Sends a duck image\n`duck weather` - Weahter at your place")
      embed.set_thumbnail(url="https://www.kindpng.com/picc/m/179-1790702_duck-toy-png-transparent-image-rubber-duck-transparent.png")
      m = await msg.channel.send(embed=embed)
      await asyncio.sleep(20)
      await m.delete()
      await msg.delete()
    elif msg.content == "duck pic":
      apilink = "https://random-d.uk/api/random"
      r = requests.get(apilink)
      x = r.text
      y = json.loads(x)
      img = y['link']
      m = await msg.channel.send(img)
      await asyncio.sleep(20)
      await m.delete()
      await msg.delete()
    elif msg.content == "duck weather":
      apilink = "http://api.weatherapi.com/v1/current.json?key=2de3b3d81ede442da62104738211310&q=" + str(CITY)
      r = requests.get(apilink)
      x = r.text
      y = json.loads(x)
      location = y['location']['name']
      country = y['location']['country']
      update = y['current']['last_updated']
      weather = y['current']['condition']['text']
      celsius = y['current']['feelslike_c']
      far = y['current']['feelslike_f']
      m = await msg.channel.send(f"__**Weather in {location}, {country}**__\n{weather}\n{celsius}°C / {far}°F")
      await asyncio.sleep(20)
      await m.delete()
      await msg.delete()
    else:
      return
  else:
    return


bot.run(TOKEN, bot=False)

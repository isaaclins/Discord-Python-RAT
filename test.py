import pyautogui
from PIL import Image, ImageDraw


screenshot = pyautogui.screenshot()
overlay = Image.new('RGBA', screenshot.size, (0, 0, 0, 0))
grid_size = 100  # Size of each grid cell
grid_color = (255, 0, 0, 128)  # Grid color and transparency
for x in range(0, screenshot.width, grid_size):
    for y in range(screenshot.height):
        overlay.putpixel((x, y), grid_color)
for y in range(0, screenshot.height, grid_size):
    for x in range(screenshot.width):
        overlay.putpixel((x, y), grid_color)
result = Image.alpha_composite(screenshot.convert('RGBA'), overlay)
result.show()

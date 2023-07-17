import pyautogui
from PIL import Image, ImageDraw

# Capture screenshot
screenshot = pyautogui.screenshot()

# Create a new image with the same size as the screenshot
overlay = Image.new('RGBA', screenshot.size, (0, 0, 0, 0))

# Set the grid parameters
grid_size = 100  # Size of each grid cell
grid_color = (255, 0, 0, 128)  # Grid color and transparency

# Draw vertical grid lines
for x in range(0, screenshot.width, grid_size):
    for y in range(screenshot.height):
        overlay.putpixel((x, y), grid_color)

# Draw horizontal grid lines
for y in range(0, screenshot.height, grid_size):
    for x in range(screenshot.width):
        overlay.putpixel((x, y), grid_color)

# Overlay the grid on the screenshot
result = Image.alpha_composite(screenshot.convert('RGBA'), overlay)

# Display the result
result.show()

from PIL import Image, ImageDraw

# Create a 50x50 green square for the snake head
img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))  # Transparent background
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, 50, 50], fill=(0, 255, 0))  # Green fill
img.save("snake_head.gif", "GIF")
print("snake_head.gif created!")

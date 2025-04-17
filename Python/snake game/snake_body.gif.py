from PIL import Image, ImageDraw

# Create a 50x50 grey square for the snake body
img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, 50, 50], fill=(128, 128, 128))  # Grey fill
img.save("snake_body.gif", "GIF")
print("snake_body.gif created!")

from PIL import Image, ImageDraw

# Create a 50x50 brown square for obstacles
img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, 50, 50], fill=(139, 69, 19))  # Brown fill (saddle brown)
img.save("obstacle.gif", "GIF")
print("obstacle.gif created!")

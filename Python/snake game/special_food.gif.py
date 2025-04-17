from PIL import Image, ImageDraw

# Create a 50x50 image with a blue triangle for special food
img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
# Define triangle vertices (centered and pointing up)
triangle = [(25, 5), (5, 45), (45, 45)]
draw.polygon(triangle, fill=(0, 0, 255))  # Blue fill
img.save("special_food.gif", "GIF")
print("special_food.gif created!")

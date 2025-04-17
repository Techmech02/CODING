from PIL import Image, ImageDraw

# Create a 50x50 image with a red circle for food
img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse([5, 5, 45, 45], fill=(255, 0, 0))  # Red circle with some padding
img.save("food.gif", "GIF")
print("food.gif created!")

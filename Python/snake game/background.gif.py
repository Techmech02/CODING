from PIL import Image, ImageDraw

# Create a 600x600 dark grey background
img = Image.new("RGBA", (600, 600), (50, 50, 50))  # Dark grey background
draw = ImageDraw.Draw(img)

# Optionally, add grid lines for a slight pattern
for i in range(0, 600, 20):
    draw.line([(i, 0), (i, 600)], fill=(80, 80, 80))  # Vertical grid lines
    draw.line([(0, i), (600, i)], fill=(80, 80, 80))  # Horizontal grid lines

img.save("background.gif", "GIF")
print("background.gif created!")


from PIL import Image, ImageDraw, ImageChops

grey = Image.new('RGB', (640, 480), 'lightgray')

market = Image.open('rynek.png')

d = ImageDraw.Draw(grey)
d.ellipse((100, 80, 540, 420), 'black')
combined = ImageChops.screen(grey, market)

combined.save('combined.png')


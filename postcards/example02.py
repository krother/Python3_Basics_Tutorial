
from PIL import Image, ImageDraw, ImageFont

white = Image.new('RGB', (320, 240), 'white')

d = ImageDraw.Draw(white)
d.rectangle((10, 10, 80, 40), 'orange')
d.ellipse((100,100,180,140), 'red')
d.polygon((50,200, 90, 200, 70, 170), 'yellow')

white.save('shapes.png')

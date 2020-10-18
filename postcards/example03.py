
from PIL import Image, ImageDraw, ImageFont

white = Image.new('RGB', (320, 240), 'white')

d = ImageDraw.Draw(white)
arial = ImageFont.truetype('arial.ttf', 40)
d.text((150, 150), 'Poznan', fill=('purple'), font=arial)

white.save('with_text.png')


from PIL import Image
from PIL import ImageDraw, ImageFont

market = Image.open('pillow/rynek.png')
cathedral = Image.open('pillow/katedra.png')
hotel = Image.open('pillow/hotel.png')
bridge = Image.open('pillow/most.png')

poznan = Image.new('RGB', (1280, 960), 'white')

poznan.paste(market, (0, 0))
poznan.paste(cathedral, (640, 0))
poznan.paste(hotel, (0, 480))
poznan.paste(bridge, (640, 480))

d = ImageDraw.Draw(poznan)
d.rectangle((0, 450, 1280, 510), 'blue')

arial = ImageFont.truetype('pillow/arial.ttf', 40)
d.text((450, 460), 'Welcome to Poznan', fill=('white'), font=arial)

poznan.save('poznan.png')


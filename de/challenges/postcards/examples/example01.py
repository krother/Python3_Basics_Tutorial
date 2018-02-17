
from PIL import Image

market = Image.open('rynek.png')

small = market.resize((320, 240))

upsidedown = small.rotate(180)


upsidedown.save('market.png')


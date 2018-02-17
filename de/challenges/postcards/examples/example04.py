
from PIL import Image

market = Image.open('rynek.png')
cathedral = Image.open('katedra.png')

small = market.resize((320, 240))

cathedral.paste(small, (0, 0))

cathedral.save('insert.png')


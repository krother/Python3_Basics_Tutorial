
# Create a Postcard

**🎯 Write a program that composes a postcard from your favorite city.**

![Welcome to Poznan](images/poznan.png)

## Step 1: Images

Obtain 2-4 images that you would like to assemble into a postcard.

## Step 2: Install Pillow

    pip install pillow

(Pillow is already installed on Anaconda)

## Step 3: Learn to know Pillow

Execute the following program:

    from PIL import Image

    im = Image.open('image1.png')
    small = im.resize((320, 240))
    result = small.rotate(180)
    result.save('image2.png')

Change the numbers to create a square image.

## Step 4: Draw Shapes

What does the following code do?

    from PIL import Image, ImageDraw

    white = Image.new('RGB', (320, 240), 'white')

    d = ImageDraw.Draw(white)
    d.rectangle((10, 10, 80, 40), 'orange')
    d.ellipse((100,100,180,140), 'red')
    d.polygon((50,200, 90, 200, 70, 170), 'yellow')

    white.save('shapes.png')

## Step 5: Drawing text

Add some Text:

    from PIL import ImageFont

    font =  ImageFont.load_default()
    d.text((150, 150), 'Poznan', fill=('purple'), font=arial)

If you find the TTF fonts on your system, it gets a lot prettier:

    font = ImageFont.truetype('arial.ttf', 40)

## Step 6: Assemble the image

Paste images with Pillow:

  image1.paste(image2, (0, 0))
  image1.save('postcard.png')

* Create a postcard composed of smaller pictures
* Add the horizontal bar and some text on it.

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*

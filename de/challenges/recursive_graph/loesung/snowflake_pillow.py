
from PIL import Image, ImageDraw, ImageFont, ImageFilter 
import math


class Turtle:
    """
    Draws turtle graphics on a white background.

    The turtle has a position and a direction,
    and can move forward and turn left and right.
    """
    def __init__(self):
        """Initializes the turtle."""
        self.x = 0
        self.y = 200
        self.angle = 0.0
        self.image = Image.new('RGB', (500, 250), (255,255,255))
        self.draw_tool = ImageDraw.Draw(self.image)

    def turn_left(self,ang):
        self.angle -= ang
        if self.angle<0: self.angle += 360
        
    def turn_right(self,ang):
        self.angle += ang
        if self.angle>=360: self.angle -= 360

    def move_forward(self,length,draw=True):
        """
        Moves the turtle forward in its current direction.
        It draws a line (can be turned off optionally."""
        new_x = self.x + length * math.cos(math.radians(self.angle))
        new_y = self.y + length * math.sin(math.radians(self.angle))
        self.draw_tool.line(((self.x,self.y),(new_x,new_y)), fill=(0,0,0),width=2)
        self.x = new_x
        self.y = new_y


       
def snowflake(turtle, length, depth):
    """Draws a recursive snowflake curve with the given turtle."""
    if depth == 0:
        turtle.move_forward(length)
    else:
        snowflake(turtle, length * 0.333, depth-1)
        turtle.turn_left(60)
        snowflake(turtle, length * 0.333, depth-1)
        turtle.turn_right(120)
        snowflake(turtle, length * 0.333, depth-1)
        turtle.turn_left(60)
        snowflake(turtle, length * 0.333, depth-1)
    


if __name__ == '__main__':
    """Main program. Starts the turtle and draws a snowflake."""
    # try different values for 'depth'
    t = Turtle()
    snowflake(t, 500, 1)
    t.image.save('snowflake1.png')
    t = Turtle()
    snowflake(t, 500, 2)
    t.image.save('snowflake2.png')
    t = Turtle()
    snowflake(t, 500, 5)
    t.image.save('snowflake3.png')

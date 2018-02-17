
from turtle import *
import canvasvg

reset()

speed('fastest')

MAX = 720
color(0, 0, 0)
width(5)

for i in range(MAX):
    forward(i / 80.0)
    left(3)
    #color(0, float(i) / MAX, 0)
    #width(i/30)

ts = getscreen().getcanvas()
canvasvg.saveall('spiral.svg', ts)







#
# Example: snowflake
#
# topics: functions, recursion
#

__author__ = "Kristian Rother, Nils Goldmann"

from turtle import *
import time

def move_to(x,y):
    up()
    setx(x)
    sety(y)
    down()


def curve(length, depth):
    if depth==0:
        forward(length)
    else:
        curve(length*0.333,depth-1)
        right(60)
        curve(length*0.333,depth-1)
        left(120)
        curve(length*0.333,depth-1)
        right(60)
        curve(length*0.333,depth-1)

reset()
left(180)

move_to(100, 100)
curve(200, 1)

move_to(100, 0)
curve(200, 2)

move_to(100, -100)
curve(200, 3)

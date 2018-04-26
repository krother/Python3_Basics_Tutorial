
import turtle
import canvasvg

turtle.speed(100)
turtle.width(3)

def save(fn):
    turtle.hideturtle()
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall(fn, ts)
    turtle.reset()
    turtle.width(3)
    turtle.speed(100)

# square
def square(w=100):
    for i in range(4):
        turtle.forward(w)
        turtle.left(90)

square()
save("square.svg")


# triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

save('triangle.svg')

# four squares
for i in range(4):
    square()
    turtle.up()
    turtle.forward(125)
    turtle.down()

save('four_squares.svg')

# star
for i in range(5):
    turtle.forward(100)
    turtle.left(145)
save('star.svg')

# concentric squares
for w in range(100, 0, -20):
    square(w)
    turtle.up()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
save('concentric.svg')

# nikohaus
square(100)
turtle.left(45)
turtle.forward(20000**0.5)
turtle.left(90)
turtle.forward(5000**0.5)
turtle.left(90)
turtle.forward(5000**0.5)
turtle.left(90)
turtle.forward(20000**0.5)
save('nikohaus.svg')

# square spiral
w = 10
for w in range(10, 160, 10):
    for j in range(2):
        turtle.forward(w)
        turtle.left(90)
save('square_spiral.svg')

# round spiral

# fibo spiral

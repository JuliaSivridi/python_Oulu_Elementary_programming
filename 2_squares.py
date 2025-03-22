from turtle import *

def draw_square(side, x, y):
    # write a function that draws a draws
    # a square with either red or blue fill
    # depending on the starting x position
    # being positive (blue) or negative (red)
    if x <= 0:
        color("red")
    else:
        color("blue")
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(side)
        right(90)
    end_fill()
    
# for _ in range(4):
    # goto(0, 0)
    # right(90)
    # forward(300)

draw_square(40, -100, 100)
draw_square(60, 100, -100)
draw_square(100, -50, -20)
draw_square(80, 90, 30)
done()

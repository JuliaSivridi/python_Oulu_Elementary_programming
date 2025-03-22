from turtle import *

def draw_spiral(c, arcs, r, g, w = 1):
    color(c)
    pensize(w)
    down()
    for _ in range(arcs):
        circle(r, 90)
        r += g
    up()
    
draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)
done()

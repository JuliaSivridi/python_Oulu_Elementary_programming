from turtle import *

def draw_spiral(c, arcs, r, g, w = 1):
    color(c)
    pensize(w)
    down()
    for _ in range(arcs):
        circle(r, 90)
        r += g
    up()

def read_row(row, results):
    try:
        color, arcs, radius, grow, width = row.split(",")
        result = {
            "color": color.strip(),
            "arcs": int(arcs),
            "radius": int(radius),
            "grow": float(grow),
            "width": int(width)
        }
        results.append(result)
    except ValueError:
        print(f"Unable to read row: {row}")

def draw_from_file(filename):
    results = []
    try:
        with open(filename) as source:
            for row in source.readlines():
                read_row(row, results)
    except IOError:
        print("Unable to open the target file. Starting with an empty results.")
    for r in results:
        draw_spiral(r['color'], r['arcs'], r['radius'], r['grow'], r['width'])

draw_from_file("spiral.txt")
done()

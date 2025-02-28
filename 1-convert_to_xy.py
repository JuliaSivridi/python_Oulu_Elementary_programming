import math

def convert_to_xy(angle, ray):
    x = int(round(ray * math.cos(angle)))
    y = int(round(ray * math.sin(angle)))
    return x, y

input_angle = float(input("Input angle in radians: "))
input_vector = float(input("Input vector length: "))
coord_x, coord_y = convert_to_xy(input_angle, input_vector)
print("Cartesian coordinates:", (coord_x, coord_y))

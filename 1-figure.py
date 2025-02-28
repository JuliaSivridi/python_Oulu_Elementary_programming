import math

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_sector_area(radius, angle):
    return math.pi * radius ** 2 * angle / 360

def calculate_catheti_length(hypotenuse):
    return math.sqrt(hypotenuse ** 2 / 2)

def calculate_figure_area(x):
    sm_sq_area = calculate_square_area(x)
    
    trg_area = sm_sq_area / 4

    big_square_side = 2 * calculate_catheti_length(x)
    big_sq_area = calculate_square_area(big_square_side)

    small_circle_radius = big_square_side / 2
    sm_crl_area = calculate_sector_area(small_circle_radius, 45)

    big_circle_radius = big_square_side
    big_crl_area = calculate_sector_area(big_circle_radius, 270)
    
    full_figure_area = sm_sq_area + trg_area + big_sq_area + sm_crl_area + big_crl_area
    return full_figure_area

# main program that prompts for x,
# calls the calculation function and 
# prints the rounded result

# s_length = float(input("Input square side length: "))
# square_area = calculate_square_area(s_length)
# print("Square area:", round(square_area, 4))

# circle_radius = float(input("Input circle radius: "))
# sector_angle = float(input("Input sector angle: "))
# sector_area = calculate_sector_area(circle_radius, sector_angle)
# print("Sector area:", round(sector_area, 4))

# hypotenuse_length = float(input("Input the hypotenuse length of a right isosceles triangle: "))
# catheti_length = calculate_catheti_length(hypotenuse_length)
# print("Catheti length:", round(catheti_length, 4))

input_x = float(input("Input x: "))
figure_area = calculate_figure_area(input_x)
print("Figure area:", round(figure_area, 4))

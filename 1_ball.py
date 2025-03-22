import math

def calculate_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_volume(radius):
    return 4 / 3 * math.pi * radius ** 3

def calculate_radius(circumference):
    return circumference / (math.pi * 2)

def calculate_ball_properties(circumference):
    radius = calculate_radius(circumference)
    area = calculate_area(radius)
    volume = calculate_volume(radius)
    return area, volume
    
measurement = float(input("Enter ball circumference: "))
ball_area, ball_volume = calculate_ball_properties(measurement)
print("Volume:", round(ball_volume, 4))
print("Surface area:", round(ball_area, 4))
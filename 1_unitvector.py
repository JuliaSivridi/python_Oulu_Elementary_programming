def calculate_unit_vector(x0, y0, x1, y1):
    length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    ux = (x1 - x0) / length
    uy = (y1 - y0) / length
    return ux, uy

def calculate_position(direction_x, direction_y, speed):
    x = direction_x * speed
    y = direction_y * speed
    return x, y

movement_speed = 5

print("This program calculates the unit vector between two points on a 2-dimensional plane")
initial_x = float(input("Input starting point x coordinate: "))
initial_y = float(input("Input starting point y coordinate: "))
target_x = float(input("Input target point x coordinate: "))
target_y = float(input("Input target point y coordinate: "))
vector_x, vector_y = calculate_unit_vector(initial_x, initial_y, target_x, target_y)
print("Directional vector (x y):", vector_x, vector_y)

new_x, new_y = calculate_position(vector_x, vector_y, movement_speed)
print(new_x)
print(new_y)

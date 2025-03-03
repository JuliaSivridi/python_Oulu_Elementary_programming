MESSAGES = {
    "outside": "The tile is outside the field.",
    "corner": "The tile is in the corner of the field.",
    "edge": "The tile is on the edge of the field.",
    "middle": "The tile is in the middle of the field."
}

def position_in_field(x, y, width, height):
    if x < 0 or x >= width or y < 0 or y >= height:
        pos_in_field = "outside"
    elif ((x == 0 and y == 0) or 
        (x == width-1 and y == 0) or 
        (x == 0 and y == height-1) or 
        (x == width-1 and y == height-1)):
        pos_in_field = "corner"
    elif ((x == 0 and 0 < y < height-1) or 
        (x == width-1 and 0 < y < height-1) or 
        (0 < x < width-1 and y == 0) or 
        (0 < x < width-1 and y == height-1)):
        pos_in_field = "edge"
    else:
        pos_in_field = "middle"
    return pos_in_field

def print_position(pos):
    try:
        print(MESSAGES[pos])
    except KeyError:
        print("Key not found")

input_w = int(input("Input field width: "))
input_h = int(input("Input field height: "))

if (input_w <= 0) or (input_h <= 0):
    print("You can't fit a single tile on a field that small!")
else:
    input_x = int(input("Input x coordinate: "))
    input_y = int(input("Input y coordinate: "))
    location = position_in_field(input_x, input_y, input_w, input_h)
    print_position(location)

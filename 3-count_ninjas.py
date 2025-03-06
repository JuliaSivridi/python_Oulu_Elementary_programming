def count_ninjas(x, y, r):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
    """
    height = len(r)
    width = len(r[0])
    if not (0 <= x < width and 0 <= y < height):
        print("Tile is out of the field")
        return 0

    n = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < width and 0 <= j < height and r[j][i] == 'N':
                n += 1
    if r[y][x] == 'N':
        n -= 1
    return n

room = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

print(" ", "- " * 5)
for row in room:
    print("|", " ".join(row), "|")
print(" ", "- " * 5)

x_inp = int(input("Input x coordinate: "))
y_inp = int(input("Input y coordinate: "))
ninjas = count_ninjas(x_inp, y_inp, room)
print(f"The tile is surrounded by {ninjas} ninjas")

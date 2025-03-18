import sweeperlib

state = {
    "field": []
}

def floodfill(fplanet, x, y):
    """
    Marks previously unknown connected areas as safe, starting from the given x, y coordinates.
    """
    if fplanet[y][x] == "x":
        return
    queue = [(x, y)]
    while queue:
        current_x, current_y = queue.pop()
        if fplanet[current_y][current_x] != " ":
            continue
        fplanet[current_y][current_x] = "0"
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x = current_x + dx
                new_y = current_y + dy
                if 0 <= new_x < len(fplanet[0]) and 0 <= new_y < len(fplanet):
                    if fplanet[new_y][new_x] == " ":
                        queue.append((new_x, new_y))

def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    mfield = state["field"]
    for y, mrow in enumerate(mfield):
        for x, tile in enumerate(mrow):
            screen_x = x * 40
            screen_y = (len(mfield) - 1 - y) * 40
            sweeperlib.prepare_sprite(tile, screen_x, screen_y)
    sweeperlib.draw_sprites()

def main(mplanet):
    """
    Loads graphics, creates a game window, and sets a draw handler.
    """
    state["field"] = mplanet
    sweeperlib.load_sprites("sprites")
    width = len(mplanet[0]) * 40
    height = len(mplanet) * 40
    sweeperlib.create_window(width, height)
    sweeperlib.set_draw_handler(draw_field)
    sweeperlib.start()

if __name__ == "__main__":
    planet = [
        [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
        [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
        [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
        ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
        ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
        [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
    ]
    floodfill(planet, 0, 0)
    main(planet)

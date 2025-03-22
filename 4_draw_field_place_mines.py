import random
import sweeperlib

state = {
    "field": []
}

def place_mines(mfield, avalbl, nmines):
    """
    Places N mines to a field in random tiles.
    """
    selected = random.sample(avalbl, nmines)
    for x, y in selected:
        mfield[y][x] = "x"
    for coord in selected:
        avalbl.remove(coord)

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

def main():
    """
    Loads the game graphics, creates a game window and sets a draw handler for it.
    """
    sweeperlib.load_sprites("sprites")
    # Create a window with a size of 600x400 pixels
    sweeperlib.create_window(600, 400)
    # Set the draw handler
    sweeperlib.set_draw_handler(draw_field)
    # Start the game
    sweeperlib.start()

if __name__ == "__main__":
    field = []
    for row in range(10):
        field.append([])
        for col in range(15):
            field[-1].append(" ")

    state["field"] = field

    available = []
    for x_avl in range(15):
        for y_avl in range(10):
            available.append((x_avl, y_avl))

    place_mines(field, available, 35)
    main()

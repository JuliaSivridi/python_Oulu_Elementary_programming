import json
import time
import math
import random
import sweeperlib

state = {
    "width": 0, "height": 0,
    "field": [], "cover": [], "free": [],
    "number_mines": 0, "closed_count": 0,
    "game_over": False, "game_win": False,
    "start": 0, "duration": 0, "turns": 0
}
stats = []
statsfile = "minestats.json"

def load_stats():
    """
    Loads the global statistics from the json file.
    """
    try:
        with open(statsfile) as source:
            stats = json.load(source)
    except (IOError, json.JSONDecodeError):
        print("Unable to open the target file. Starting with an empty collection.")
        stats = []
    return stats

def save_stats(stats):
    """
    Saves the current game statistics to the global statistics and writes it to the json file.
    """
    # Duration in minutes
    state["duration"] = int(time.time() - state["start"]) // 60
    # I adore the ternary conditional operator since php ;)
    outcome = "win" if state["game_win"] else "lose"
    # How many not flagged mines left
    mines_left = 0
    for y in range(state["height"]):
        for x in range(state["width"]):
            if state["field"][y][x] == "x" and state["cover"][y][x] != "f":
                mines_left += 1

    stats.append({
        "start": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(state["start"])),
        "duration": state["duration"],
        "turns": state["turns"],
        "outcome": outcome,
        "mines_left": mines_left
    })

    try:
        with open(statsfile, "w") as target:
            json.dump(stats, target, indent=4)
    except IOError:
        print("Unable to open the target file. Saving failed.")

def view_stats(stats):
    per_page = 5
    pages = math.ceil(len(stats) / per_page)
    for i in range(pages):
        start = i * per_page
        end = (i + 1) * per_page
        view_page(stats[start:end], i)
        if i < pages - 1:
            input("   -- press enter to continue --")

def view_page(lines, page_n):
    per_page = 5
    for i, stat in enumerate(lines, page_n * per_page + 1):
        print(
            f"Game was played on {stat['start']} for "
            f"{stat['duration']} minutes "
            f"with {stat['turns']} turn(s). "
            f"Game outcome is {stat['outcome']} with "
            f"{stat['mines_left']} mines left"
        )

def prompt_number(prompt, err, low, top):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print(err)
        else:
            if not (low <= number <= top):
                print(err)
            else:
                return number

def init_game():
    """
    Fills the field size and number of mines.
    Creates a mine field and a cover field.
    Reset the statistics variables for a new game.
    """
    # Player can input field size, but not greater than 50*30
    state["width"] = prompt_number("Input field width (1..50): ", "This does not fit", 1, 50)
    state["height"] = prompt_number("Input field height (1..30): ", "This does not fit", 1, 30)
    # Mines amount can't be bigger than field's square
    max_mines = state["width"] * state["height"]
    state["number_mines"] = prompt_number(f"Input mines number (1..{max_mines}): ", "This does not fit", 1, max_mines)
    # Counter for not opened cells without number of mines
    # Then becomes zero - game is won
    state["closed_count"] = max_mines - state["number_mines"]

    field = []
    cover = []
    free = []
    # Fill all lists in one cycle
    for row in range(state["height"]):
        field.append([])
        # Cover for field is totally closed
        cover.append([" "] * state["width"])
        for col in range(state["width"]):
            # Minefield is empty
            field[-1].append(0)
            # Save all coordinates
            free.append((col, row))
    state["field"] = field
    state["cover"] = cover
    state["free"] = free

    # Reset for new game
    state["game_over"] = False
    state["game_win"] = False
    # Save current game statistics
    state["start"] = time.time()
    state["duration"] = 0
    state["turns"] = 0

def place_mines():
    """
    Places mines to a field in random tiles.
    Places numbers around the mines.
    """
    selected = random.sample(state["free"], state["number_mines"])
    for x, y in selected:
        # Placing mine
        state["field"][y][x] = "x"
        # Increase numbers around mine
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < state["width"] and
                    0 <= ny < state["height"] and
                    state["field"][ny][nx] != "x"):
                    state["field"][ny][nx] += 1

def start_game():
    """
    Loads the game graphics, creates a game window and sets a draw handler for it.
    """
    sweeperlib.load_sprites("sprites")
    # Create a window with a size of field
    sweeperlib.create_window(40 * state["width"], 40 * state["height"])
    # Set the draw handler
    sweeperlib.set_draw_handler(draw_field)
    # Set the mouse click handler
    sweeperlib.set_mouse_handler(handle_mouse)
    # Start the game
    sweeperlib.start()

def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list into a game window.
    This function is called whenever the game engine requests a screen update.
    """
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    for y, line in enumerate(state["field"]):
        for x, tile in enumerate(line):
            screen_x = 40 * x
            screen_y = 40 * (state["height"] - 1 - y)
            # Cover opened -> draw field tiles: mine|number|empty
            if state["cover"][y][x] == 0:
                sweeperlib.prepare_sprite(tile, screen_x, screen_y)

    for y, line in enumerate(state["cover"]):
        for x, tile in enumerate(line):
            screen_x = 40 * x
            screen_y = 40 * (state["height"] - 1 - y)
            # Cover not opened -> draw cover: back|flag
            if tile != 0:
                sweeperlib.prepare_sprite(tile, screen_x, screen_y)

    sweeperlib.draw_sprites()
    msg_game_over()

def msg_game_over():
    """
    If a mine has opened or all tiles without mines have opened
    """
    if state["game_over"]:
        x_msg, y_msg = get_msg_position()
        if state["game_win"]:
            color = (255, 255, 32, 255)
            msg1, msg2 = "Congrats!", "You win! :-)"
        else:
            color = (255, 0, 0, 255)
            msg1, msg2 = "Game Over!", "You lose :-("
        sweeperlib.draw_text(msg1, x_msg, y_msg + 20, color=color, font="Arial")
        sweeperlib.draw_text(msg2, x_msg, y_msg - 20, color=color, font="Arial")

def get_msg_position():
    # Sometimes game window is too small :-(
    min_width = 300
    min_height = 200
    current_width = 40 * state["width"]
    current_height = 40 * state["height"]
    new_width = max(current_width, min_width)
    new_height = max(current_height, min_height)
    sweeperlib.resize_window(new_width, new_height, bg_color=(190, 190, 190, 255))
    x_msg = new_width // 2 - 100
    y_msg = (new_height - 40) // 2
    return x_msg, y_msg

def handle_mouse(x, y, button, modifiers):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    
    :param int x: x-coordinate of the mouse click
    :param int y: y-coordinate of the mouse click
    :param int button: mouse button clicked (use sweeperlib constants)
    """
    # Prevent opening tiles after game over
    if state["game_over"]:
        return

    grid_x = int(x) // 40
    grid_y = (state["height"] - 1) - (int(y) // 40)
    # Prevent clicking outside the field
    if not (0 <= grid_x < state["width"] and 0 <= grid_y < state["height"]):
        return

    # Open covered tile without flag
    if button == sweeperlib.MOUSE_LEFT:
        open_cover(grid_x, grid_y)
        if state["game_over"]:
            if state["game_win"]:
                put_flags()
            save_stats(stats)

    # Up/down flag on covered tile
    elif button == sweeperlib.MOUSE_RIGHT:
        switch_flag(grid_x, grid_y)

def open_cover(x, y):
    """
    Open covered tile without flag.
    """
    if state["cover"][y][x] == " ":
        state["turns"] += 1
        # Tile with mine was opened -> player loses
        if state["field"][y][x] == "x":
            open_mines()
            state["game_over"] = True
            state["game_win"] = False
        else:
            floodfill(x, y)
            # All tiles without mines were opened -> player wins
            if state["closed_count"] == 0:
                state["game_over"] = True
                state["game_win"] = True

def put_flags():
    """
    If player wins, but doesn't flag all the mines - we'll do it for him
    """
    for y in range(state["height"]):
        for x in range(state["width"]):
            if state["field"][y][x] == "x" and state["cover"][y][x] != "f":
                switch_flag(x, y)

def switch_flag(x, y):
    """
    Up/down flag on covered tile.
    """
    if state["cover"][y][x] == " ":
        state["cover"][y][x] = "f"
    elif state["cover"][y][x] == "f":
        state["cover"][y][x] = " "

def open_mines():
    """
    Open all mines if game lose, except flagged ones.
    """
    for y in range(state["height"]):
        for x in range(state["width"]):
            if state["field"][y][x] == "x" and state["cover"][y][x] != "f":
                state["cover"][y][x] = 0

def floodfill(x, y):
    """
    Open all neighbours around empty tile, starting from the given x, y coordinates.
    """
    queue = [(x, y)]
    while queue:
        current_x, current_y = queue.pop()
        # Skip already opened
        if state["cover"][current_y][current_x] == 0:
            continue
        state["cover"][current_y][current_x] = 0
        state["closed_count"] -= 1
        # Skip all numbers
        if state["field"][current_y][current_x] != 0:
            continue
        # Add to queue all covered neighbours without mines
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = current_x + dx, current_y + dy
                if 0 <= nx < state["width"] and 0 <= ny < state["height"]:
                    if state["cover"][ny][nx] == " " and state["field"][ny][nx] != "x":
                        queue.append((nx, ny))

def showmenu():
    print(" ")
    print("        ,--.!,         Welcome to")
    print("     __/   -*-      Minesweeper game!")
    print("   ,d08b.  '|`    [S]tart new game")
    print("   0088MM        [V]iew statistics")
    print("   `9MMP'       [Q]uit")

if __name__ == "__main__":
    stats = load_stats()
    while True:
        showmenu()
        choice = input("Choose something: ").strip().lower()
        if choice == "s":
            init_game()
            place_mines()
            start_game()
        elif choice == "v":
            view_stats(stats)
        elif choice == "q":
            break
        else:
            print("The chosen feature is not available.")

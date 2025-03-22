import random
import sys
import time
import turtle as t

WIDTH = 800
HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

LEFT = 0
RIGHT = 1
TOP = 2
BOTTOM = 3

window = []
state = {
    "draw": False,
    "running": False
}


def create_window(title):
    """
    Creates a "window" where all user interface frames and elements are placed.
    In this approximation the window is just an empty list where frames are
    appended. This functin only clears an existing window list.
    """
    
    window.clear()
    return window
    
def create_frame(host, side=LEFT):
    """
    Creates a frame. This function cheats a bit and just pushes a new frame
    into the window regardless of what its parameters are. Therefore this
    library does not support frames within frames, or frames below other
    frames.
    """

    frame = []
    window.append(frame)
    return frame

def create_button(frame, label, action):
    """
    Creates a button by adding a dictionary that describes a button to the
    frame list. The button's position is calculated from the frame's index
    within the window, and the number of buttons already in the frame so that
    the width of the button becomes BUTTON_WIDTH units and height becomes 
    BUTTON_HEIGHT units.
    """
    
    left = window.index(frame) * BUTTON_WIDTH
    right = left + BUTTON_WIDTH
    top = len(frame) * BUTTON_HEIGHT
    bottom = top + BUTTON_HEIGHT
    frame.append({
        "left": left,
        "right": right,
        "top": top,
        "bottom": bottom,
        "label": label,
        "action": action
    })
    
def read_click():
    """
    Reads a mouse click. For now just generates a random point inside the
    window.
    """
    
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    return x, y
    
def detect_button(x, y, window):
    """
    Finds which button was clicked, if any. If the clicked point is inside
    a button's boundaries, the button's action function is called.
    """

    for frame in window:
        for button in frame:
            if button["left"] <= x <= button["right"]:
                if button["top"] <= y <= button["bottom"]:
                    function = button["action"]
                    function()
                    return
    
def start():
    """
    Reads clicks and checks if they hit a button. The loop is repeated as long
    as the state dictionary's "running" value is True. If drawing was enabled
    at startup, also draws the window and each clicked point.
    """

    state["running"] = True
    if state["draw"]:
        draw_window()
    while state["running"]:
        print(".", end="", flush=True)
        mouse_x, mouse_y = read_click()
        if state["draw"]:
            t.up()
            t.setx(mouse_x - WIDTH / 2)
            t.sety(HEIGHT / 2 - mouse_y)
            t.down()
            t.dot()
        detect_button(mouse_x, mouse_y, window)
        # added to prevent the program from running too fast    
        time.sleep(0.1)
    if state["draw"]:
        t.done()
        
def quit():
    """
    Sets the state dictionary's "running" flag to False, which ends the loop
    inside the start function.    
    """
    
    state["running"] = False
    
def draw_window():
    """
    Uses turtle to draw a picture of the window.
    """
    
    t.up()
    t.setx(-1 * WIDTH / 2)
    t.sety(HEIGHT / 2)
    t.down()
    t.forward(WIDTH)
    t.right(90)
    t.forward(HEIGHT)
    t.right(90)
    t.forward(WIDTH)
    t.right(90)
    t.forward(HEIGHT)
    t.right(90)
    for frame in window:
        for button in frame:
            t.up()
            t.setx(button["left"] - WIDTH / 2)
            t.sety(HEIGHT / 2 - button["top"])
            t.down()
            t.forward(BUTTON_WIDTH)
            t.right(90)
            t.forward(BUTTON_HEIGHT)
            t.right(90)
            t.forward(BUTTON_WIDTH)
            t.right(90)
            t.forward(BUTTON_HEIGHT)
            t.right(90)
    
try:
    if sys.argv[1].lower() in ["-d", "--draw"]:
        state["draw"] = True
except IndexError:
    pass

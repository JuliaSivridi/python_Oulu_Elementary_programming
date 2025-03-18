import sweeperlib

def handle_mouse(x, y, button, modifiers):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    
    :param int x: x-coordinate of the mouse click
    :param int y: y-coordinate of the mouse click
    :param int button: mouse button clicked (use sweeperlib constants)
    :param int modifiers: modifier keys (not used in this exercise)
    """
    # Dictionary to map mouse button constants to their names
    button_names = {
        sweeperlib.MOUSE_LEFT: "left",
        sweeperlib.MOUSE_MIDDLE: "middle",
        sweeperlib.MOUSE_RIGHT: "right"
    }
    
    # Get the button name from the dictionary
    button_name = button_names.get(button, "unknown")
    
    # Print the mouse position and button clicked
    print(f"The {button_name} mouse button was pressed at {x}, {y}")

def main():
    """
    Creates a game window and sets a handler for mouse clicks.
    Starts the game.
    """
    # Create a window with a size of 800x600 pixels
    sweeperlib.create_window(width=800, height=600)
    
    # Set the mouse click handler
    sweeperlib.set_mouse_handler(handle_mouse)
    
    # Start the game
    sweeperlib.start()

if __name__ == "__main__":
    main()

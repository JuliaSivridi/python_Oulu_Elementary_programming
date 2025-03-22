import guilib as ui

def show_help():
    """
    Shows instructions to the user
    """

    ui.open_msg_window(
        "Instructions",
        "This program only includes this help text at the moment..."
    )

def create_window():
    window = ui.create_window("Amazing Program")
    frame = ui.create_frame(window, ui.TOP)
    button = ui.create_button(frame, "Help", show_help)
    ui.start()

if __name__ == "__main__":
    create_window()

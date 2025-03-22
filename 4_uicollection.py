import json
import guilib as ui
import sniffer

NOT_SELECTED = 0
ADD = 1
EDIT = 2

components = {
    "listbox": None,
    "album_form": None,
    "form_artist": None,
    "form_album": None,
    "form_no_tracks": None,
    "form_length": None,
    "form_year": None
}

state = {
    "collection": [],
    "action": NOT_SELECTED
}

def prompt_number(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Input an integer")
        else:
            return number

def prompt_time(prompt):
    while True:
        parts = input(prompt).split(":")
        if len(parts) == 3:
            h, min, s = parts
        elif len(parts) == 2:
            min, s = parts
            h = "0"
        else:
            print("Input the time as hours:minutes:seconds or minutes:seconds")
            continue

        try:
            h = int(h)
            min = int(min)
            s = int(s)
        except ValueError:
            print("Times must be integers")
            continue

        if not (0 <= min <= 59):
            print("Minutes must be between 0 and 59")
            continue
        if not (0 <= s <= 59):
            print("Seconds must be between 0 and 59")
            continue
        if h < 0:
            print("Hours must be a positive integer")
            continue

        return f"{h}:{min:02}:{s:02}"

def check_length(value):
    return value

def select_artist(album):
    return album["artist"]

def select_title(album):
    return album["album"]

def select_no_tracks(album):
    return album["no_tracks"]

def select_length(album):
    return album["length"]

def select_year(album):
    return album["year"]

def load_collection(filename):
    try:
        with open(filename) as source:
            state["collection"] = json.load(source)
    except (IOError, json.JSONDecodeError):
        print("Unable to open the target file. Starting with an empty collection.")
        state["collection"] = []

def save_collection(collection, filename):
    try:
        with open(filename, "w") as target:
            json.dump(collection, target)
    except IOError:
        print("Unable to open the target file. Saving failed.")

def read_form(album):
    album["artist"] = ui.read_field(components["form_artist"])
    album["album"] = ui.read_field(components["form_album"])
    try:
        album["no_tracks"] = int(ui.read_field(components["form_no_tracks"]))
    except ValueError:
        ui.open_msg_window("Error in data", "Number of tracks must be an integer", error=True)
        return None

    try:
        album["length"] = check_length(ui.read_field(components["form_no_tracks"]))
    except ValueError:
        ui.open_msg_window("Error in data", "Length must be written as HH:MM:SS", error=True)
        return None

    try:
        album["year"] = int(ui.read_field(components["form_year"]))
    except ValueError:
        ui.open_msg_window("Error in data", "Release year must be an integer", error=True)
        return None

    return album

def edit(collection, index):
    album = read_form(collection[index].copy())
    if album:
        collection[index] = album
        return True
    return False

def add(collection):
    album = read_form({})
    if album:
        collection.append(album)
        return True
    return False

def remove():
    index, contents = ui.read_selected(components["listbox"])
    if index != None:
        state["collection"].pop(index)
        ui.remove_list_row(components["listbox"], index)

def edit_fields(album):
    print("Current information:")
    print("{artist}, {album}, {no_tracks}, {length}, {year}".format(**album))
    print("Choose a field to edit by entering its number. Leave empty to stop.")
    print("1 - artist")
    print("2 - album title")
    print("3 - number of tracks")
    print("4 - album length")
    print("5 - release year")
    while True:
        field = input("Select field (1-5): ")
        if not field:
            break
        elif field == "1":
            album["artist"] = input("Artist name: ")
        elif field == "2":
            album["album"] = input("Album title: ")
        elif field == "3":
            album["no_tracks"] = prompt_number("Number of tracks: ")
        elif field == "4":
            album["length"] = prompt_time("Album length: ")
        elif field == "5":
            album["year"] = prompt_number("Release year: ")
        else:
            print("Field does not exist")            

def show(collection):
    for i, album in enumerate(collection):
        ui.add_list_row(components["listbox"], format_row(album, i + 1))

def format_row(album, i):
    return (
        f"{i:2}. "
        f"{album['artist']} - {album['album']} ({album['year']}) "
        f"[{album['no_tracks']}] [{album['length'].lstrip('0:')}]"
    )

def organize(collection):
    print("Choose a field to use for sorting the collection by inputting the corresponding number")
    print("1 - artist")
    print("2 - album title")
    print("3 - number of tracks")
    print("4 - album length")
    print("5 - release year")
    field = input("Choose field  (1-5): ")
    order = input("Order; (a)scending or (d)escending: ").lower()
    if order == "d":
        reverse = True
    else:
        reverse = False
    if field == "1":
        collection.sort(key=select_artist, reverse=reverse)
    elif field == "2":
        collection.sort(key=select_title, reverse=reverse)
    elif field == "3":
        collection.sort(key=select_no_tracks, reverse=reverse)
    elif field == "4":
        collection.sort(key=select_length, reverse=reverse)
    elif field == "5":
        collection.sort(key=select_year, reverse=reverse)
    else:
        print("Field doesn't exist")

def construct_collection(folder):
    try:
        components["collection"] = sniffer.read_collection(folder)
    except FileNotFoundError:
        print("Folder not found")

def read_arguments(arguments):
    if len(arguments) >= 3:
        source = arguments[1]
        target = arguments[2]
        return source, target
    elif len(arguments) == 2:
        source = arguments[1]
        return source, source
    else:
        return None, None

def open_load_window():
    path = ui.open_file_dialog("Select collection file (JSON)")
    load_collection(path)
    show(state["collection"])

def open_save_window():
    path = ui.open_save_dialog("Choose filename (JSON)")
    save_collection(state["collection"], path)

def open_construct_window():
    path = ui.open_folder_dialog("Select music collection root folder")
    construct_collection(path)
    show(state["collection"])

def open_add_window():
    ui.show_subwindow(components["album_form"])
    state["action"] = ADD

def open_edit_window():
    place = prefill_form()
    ui.show_subwindow(components["album_form"])
    state["action"] = EDIT
    state["selected"] = place

def save_form():
    if state["action"] == ADD:
        success = add(state["collection"])
        place = len(state["collection"]) - 1
    elif state["action"] == EDIT:
        place = state["selected"]
        success = edit(state["collection"], place)
        if success:
            ui.remove_list_row(components["listbox"], place)
            state["selected"] = None
    else:
        return

    if success:
        ui.add_list_row(
            components["listbox"],
            format_row(state["collection"][place], place + 1),
            place
        )
        ui.clear_field(components["form_artist"])
        ui.clear_field(components["form_album"])
        ui.clear_field(components["form_no_tracks"])
        ui.clear_field(components["form_length"])
        ui.clear_field(components["form_year"])    
        ui.hide_subwindow(components["album_form"])
        state["action"] = NOT_SELECTED

def prefill_form():
    index, contents = ui.read_selected(components["listbox"])
    album = state["collection"][index]
    ui.write_field(components["form_artist"], album["artist"])
    ui.write_field(components["form_album"], album["album"])
    ui.write_field(components["form_no_tracks"], album["no_tracks"])
    ui.write_field(components["form_length"], album["length"])
    ui.write_field(components["form_year"], album["year"])
    return index

def quit():
    ui.quit()

def create_window():
    # Main window creation
    window = ui.create_window("Collection Manager 0.1 alpha")
    button_frame = ui.create_frame(window, ui.LEFT)
    collection_frame = ui.create_frame(window, ui.LEFT)
    ui.create_button(button_frame, "Load", open_load_window)
    ui.create_button(button_frame, "Construct", open_construct_window)
    ui.create_button(button_frame, "Save", open_save_window)
    ui.create_horiz_separator(button_frame, 5)
    ui.create_button(button_frame, "Add", open_add_window)
    ui.create_button(button_frame, "Remove", remove)
    ui.create_button(button_frame, "Edit", open_edit_window)
    ui.create_horiz_separator(button_frame, 5)
    ui.create_button(button_frame, "Quit", quit)
    components["listbox"] = ui.create_listbox(collection_frame)

    # Subwindow creation
    album_form = ui.create_subwindow("Album information")
    field_frame = ui.create_frame(album_form, ui.TOP)
    button_frame = ui.create_frame(album_form, ui.TOP)
    label_frame = ui.create_frame(field_frame, ui.LEFT)
    input_frame = ui.create_frame(field_frame, ui.LEFT)
    ui.create_label(label_frame, "Artist")
    components["form_artist"] = ui.create_textfield(input_frame)
    ui.create_label(label_frame, "Album")
    components["form_album"] = ui.create_textfield(input_frame)
    ui.create_label(label_frame, "No. tracks")
    components["form_no_tracks"] = ui.create_textfield(input_frame)
    ui.create_label(label_frame, "Length")
    components["form_length"] = ui.create_textfield(input_frame)
    ui.create_label(label_frame, "Release year")
    components["form_year"] = ui.create_textfield(input_frame)
    ui.create_button(button_frame, "Save", save_form)
    ui.hide_subwindow(album_form)
    components["album_form"] = album_form
    ui.start()

if __name__ == "__main__":
    #source, target = read_arguments(sys.argv)
    try:
        create_window()
    except KeyboardInterrupt:
        print("Program was interrupted, collection was not saved.")

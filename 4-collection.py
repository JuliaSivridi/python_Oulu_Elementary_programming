import json
import math

PER_PAGE = 5

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

        return "{}:{:02}:{:02}".format(h, min, s)

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

def read_row(row, collection):
    try:
        artist, album, no_tracks, length, year = row.split(",")
        newalbum = {
            "artist": artist.strip(),
            "album": album.strip(),
            "no_tracks": int(no_tracks),
            "length": length.strip(),
            "year": int(year)
        }
        collection.append(newalbum)
    except ValueError:
        print(f"Unable to read row: {row}")

def load_collection(filename):
    # The order of values in each row corresponds to dictionary keys:
    # 1. "artist" - artist name
    # 2. "album" - album title
    # 3. "no_tracks" - number of tracks
    # 4. "length" - album length
    # 5. "year" - release year
    collection = []
    try:
        with open(filename) as source:
            for row in source.readlines():
                read_row(row, collection)
    except IOError:
        print("Unable to open the target file. Starting with an empty collection.")
    return collection

def save_collection(collection, filename):
    try:
        with open(filename, "w") as target:
            for i, album in enumerate(collection):
                target.write(
                    f"{album['artist']}, {album['album']}, {album['no_tracks']}, "
                    f"{album['length'].lstrip('0:')}, {album['year']}\n"
                )
    except IOError:
        print("Unable to open the target file. Saving failed.")

def add(collection):
    print("Fill the information for a new album. Leave album title empty to stop.")
    while True:
        title = input("Album name: ")
        if not title:
            break

        artist = input("Artist name: ")
        no_tracks = prompt_number("Number of tracks: ")
        length = prompt_time("Total length: ")
        year = prompt_number("Release year: ")
        collection.append({
            "artist": artist,
            "album": title,
            "no_tracks": no_tracks,
            "length": length,
            "year": year
        })
        print("Album added")

def remove(collection):
    print("Fill in the album title and artist name to select which album to remove")
    print("Leave album title empty to quit")
    while True:
        title = input("Album title: ").lower()
        if not title:
            break

        artist = input("Artist name: ").lower()
        for album in collection[:]:
            if album["artist"].lower() == artist and album["album"].lower() == title:
                collection.remove(album)
                print("Album removed")

def edit(collection):
    print("Fill in the album title and artist name to select which album to edit")
    print("Leave album title empty to quit")
    while True:
        title = input("Album title: ").lower()
        if not title:
            break

        artist = input("Artist name: ").lower()
        for album in collection[:]:
            if album["artist"].lower() == artist and album["album"].lower() == title:
                edit_fields(album)
                print("Album edited")

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
    pages = math.ceil(len(collection) / PER_PAGE)
    for i in range(pages):
        start = i * PER_PAGE
        end = (i + 1) * PER_PAGE
        format_page(collection[start:end], i)
        if i < pages - 1:
            input("   -- press enter to continue --")

def format_page(lines, page_n):
    for i, album in enumerate(lines, page_n * PER_PAGE + 1):
        print(
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

collection = load_collection("collection.txt")
print("This program manages an album collection. You can use the following features:")
print("(A)dd new albums")
print("(E)dit albums")
print("(R)emove albums")
print("(S)how the collection")
print("(O)rganize the collection")
print("(Q)uit")
while True:
    choice = input("Make your choice: ").strip().lower()
    if choice == "a":
        add(collection)
    if choice == "e":
        edit(collection)
    elif choice == "r":
        remove(collection)
    elif choice == "s":
        show(collection)
    elif choice == "o":
        organize(collection)
    elif choice == "q":
        break
    else:
        print("The chosen feature is not available.")
save_collection(collection, "collection.txt")

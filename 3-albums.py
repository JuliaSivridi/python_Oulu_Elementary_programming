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

        return f"{h}:{min:02}:{s:02}"

def load_collection():
    """
    Creates a test collection. Returns a list that contains dictionaries of
    five key-value pairs.
    Dictionary keys match the following information:
    "artist" - name of the album artist
    "album" - title of the album
    "no_tracks" - number of tracks
    "length" - total length
    "year" - release year
    """

    collection = [
        {
            "artist": "Alcest",
            "album": "Kodama",
            "no_tracks": 6,
            "length": "42:15",
            "year": 2016
        },
        {
            "artist": "Canaan",
            "album": "A Calling to Weakness",
            "no_tracks": 17,
            "length": "1:11:17",
            "year": 2002
        },
        {
            "artist": "Deftones",
            "album": "Gore",
            "no_tracks": 11,
            "length": "48:13",
            "year": 2016
        },
        {
            "artist": "Funeralium",
            "album": "Deceived Idealism",
            "no_tracks": 6,
            "length": "1:28:22",
            "year": 2013
        },
        {
            "artist": "IU",
            "album": "Modern Times",
            "no_tracks": 13,
            "length": "47:14",
            "year": 2013
        },
        {
            "artist": "Mono",
            "album": "You Are There",
            "no_tracks": 6,
            "length": "1:00:01",
            "year": 2006
        },
        {
            "artist": "Panopticon",
            "album": "Roads to the North",
            "no_tracks": 8,
            "length": "1:11:07",
            "year": 2014
        },
        {
            "artist": "PassCode",
            "album": "Clarity",
            "no_tracks": 13,
            "length": "49:27",
            "year": 2019
        },
        {
            "artist": "Scandal",
            "album": "Hello World",
            "no_tracks": 13,
            "length": "53:22",
            "year": 2014
        },
        {
            "artist": "Slipknot",
            "album": "Iowa",
            "no_tracks": 14,
            "length": "1:06:24",
            "year": 2001
        },
        {
            "artist": "Wolves in the Throne Room",
            "album": "Thrice Woven",
            "no_tracks": 5,
            "length": "42:19",
            "year": 2017
        },
    ]
    return collection

def save_collection(collection):
    pass

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
    pass

def format_page(lines, page_no):
    for i, album in enumerate(lines, page_no * PER_PAGE + 1):
        print("{i:2}. {artist} - {album} ({year}) [{tracks}] [{length}]".format(
            i=i,
            artist=album["artist"],
            album=album["album"],
            tracks=album["no_tracks"],
            length=album["length"].lstrip("0:"),
            year=album["year"]
        ))

def show(collection):
    pages = math.ceil(len(collection) / PER_PAGE)
    for i in range(pages):
        start = i * PER_PAGE
        end = (i + 1) * PER_PAGE
        format_page(collection[start:end], i)
        if i < pages - 1:
            input("   -- press enter to continue --")

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

collection = load_collection()
print("This program manages an album collection. You can use the following features:")
print("(A)dd new albums")
print("(R)emove albums")
print("(S)how the collection")
print("(O)rganize the collection")
print("(Q)uit")
while True:
    choice = input("Make your choice: ").strip().lower()
    if choice == "a":
        add(collection)
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
save_collection(collection)

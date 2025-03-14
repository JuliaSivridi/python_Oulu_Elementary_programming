import os
import tinytag

def read_folder(folder, collection):
    print("Opening folder:", folder)
    contents = os.listdir(folder)
    for name in contents:
        path = os.path.join(folder, name)
        if os.path.isdir(path):
            read_folder(path, collection)
        else:
            try:
                read_metadata(path, collection)
            except tinytag.TinyTagException:
                print("Skipping", name)
    
def read_metadata(filename, collection):
    tag = tinytag.TinyTag.get(filename)
    title = tag.album
    artist = tag.artist
    year = tag.year
    length = tag.duration
    for album in collection:
        if album["artist"].lower() == artist.lower() and album["album"].lower() == title.lower():
            album["lengths"].append(length)
            break
    else:
        collection.append({
            "artist": artist.strip(),
            "album": title.strip(),
            "lengths": [],
            "year": int(year)
        })
        
def parse_lenghts(collection):
    for album in collection:
        album["length"] = time.strftime("%H:%M:%S", time.gmtime(sum(album["lengths"])))
        album["no_tracks"] = len(album["lengths"])
        album.pop("lengths")
        
def read_collection(folder):
    collection = []
    read_folder(folder, collection)
    parse_lenghts(collection)
    return collection
            


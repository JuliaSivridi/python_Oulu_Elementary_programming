ANIMALS = {
    "s": "sloth",
    "d": "doggo",
    "@": "cat",
    "m": "moogle",
    "c": "chocobo"
}

def explore_tile(tile, row, col):
    """
    Explore a tile - if there is an animal, prints the
    location and name of the animal
    """
    if tile in ANIMALS:
        print(f"Tile ({col}, {row}) contains {ANIMALS[tile]}")

def explore_field(efield):
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field.
    """
    for er, erow in enumerate(efield):
        for ec, etile in enumerate(erow):
            explore_tile(etile, er, ec)

field = [
    [" ", "s", " ", " ", "m"],
    [" ", "d", "@", "d", " "],
    ["c", " ", "s", "d", " "]
]
explore_field(field)

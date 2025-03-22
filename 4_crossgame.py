import math
import random
import pyglet
import sweeperlib

WIDTH = 800
HEIGHT = 600
ANIM_SPEED = 0.1

state = {
    "player": {
        "x": 40,
        "y": 40,
        "heading": 0,
        "speed": 0,
        "accel": 0,
        "sprite": 0
    }
}

def load_sprites(path):
    pyglet.resource.path = [path]
    sprites = {
        "0": pyglet.resource.image("plus_1.png"),
        "1": pyglet.resource.image("plus_2.png")
    }
    sweeperlib.graphics["images"] = sprites
    
def create_player():
    state["player"] = {
        "x": random.randint(0, WIDTH - 1),
        "y": random.randint(0, HEIGHT - 1),
        "heading": 0,
        "speed": 0,
        "accel": 0.2,
        "sprite": 0
    }

def convert_to_xy(a, r):
    x = int(round(math.cos(a) * r))
    y = int(round(math.sin(a) * r))
    return x, y    
    
def set_heading(character, target_x, target_y):
    distance_x = target_x - character["x"]
    distance_y = target_y - character["y"]
    character["heading"] = math.degrees(math.atan2(distance_y, distance_x))
    
def update_position(char):
    dx, dy = convert_to_xy(math.radians(char["heading"]), char["speed"])
    char["x"] += dx
    char["y"] += dy

def handle_mouse(x, y, button, modifiers):
    set_heading(state["player"], x, y)
    state["player"]["speed"] = 0
    print(state["player"])

def update_game(elapsed):
    state["player"]["speed"] += state["player"]["accel"]
    state["player"]["sprite"] = (state["player"]["sprite"] + ANIM_SPEED) % 2
    update_position(state["player"])
    
def draw_game():
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()
    sweeperlib.prepare_sprite(int(state["player"]["sprite"]), state["player"]["x"], state["player"]["y"])
    sweeperlib.draw_sprites()
    
def start_game():
    create_player()
    sweeperlib.create_window(WIDTH, HEIGHT)
    sweeperlib.set_draw_handler(draw_game)
    sweeperlib.set_mouse_handler(handle_mouse)
    sweeperlib.set_interval_handler(update_game)
    sweeperlib.start()
    
if __name__ == "__main__":
    load_sprites("sprites")
    start_game()
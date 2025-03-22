import library

def print_donkey():
    print("donkey")
    
def print_hemulen():
    print("hemulen")

window = library.create_window("test")
frame = library.create_frame(window)
library.create_button(frame, "button 1", print_donkey)
library.create_button(frame, "button 2", print_hemulen)
library.create_button(frame, "quit", library.quit)
library.start()
print("so long, and thanks for all the fish")

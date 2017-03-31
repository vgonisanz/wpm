import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from button import Button

# Configuration
button_message = "Normal"
button_message_inactive = "Inactive"
button_message_focus = "Focus"
button_message_pushed = "Pushed"

button_width = 10
button_x0 = 1
button_y0 = 2

# Variables
wpm = None
background = None
button_normal = None
button_inactive = None
button_focus = None
button_pushed = None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()   # Get main window to print
    return None

def draw_buttons():
    global button_normal
    global button_inactive
    global button_focus
    global button_pushed

    current_y = button_y0

    background.print_message("This is a %s button" % button_message, button_x0, current_y)
    current_y += 1
    button_normal = Button(button_message, button_width, button_x0, current_y)
    button_normal.draw()

    current_y += 2
    background.print_message("This is a %s button" % button_message_inactive, button_x0, current_y)
    current_y += 1
    button_inactive = Button(button_message_inactive, button_width, button_x0, current_y)
    button_inactive.set_active(False)
    button_inactive.draw()

    current_y += 2
    background.print_message("This is a %s button" % button_message_focus, button_x0, current_y)
    current_y += 1
    button_focus = Button(button_message_focus, button_width, button_x0, current_y)
    button_focus.set_focus()
    button_focus.draw()

    current_y += 2
    background.print_message("This is a %s button" % button_message_pushed, button_x0, current_y)
    current_y += 1
    button_pushed = Button(button_message_pushed, button_width, button_x0, current_y)
    button_pushed.push()
    button_pushed.draw()

    background.waitforkey()
    return None

def change_palette():
    button_focus.change_color(curses.COLOR_GREEN, curses.COLOR_BLACK)
    background.waitforkey()
    return None

def clean_and_update_normal_button():
    background.clear()
    background.print_message("Now we clean and redraw normal button", button_x0, button_y0)
    button_normal.draw()
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    draw_buttons()
    #change_palette() #Todo check colors crossplatform
    clean_and_update_normal_button()

    #
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

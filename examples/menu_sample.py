import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from menu import Menu

# Configuration
menu_width = 30
menu_height = 10
menu_x0 = 5
menu_y0 = 5
menu_title = "This is your First Menu"
menu_options = [ "Option 0", "Option 1", "Option 2", "Option 3", "Option 4" ] # Change option list for object with callbacks
menu_centered = True

# Variables
wpm = None
background = None
menu = None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()
    return None

def create_menu():
    global menu

    # Create test menu and run
    menu = Menu(menu_width, menu_height, menu_x0, menu_y0, menu_title, menu_options)
    menu.set_centered(menu_centered)
    option_index = menu.run()

    background.clear()
    background.print_message("You choose option: %s" % option_index)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    #print_help()
    create_menu()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

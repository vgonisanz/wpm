import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from menu import Menu
from optionstruct import OptionStruct

# Configuration
menu_width = 30
menu_height = 10
menu_x0 = 5
menu_y0 = 5
menu_title = "This is your First Menu"
#menu_options = [ "Option 0", "Option 1", "Option 2", "Option 3", "Option 4" ] # Change option list for object with callbacks
menu_centered = True

# Variables
wpm = None
background = None
menu = None

def callback_hello():
    background.print_message("Hello")
    #background.waitforkey()
    return None

def callback_print(message):
    background.print_message(message)
    #background.waitforkey()
    return None

def callback_quit():
    menu.callback_quit()
    return None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()
    return None

def create_menu():
    global menu

    option_0 = OptionStruct("Option 0", callback_hello)
    option_1 = OptionStruct("Option 1", callback_print, "Hello world")
    option_2 = OptionStruct("Option 2, do nothing")
    option_3 = OptionStruct("Option 3, me neither")
    option_4 = OptionStruct("Option quit", callback_quit)

    # Create test menu and run
    menu = Menu(menu_width, menu_height, menu_x0, menu_y0, menu_title, "Use arrows")
    menu.set_centered(menu_centered)
    menu.add_option(option_0)
    menu.add_option(option_1)
    menu.add_option(option_2)
    menu.add_option(option_3)
    menu.add_option(option_4)

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

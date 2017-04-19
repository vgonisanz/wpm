# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from toggle_table import ToggleTable

# Configuration
toggletable_width = 30
toggletable_height = 10
toggletable_x0 = 1
toggletable_y0 = 2

# Variables
wpm = None
background = None

def initialize():
    global wpm
    global background

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    background = wpm.get_screen()   # Get main window to print
    return None

def draw_toggletable():

    background.print_message("This is a toggle table:")
    toggletable = ToggleTable(toggletable_width, toggletable_height, toggletable_x0, toggletable_y0)
    toggletable.set(0, 0)
    toggletable.set(2, 3)
    toggletable.set(2, 4)
    toggletable.draw()
    #toggletable.print_border_type()

    background.waitforkey()
    return None

def draw_random_toggletable():
    background.clear()
    background.print_message("This is a toggle table generated randomly")
    toggletable = ToggleTable(toggletable_width, toggletable_height, toggletable_x0, toggletable_y0)
    toggletable.generate_random_table()
    toggletable.draw()

    background.waitforkey()
    return None

def run_toggletable_widget():

    return None

def main(stdscr):
    initialize()
    draw_toggletable()
    draw_random_toggletable()
    run_toggletable_widget()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

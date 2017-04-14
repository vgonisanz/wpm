import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from toggle_board import ToggleBoard

# Configuration
toggleboard_width = 50
toggleboard_height = 30
toggleboard_message = "q to quit"

# Variables
wpm = None
toggleboard = None
toggleboard_foreground = None

def initialize():
    global wpm

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    return None

def create_toggleboard():
    global toggleboard
    global toggleboard_foreground

    # Calculate center of screen
    window_width, window_height = wpm.get_window_size()
    toggleboard_x0 = int(window_width/2-toggleboard_width/2)
    toggleboard_y0 = int(window_height/2-toggleboard_height/2)

    # toggleboard with title
    toggleboard = ToggleBoard(toggleboard_width, toggleboard_height, toggleboard_x0, toggleboard_y0, True)
    toggleboard_foreground = toggleboard.get_foreground()

    #toggleboard.set_message(toggleboard_message, True)
    wpm.set_cursor_mode(2)
    toggleboard.run()
    return None

def main(stdscr):
    initialize()
    create_toggleboard()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

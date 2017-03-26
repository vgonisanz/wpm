import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from button import Button

# Configuration

# Variables

def main(stdscr):
    wpm = Wpm()

    # Create button element
    button_message = "12345678910"
    button_width = 10
    button_x0 = 1
    button_y0 = 2

    button = Button(button_message, button_width, button_x0, button_y0)
    button.change_color(curses.COLOR_RED, curses.COLOR_YELLOW)
    button.draw()

    wpm.msleep(2000)
    background.waitforkey(True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

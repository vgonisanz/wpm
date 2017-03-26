import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration

# Variables

def main(stdscr):
    wpm = Wpm()
    background = wpm.get_background()

    x0 = 1
    y0 = 1
    current_y = y0

    # Initial message
    background.print_message("In this sample we are going to print messages.", x0, current_y)
    background.waitforkey(True)
    background.clear()

    # Different attributes message
    current_y = y0
    background.print_message("Attribute:", x0, current_y)
    current_y += 1
    background.print_message("A_ALTCHARSET", x0, current_y, curses.A_ALTCHARSET)
    current_y += 1
    background.print_message("A_BLINK", x0, current_y, curses.A_BLINK)
    current_y += 1
    background.print_message("A_BOLD", x0, current_y, curses.A_BOLD)
    current_y += 1
    background.print_message("A_DIM", x0, current_y, curses.A_DIM)
    current_y += 1
    background.print_message("A_NORMAL", x0, current_y, curses.A_NORMAL)
    current_y += 1
    background.print_message("A_REVERSE", x0, current_y, curses.A_REVERSE)
    current_y += 1
    background.print_message("A_STANDOUT", x0, current_y, curses.A_STANDOUT)
    current_y += 1
    background.print_message("A_UNDERLINE", x0, current_y, curses.A_UNDERLINE)
    background.waitforkey(True)
    background.clear()

    # Change color character and background
    current_y = y0
    background.print_message("Last, You can change a concrete color from the pair palette, we change background color.", x0, current_y)
    background.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Modify to use a palette!
    background.waitforkey(True)
    background.clear()

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

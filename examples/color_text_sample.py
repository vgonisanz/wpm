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
    # TODO rework
    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))

    # Configure iterations
    color_to_print = wpm.get_max_custom_colors()
    custom_color = 2

    # Get main window to print
    background = wpm.get_background()
    background.print_message("Character color will change every time you push a key. This terminal have: %d" % color_to_print, 1, 1)
    background.waitforkey()
    background.clearln(1)

    for x in range(1, color_to_print):
        background.change_color(x, 0)
        wpm.msleep(5)
        background.print_message("Color %d is this text color." % x, 1, 1)
        background.waitforkey()

    background.clear()

    background.print_message("Creating custom color RED: %d" % custom_color, 1, 1)
    try:
        curses.init_color(2, 1000, 0, 0)
    except:
        print("This terminal cannot init_color")
        pass

    background.waitforkey()

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

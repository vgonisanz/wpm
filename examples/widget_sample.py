import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from widget import Widget

# Configuration

# Variables

def main(stdscr):
    wpm = Wpm()
    background = wpm.get_background()

    # Create widget or widget here
    widget_width = 20
    widget_height = 10
    widget_x0 = 1
    widget_y0 = 2

    widget = Widget(widget_width, widget_height, widget_x0, widget_y0)
    widget.run_test()

    wpm.msleep(1)
    background.waitforkey(True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

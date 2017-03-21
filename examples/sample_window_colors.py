import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()

    # Configure iterations
    color_to_print = curses.COLORS

    # Get main window to print
    main_window = wpm.get_current_widget()
    wpm.print_message(main_window, "Character color will change every time you push a key.", 1, 1)
    wpm.waitforkey(main_window, True, 1, 2)
    wpm.clearln(main_window, 1)

    for x in range(1, color_to_print):
        wpm.print_background(main_window, x, 0)
        wpm.msleep(5)
        wpm.print_message(main_window, "Color %d is this text color." % x, 1, 1)
        wpm.waitforkey(main_window, True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use window color.")
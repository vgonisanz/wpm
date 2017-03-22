import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()

    # Configure iterations
    color_to_print = wpm.get_max_custom_colors()
    custom_color = 2

    # Get main window to print
    main_window = wpm.get_current_widget()
    wpm.print_message(main_window, "Character color will change every time you push a key. This terminal have: %d" % color_to_print, 1, 1)
    wpm.waitforkey(main_window, True, 1, 2)
    wpm.clearln(main_window, 1)

    for x in range(1, color_to_print):
        wpm.print_background(main_window, x, 0)
        wpm.msleep(5)
        wpm.print_message(main_window, "Color %d is this text color." % x, 1, 1)
        wpm.waitforkey(main_window, True, 1, 2)

    wpm.clear(main_window)

    wpm.print_message(main_window, "Creating custom color RED: %d" % custom_color, 1, 1)
    curses.init_color(2, 1000, 0, 0)
    wpm.waitforkey(main_window, True, 1, 2)

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use window color.")

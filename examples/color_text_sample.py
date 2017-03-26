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
    background = wpm.get_background()
    background.print_message("Character color will change every time you push a key. This terminal have: %d" % color_to_print, 1, 1)
    background.waitforkey()
    background.clearln(1)

    for x in range(1, color_to_print):
        background.change_color(x, 0)
        wpm.msleep(5)
        background.print_message("Color %d is this text color." % x, 1, 1)
        background.waitforkey(True, 1, 2)

    background.clear()

    background.print_message("Creating custom color RED: %d" % custom_color, 1, 1)
    try:
        curses.init_color(2, 1000, 0, 0)
    except:
        print("This terminal cannot init_color")
        pass

    background.waitforkey(background, True, 1, 2)

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use window color.")

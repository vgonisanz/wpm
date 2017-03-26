import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()

    # Get main window to print
    main_window = wpm.get_current_widget()

    # Initial message
    wpm.print_message(main_window, "In this sample we are going to print messages.")
    wpm.waitforkey(main_window, True)
    wpm.clear(main_window)

    # Change color character and background
    wpm.print_message(main_window, "But first, we change background color.")
    wpm.change_color(main_window, curses.COLOR_BLACK, curses.COLOR_WHITE)
    wpm.print_border(main_window)
    wpm.waitforkey(main_window, True)
    wpm.clear(main_window)


    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use window color.")

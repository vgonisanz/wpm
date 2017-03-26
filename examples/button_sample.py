import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

from element import Element
from button import Button

def main(stdscr):
    wpm = Wpm()
    main_window = wpm.get_current_widget()

    # Create button element
    button_message = "12345678910"
    button_width = 10
    button_x0 = 1
    button_y0 = 2

    button = Button(button_message, button_width, button_x0, button_y0)
    button.change_color(curses.COLOR_RED, curses.COLOR_YELLOW)
    button.draw()

    wpm.msleep(2000)
    wpm.waitforkey(main_window, True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use button sample")

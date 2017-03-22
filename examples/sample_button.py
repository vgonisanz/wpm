import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()
    main_window = wpm.get_current_widget()

    # Create button element
    button_message = "12345678910"
    button_width = 10
    button_x0 = 1
    button_y0 = 2
    button = wpm.create_element_button(button_message, button_width, button_x0, button_y0)

    # Print normal button
    wpm.print_message(main_window, "Button normal:", 1, 1, curses.A_NORMAL)
    button.draw()
    wpm.msleep(2000)
    wpm.waitforkey(main_window, True, 1, 2)

    # Print focus button
    ## TODO change status internal
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use button sample")

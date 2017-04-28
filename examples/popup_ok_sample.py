import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from popup_ok import PopupOk

# Configuration
popup_width = 30
popup_height = 10
popup_message = "Popup with ok button"

# Variables
wpm = None
screen = None
popup = None
popup_background = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()
    return None

def create_popup_ok():
    global popup
    global popup_background

    # Calculate center of screen
    window_width, window_height = wpm.get_window_size()
    popup_x0 = int(window_width/2-popup_width/2)
    popup_y0 = int(window_height/2-popup_height/2)

    # Popup with title
    popup = PopupOk(popup_width, popup_height, popup_x0, popup_y0, ord('q'), True)
    popup_background = popup.get_background()
    popup_background.print_border_type()
    popup.set_message(popup_message, True)
    popup.run()

    screen.clear()
    screen.print_message("Removed popup")
    screen.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_popup_ok()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

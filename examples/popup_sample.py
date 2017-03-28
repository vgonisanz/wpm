import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from popup import Popup

# Configuration
popup_width = 30
popup_height = 10
popup_message = "Pop-up say: press q to quit"

# Variables
wpm = None
popup = None
popup_background = None

def initialize():
    global wpm

    wpm = Wpm()
    return None

def create_popup():
    global popup
    global popup_background

    # Calculate center of screen
    window_width, window_height = wpm.get_window_size()
    popup_x0 = int(window_width/2-popup_width/2)
    popup_y0 = int(window_height/2-popup_height/2)

    # Popup with title
    popup = Popup(popup_width, popup_height, popup_x0, popup_y0, True)
    popup_background = popup.get_background()

    popup.set_message(popup_message)
    popup.run()
    return None

def main(stdscr):
    initialize()
    create_popup()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

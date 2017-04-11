import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from interface import Interface
from widget import EventObject

# Configuration
interface_title = "My first interface"
interface_print_title = True

# Variables
interface = None
interface_background = None

def initialize():
    global wpm

    wpm = Wpm()
    return None

def create_interface():
    global interface
    global interface_background

    # All screen widget
    interface_x0 = 0
    interface_y0 = 0
    interface_width, interface_height = wpm.get_window_size()

    interface = Interface(interface_width, interface_height, interface_x0, interface_y0, interface_title, interface_print_title)
    interface_background = interface.get_background()

    #widget_background.print_message("Push left, s, c, or q to quit.\n")

    #event_print = EventObject(curses.KEY_LEFT, callback_event_print, ["Left\n"])
    #event_clear = EventObject(ord('c'), callback_clear)
    #event_sum = EventObject(ord('s'), callback_sum, [ 4, 5 ])
    #event_quit = EventObject(ord('q'), callback_quit)

    #widget.add_event(event_print)
    #widget.add_event(event_clear)
    #widget.add_event(event_sum)
    #widget.add_event(event_quit)

    interface.run()
    return None

def main(stdscr):
    initialize()
    create_interface()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from widget import Widget
from widget import ActionObject

# Configuration
widget_width = 20
widget_height = 10
widget_x0 = 1
widget_y0 = 2

# Variables
widget = None
widget_background = None

def callback_action1():
    widget_background.print_message("Left")
    return None

def callback_c():
    widget_background.print_message("c")
    return None

def callback_quit():
    widget.end_condition()
    return None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()   # Get main window to print
    return None

def create_widget():
    global widget
    global widget_background

    widget = Widget(widget_width, widget_height, widget_x0, widget_y0)
    widget_background = widget.get_background()

    action_c = ActionObject(ord('c'), callback_c)
    action_quit = ActionObject(ord('q'), callback_quit)
    action1 = ActionObject(curses.KEY_LEFT, callback_action1)

    widget.add_event(action1)
    widget.add_event(action_quit)
    widget.add_event(action_c)

    widget.run()
    return None



def main(stdscr):
    initialize()
    create_widget()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

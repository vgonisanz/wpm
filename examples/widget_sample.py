import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from widget import Widget
from widget import EventObject

# Configuration
widget_width = 30
widget_height = 20
widget_x0 = 1
widget_y0 = 2

# Variables
widget = None
widget_background = None

def callback_event_print(message):
    widget_background.print_message(message)
    return None

def callback_clear():
    widget_background.clear()
    return None

def callback_sum(a, b):
    widget_background.print_message("a + b = %s\n" % str(a + b) )
    return None

def callback_quit():
    widget.end_condition()
    return None

def initialize():
    global wpm

    wpm = Wpm()
    return None

def create_widget():
    global widget
    global widget_background

    widget = Widget(widget_width, widget_height, widget_x0, widget_y0)
    widget_background = widget.get_background()

    widget_background.print_message("Push left, s, c, or q to quit.\n")

    event_print = EventObject(curses.KEY_LEFT, callback_event_print, ["Left\n"])
    event_clear = EventObject(ord('c'), callback_clear)
    event_sum = EventObject(ord('s'), callback_sum, [ 4, 5 ])
    event_quit = EventObject(ord('q'), callback_quit)

    widget.add_event(event_print)
    widget.add_event(event_clear)
    widget.add_event(event_sum)
    widget.add_event(event_quit)

    widget.run()
    return None

def change_widget_events():
    widget.purge_events()

    widget_background.clear()
    widget_background.print_message("Push directions, or q to quit.\n")

    event_print_left = EventObject(curses.KEY_LEFT, callback_event_print, ["Left\n"])
    event_print_right = EventObject(curses.KEY_RIGHT, callback_event_print, ["Right\n"])
    event_print_up = EventObject(curses.KEY_UP, callback_event_print, ["Up\n"])
    event_print_down = EventObject(curses.KEY_DOWN, callback_event_print, ["Down\n"])
    event_quit = EventObject(ord('q'), callback_quit)

    widget.add_event(event_print_left)
    widget.add_event(event_print_right)
    widget.add_event(event_print_up)
    widget.add_event(event_print_down)
    widget.add_event(event_quit)

    widget.run()
    return None

def main(stdscr):
    initialize()
    create_widget()
    change_widget_events()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

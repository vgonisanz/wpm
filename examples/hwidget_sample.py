import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from hwidget import HWidget
from widget import EventObject

# Configuration
widget_width = 50
widget_height = 30
widget_x0 = 1
widget_y0 = 2

# Variables
widget = None
widget_background = None
widget_foreground = None

def initialize():
    global wpm

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    return None

def create_widget():
    global widget
    global widget_background
    global widget_foreground

    widget = HWidget(widget_width, widget_height, widget_x0, widget_y0)
    widget_background = widget.get_background()
    widget_foreground = widget.get_foreground()

    # Print manually exterior border *TODO* change for print border in widget
    widget_background.window.border()
    widget_background.window.refresh()
    #widget_background.waitforkey()
    #widget_foreground.window.border()
    #widget_foreground.waitforkey()
    help_message =  "Push left to print LEFT\n" + \
                    "Push right to print RIGHT\n" + \
                    "Push up to print UP\n" + \
                    "Push down to print DOWN\n" + \
                    "Push c to clear foreground\n" + \
                    "Push q to quit\n"
    widget.create_help(help_message)

    event_print_left = EventObject(curses.KEY_LEFT, callback_event_print, ["Left\n"])
    event_print_right = EventObject(curses.KEY_RIGHT, callback_event_print, ["Right\n"])
    event_print_up = EventObject(curses.KEY_UP, callback_event_print, ["Up\n"])
    event_print_down = EventObject(curses.KEY_DOWN, callback_event_print, ["Down\n"])
    event_clear = EventObject(ord('c'), callback_clear)
    event_quit = EventObject(ord('q'), callback_quit)

    widget.add_event(event_print_left)
    widget.add_event(event_print_right)
    widget.add_event(event_print_up)
    widget.add_event(event_print_down)
    widget.add_event(event_clear)
    widget.add_event(event_quit)

    #widget.draw()
    widget_foreground.print_message("Press F1 to help.\n")
    widget.run()
    return None

def callback_event_print(message):
    widget_foreground.print_message(message)
    return None

def callback_clear():
    widget_foreground.clear()
    return None

def callback_quit():
    widget.end_condition()
    return None

def main(stdscr):
    initialize()
    create_widget()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

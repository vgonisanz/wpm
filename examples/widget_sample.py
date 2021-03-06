import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from widget import Widget
from widget import EventObject

# Configuration
widget_width = 40
widget_height = 20
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

    widget = Widget(widget_width, widget_height, widget_x0, widget_y0)
    widget_background = widget.get_background()
    widget_foreground = widget.get_foreground()

    # Print manually exterior border *TODO* change for print border in widget
    widget_background.window.border()
    widget_background.window.refresh()

    widget_foreground.print_message("Push left, s, c, or q to quit.\n")

    event_print = EventObject(curses.KEY_LEFT, "Press LEFT to write Left", callback_event_print, ["Left\n"])
    event_clear = EventObject(ord('c'), "Press c to clear widget", callback_clear)
    event_sum = EventObject(ord('s'), "Press s to sum 4 + 5", callback_sum, [ 4, 5 ])
    event_quit = EventObject(ord('q'), "Press q to quit", callback_quit)

    widget.add_event(event_print)
    widget.add_event(event_clear)
    widget.add_event(event_sum)
    widget.add_event(event_quit)

    widget.run()
    return None

def change_widget_events():
    widget.purge_events()

    widget_foreground.clear()
    widget_foreground.print_message("Push directions, or q to quit.\n")

    event_print_left = EventObject(curses.KEY_LEFT, "Press LEFT to write Left", callback_event_print, ["Left\n"])
    event_print_right = EventObject(curses.KEY_RIGHT, "Press RIGHT to write Right", callback_event_print, ["Right\n"])
    event_print_up = EventObject(curses.KEY_UP, "Press UP to write Up", callback_event_print, ["Up\n"])
    event_print_down = EventObject(curses.KEY_DOWN, "Press DOWN to write Down", callback_event_print, ["Down\n"])
    event_quit = EventObject(ord('q'), "Press q to quit", callback_quit)

    widget.add_event(event_print_left)
    widget.add_event(event_print_right)
    widget.add_event(event_print_up)
    widget.add_event(event_print_down)
    widget.add_event(event_quit)

    widget.run()
    return None

def callback_event_print(message):
    widget_foreground.print_message(message)
    return None

def callback_clear():
    widget_foreground.clear()
    return None

def callback_sum(a, b):
    widget_foreground.print_message("a + b = %s\n" % str(a + b) )
    return None

def callback_quit():
    widget.end_condition()
    return None

def main(stdscr):
    initialize()
    create_widget()
    change_widget_events()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

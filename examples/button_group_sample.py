import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/groups'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from widget import Widget
from eventobject import EventObject
from button_group import ButtonGroup
from button import Button

# Configuration
widget_width = 0
widget_height = 0
widget_x0 = 0
widget_y0 = 0

message_x0 = 1
message_y0 = 1

position_x0_button_1 = 1
position_y0_button_1 = 2

# Variables
wpm = None
screen = None

widget = None
widget_background = None
widget_foreground = None
button_group = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()   # Get main window to print
    return None

def create_buttons():
    global button_group

    screen.print_message("Creating button group...")
    button_group = ButtonGroup()

    button_text = "B1"
    button_width = 10

    # Add textbox and button inside
    ok_button = Button(button_text, button_width, position_x0_button_1, position_y0_button_1)
    #ok_button.set_on_push_callback(self.callback_quit)
    ok_button.draw()

    screen.waitforkey()
    return None

def create_widget_to_manage_buttons():
    global widget
    global widget_background
    global widget_foreground

    widget = Widget(widget_width, widget_height, widget_x0, widget_y0)
    widget_background = widget.get_background()
    widget_foreground = widget.get_foreground()

    event_left = EventObject(curses.KEY_LEFT, "Press LEFT to select previous", callback_previous)
    event_right = EventObject(curses.KEY_RIGHT, "Press RIGHT to select next", callback_next)
    event_up = EventObject(curses.KEY_UP, "Press UP to select middle", callback_select, [1] )

    widget.add_event(event_left)
    widget.add_event(event_right)
    widget.add_event(event_up)

    widget.run()
    return None

def callback_next():
    message = "Callback next pressed."
    wpm.logger.info(message)
    screen.clearln(message_y0)
    screen.print_message(message, message_x0, message_y0)
    return None

def callback_previous():
    message = "Callback previous pressed."
    wpm.logger.info(message)
    screen.clearln(message_y0)
    screen.print_message(message, message_x0, message_y0)
    return None

def callback_select(number):
    message = "Callback select pressed."
    wpm.logger.info(message)
    screen.clearln(message_y0)
    screen.print_message(message, message_x0, message_y0)
    return None

def main(stdscr):
    initialize()
    create_buttons()
    create_widget_to_manage_buttons()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

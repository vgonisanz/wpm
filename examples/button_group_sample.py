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
position_x0_button_2 = 1
position_y0_button_2 = 3
position_x0_button_3 = 1
position_y0_button_3 = 4
button_text_1 = "B1"
button_text_2 = "B2"
button_text_3 = "B3"
button_width = 10

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

    # Add textbox and button inside
    button_1 = Button(button_text_1, button_width, position_x0_button_1, position_y0_button_1)
    button_2 = Button(button_text_2, button_width, position_x0_button_2, position_y0_button_2)
    button_3 = Button(button_text_3, button_width, position_x0_button_3, position_y0_button_3)

    button_1.set_on_push_callback(callback_print_ok)

    # Append
    button_group.add_button(button_1)
    button_group.add_button(button_2)
    button_group.add_button(button_3)

    # Draw
    button_group.update_button_state()

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
    event_enter = EventObject(10, "Press <ENTER> to select", callback_enter) # Shall be curses.KEY_ENTER = 10
    event_quit = EventObject(ord('q'), "Press <q> to quit", callback_quit)

    widget.add_event(event_left)
    widget.add_event(event_right)
    widget.add_event(event_up)
    widget.add_event(event_quit)
    widget.add_event(event_enter)

    widget.run()
    return None

def callback_next():
    message = "Callback next pressed."
    callback_print(message)
    button_group.next_button()
    return None

def callback_previous():
    message = "Callback previous pressed."
    callback_print(message)
    button_group.previous_button()
    return None

def callback_select(number):
    message = "Callback select pressed."
    callback_print(message)
    button_group.select_button(number)
    return None

def callback_quit():
    widget.end_condition()
    return None

def callback_enter():
    button_group.push_current_button()
    return None

def callback_print_ok():
    callback_print("Ok pushed.")
    return None

def callback_print(message):
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

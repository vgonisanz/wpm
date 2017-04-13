import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from textbox import TextBox

# Configuration
textbox_inside_message = "Textbox inside box"
textbox_up_message = "Textbox in top of box"

textbox_width = 30
textbox_height = 10
textbox_x0 = 1
textbox_y0 = 2

# Variables
wpm = None
background = None

def initialize():
    global wpm
    global background

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    background = wpm.get_background()   # Get main window to print
    return None

def draw_textbox():

    background.print_message("There are 2 textbox:", textbox_x0, textbox_y0)
    current_x = textbox_x0 + 2
    current_y = textbox_y0 + 3

    textbox = TextBox(textbox_width, textbox_height, current_x, current_y)
    textbox.set_text(textbox_up_message)
    textbox.window.border()
    textbox.draw()

    current_x += 2
    current_y += 2

    textbox2 = TextBox(textbox_width, textbox_height, current_x, current_y)
    textbox2.set_text(textbox_inside_message)
    textbox2.set_cursor(3, 3)
    textbox2.window.border()
    textbox2.draw()

    background.waitforkey()
    return None

def draw_more_textbox():
    background.clear()
    background.print_message("There are 2 more textbox:", textbox_x0, textbox_y0)
    current_x = textbox_x0 + 2
    current_y = textbox_y0 + 1

    textbox = TextBox(textbox_width, textbox_height, current_x, current_y)
    textbox.set_text("This text is useless")
    textbox.set_manual_draw(True)
    textbox.window.border()
    textbox.draw()  # Do nothing

    current_x += 5
    current_y += 5

    textbox2 = TextBox(textbox_width, textbox_height, current_x, current_y)
    textbox2.set_text(textbox_inside_message)
    textbox2.set_cursor_center(True)
    textbox2.window.border()
    textbox2.draw()

    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    draw_textbox()
    draw_more_textbox()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

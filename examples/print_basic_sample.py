import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration
x0 = 1
y0 = 1
current_y = y0

# Variables
wpm = None
screen = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()   # Get main window to print
    return None

def print_message_initial():
    screen.print_message("In this sample we are going to print messages.", x0, current_y)
    screen.waitforkey(True)
    return None

def print_message_attributes():
    # Clear screen
    screen.clear()

    # Different attributes message
    current_y = y0
    screen.print_message("You can change several text attribute:", x0, current_y)
    current_y += 1
    screen.print_message("A_ALTCHARSET", x0, current_y, curses.A_ALTCHARSET)
    current_y += 1
    screen.print_message("A_BLINK", x0, current_y, curses.A_BLINK)
    current_y += 1
    screen.print_message("A_BOLD", x0, current_y, curses.A_BOLD)
    current_y += 1
    screen.print_message("A_DIM", x0, current_y, curses.A_DIM)
    current_y += 1
    screen.print_message("A_NORMAL", x0, current_y, curses.A_NORMAL)
    current_y += 1
    screen.print_message("A_REVERSE", x0, current_y, curses.A_REVERSE)
    current_y += 1
    screen.print_message("A_STANDOUT", x0, current_y, curses.A_STANDOUT)
    current_y += 1
    screen.print_message("A_UNDERLINE", x0, current_y, curses.A_UNDERLINE)
    screen.waitforkey(True)
    return None

def print_message_slow():
    screen.clear()

    # Change color character and screen
    current_y = y0
    screen.print_message_slow("This message is slooooooow", x0, current_y, 500)
    current_y += 1
    screen.print_message_slow("and this just slow", x0, current_y, 50)
    screen.waitforkey(True)
    screen.clear()
    return None

def print_change_color():
    screen.clear()

    # Change color character and screen
    current_y = y0
    screen.print_message("Last, You can change a concrete color from the pair palette, we change screen color.", x0, current_y)
    screen.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Modify to use a palette!
    screen.waitforkey(True)
    screen.clear()
    return None

def main(stdscr):
    initialize()
    print_message_initial()
    print_message_attributes()
    print_message_slow()
    print_change_color()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

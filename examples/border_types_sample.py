import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/structs'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element
from bordertypes import BorderTypes

# Configuration
border_width = 20
border_height = 10
border_x0 = 1
border_y0 = 1

# Variables
wpm = None
element = None
element_screen = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    #screen = wpm.get_screen()
    return None

def create_element():
    global element

    element = Element(border_width, border_height, border_x0, border_y0)
    return None

def set_border(number):
    element.print_border_type(number)
    element.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_element()
    #set_border(BorderTypes.normal)
    #set_border(BorderTypes.simple)
    #set_border(BorderTypes.double)
    #set_border(BorderTypes.simplest)
    #set_border(BorderTypes.rounded)
    #set_border(BorderTypes.quadrant)
    set_border(BorderTypes.shade_light)
    set_border(BorderTypes.shade_medium)
    set_border(BorderTypes.shade_dark)
    set_border(BorderTypes.density)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

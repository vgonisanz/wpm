# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

from curses import wrapper  # Use my own wrapper
import curses

from wpm import Wpm
from table import Table

# Configuration
table_custom_title = "Curses variables:"
table_custom_width = 2
table_custom_height = 3
table_custom_x0 = 0
table_custom_y0 = 0
table_custom_cell_width = 40

# Variables
wpm = None
screen = None
table = None
table_custom = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()
    screen.print_character(int(curses.ACS_BBSS))
    screen.waitforkey()
    return None

def create_table_curses():
    global table_custom

    screen.clear()
    table_custom = Table(table_custom_width, table_custom_height, table_custom_x0, table_custom_y0, table_custom_cell_width)
    table_custom.set_title(table_custom_title)

    # Data only defined after initscr()
    table_custom_data = [   [ "ACS_BBSS", curses.ACS_BBSS   ],
                            [ "ACS_BBSS", curses.ACS_BBSS   ],
                            [ "ACS_BBSS", curses.ACS_BBSS    ]
                        ]

    table_custom.set_data(table_custom_data)
    table_custom.draw()
    table_custom.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_table_curses()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

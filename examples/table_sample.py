import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from table import Table

# Configuration
table_title = "My table:"
table_width = 7
table_height = 7
table_x0 = 0
table_y0 = 0
table_cell_width = 3
cell_value = "123"

table_custom_title = "Custom table:"
table_custom_width = 3
table_custom_height = 3
table_custom_x0 = 0
table_custom_y0 = 0
table_custom_cell_width = 4
table_custom_data = [   [ "1234", "abcd", "ABCD"],
                        [ "123456", "abcdef", "ABCDEF"],
                        [ "a", "b", "c"] ]

# Variables
wpm = None
background = None
table = None
table_custom = None

def initialize():
    global wpm
    global background

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    background = wpm.get_background()
    return None

def create_table():
    global table

    table = Table(table_width, table_height, table_x0, table_y0, table_cell_width, cell_value)
    table.set_title(table_title)
    table.draw()
    table.waitforkey()
    return None

def create_table_custom():
    global table_custom

    background.clear()
    table_custom = Table(table_custom_width, table_custom_height, table_custom_x0, table_custom_y0, table_custom_cell_width)
    table_custom.set_title(table_custom_title)
    table_custom.set_data(table_custom_data)
    table_custom.draw()
    table_custom.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_table()
    create_table_custom()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

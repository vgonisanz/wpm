import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration

# Variables
wpm = None
screen = None
def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()
    return None

def print_colors_1():
    screen.print_message("Total colors are: %d\n" % curses.COLORS )
    # How improve this code using wpm????
    curses.start_color()
    curses.use_default_colors()
    
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    #try:
    for i in range(0, curses.COLORS):
        if i % 8 == 0:
            screen.window.addstr("\n")
        screen.window.addstr("%03d" % i, curses.color_pair(i))
        screen.window.addstr("-", curses.color_pair(1))
    #except curses.ERR:
        # End of screen reached
    #    stdscr.addstr(curses.ERR)
    #except:
    #    print("Unexpected error:", sys.exc_info()[0])
    #    pass
    screen.window.getch()
    return None

def print_colors_2():
    screen.clear()
    screen.print_message("You can change them:\n")

    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_WHITE)

    #try:
    for i in range(0, curses.COLORS):
        if i % 8 == 0:
            screen.window.addstr("\n")
        screen.window.addstr("%03d" % i, curses.color_pair(i))
        screen.window.addstr("-", curses.color_pair(1))
    #except curses.ERR:
        # End of screen reached
    #    stdscr.addstr(curses.ERR)
    #except:
    #    print("Unexpected error:", sys.exc_info()[0])
    #    pass
    screen.window.getch()
    return None

def print_custom_colors():
    try:
        curses.init_color(5, 1000, 0, 0)
        screen.window.addstr("Custom color red", curses.color_pair(5))
    except curses.ERR:
        # End of screen reached
        screen.window.addstr(curses.ERR)
    except Exception as e:
        print("Unexpected error: %s" % e)
        pass
    screen.window.getch()
    return None

def main(stdscr):
    initialize()
    print_colors_1()
    print_colors_2()
    print_custom_colors()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

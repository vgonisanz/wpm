import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()

    # How improve this code using wpm????
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    #try:
    for i in range(0, 255):
        stdscr.addstr(str(i), curses.color_pair(i))
        stdscr.addstr("-", curses.color_pair(1))
    #except curses.ERR:
        # End of screen reached
    #    stdscr.addstr(curses.ERR)
    #except:
    #    print("Unexpected error:", sys.exc_info()[0])
    #    pass
    stdscr.getch()

    try:
        curses.init_color(2, 1000, 0, 0)
    except curses.ERR:
        # End of screen reached
        stdscr.addstr(curses.ERR)
    except Exception as e:
        print("Unexpected error: %s" % e)
        pass
    stdscr.getch()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use all print color.")
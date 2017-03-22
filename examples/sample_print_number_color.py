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
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
            stdscr.addstr("-", curses.color_pair(1))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

    curses.init_color(2, 1000, 0, 0)

    stdscr.getch()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use all print color.")
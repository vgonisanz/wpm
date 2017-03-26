import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))
from cursesManager import CursesManager

def main(stdscr):
    # Initialize curses manager
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.create_screen_info_popup()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use widget stack sample")

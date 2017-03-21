import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

def main(stdscr):
    Wpm().diagnose()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use diagnose terminal.")
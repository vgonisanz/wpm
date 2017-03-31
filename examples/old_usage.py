import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))

from curses import wrapper
from cursesManager import CursesManager

def test1(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()
    return

def test2(stdscr):

    return

def current(stdscr):
    cman = CursesManager()
    cman.create_window()
    cman.draw()
    cman.close()
    sys.exit(0)
    return None

#wrapper(test1)
#test2()
if __name__ == "__main__":
    print("Welcome")
    #wrapper(current)
    wrapper(test2)

import curses
from curses import wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))
from wpm import Wpm

def main(stdscr):
    wpm = Wpm()
    #wpm.size_stack(False)
    #width, height = wpm.get_window_size()
    #wpm.print_message(stdscr, "Window size: %d, %d" %(width, height))
    #wpm.print_message(stdscr, "idiota", 5, 5)
    button = wpm.create_element_button()
    #wpm.rwait(1)
    button.draw()
    wpm.wait(2000)
    #wpm.rwait(1)
    #wpm.waitforkey(True)
    # Initialize curses manager
    #cm = CursesManager()
    #cm.set_current_window(stdscr)
    #cm.clear()
    #
    #button.hello()
    #cm.waitforkey()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use button sample")

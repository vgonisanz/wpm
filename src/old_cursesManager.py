import curses
import locale

from element_button import Button

"""
This python 3 class will manager a curses windows for you.

To generate HTML documentation for this module issue the command:

    pydoc -w cursesManager
"""

class CursesManager(object):



    """
    Reverse line y.

    :return: returns None
    """

    def reverseln(self, y0, clear = False):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            self._current_window.move(y0, 0)
            if clear:
                self._current_window.clrtoeol()
            self._current_window.chgat(y0, 0, x_max, curses.A_REVERSE)
        return None

    """
    Clear line y.

    :return: returns None
    """

    def clearln(self, y0):
        if self._current_window != None:
            self._current_window.move(y0, 0)
            self._current_window.clrtoeol()
        return None

    """
    Clear line from (x, y) position.

    :return: returns None
    """

    def clrtoeol(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtoeol()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns None
    """

    def clrtobot(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.clrtobot()
        return None

    """
    Print hline in (x, y) position.

    :return: returns None
    """

    def hline(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.hline()
        return None

    """
    Print hline in (x, y) position.

    :return: returns None
    """

    def vline(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
            self._current_window.vline()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns None
    """

    def flash(self):
        curses.flash()
        return None

    """
    Request insert next line, moving down data

    :return: returns None
    """

    def insertln(self, y0):
        if self._current_window != None:
            self._current_window.move(y0, 0)
            self._current_window.insertln()
        return None

    """
    Request delete line at line y

    :return: returns None
    """

    def deleteln(self, y0 = -1):
        if self._current_window != None:
            if y0 >= 0:
                self._current_window.move(y0, 0)
            self._current_window.deleteln()
        return None

    """
    Request delete character at position x0, y0

    :return: returns None
    """

    def delch(self, x0, y0):
        if self._current_window != None:
            self._current_window.delch(y0, x0)
        return None


    """
    Get max size position.

    :return: returns max valid x and y, or -1 if not window
    """

    def get_max_cursor(self):
        y = -1
        x = -1
        if self._current_window != None:
            y, x = self._current_window.getmaxyx()
            y = y - 2
            x = x - 1
        return x, y

    """
    Get a valid coordinates. 0 is value < min, and max if  value > max

    :return: returns valid x and y, or -1 if not window
    """

    def get_valid_cursor(self, x0, y0):
        y = -1
        x = -1
        if self._current_window != None:
            y, x = self._current_window.getmaxyx()
            y = y - 2
            x = x - 1
            if x0 < 0:
                x = 0
            elif x0 <= x:    # Valid value inside
                x = x0
            if y0 < 0:
                y = 0
            elif y0 <= y:
                y = y0
        return x, y


    """
    Print a progress bar in a position (x0, y0) with width

    :param: progress from 0 to 100
    :return: returns nothing
    """

    def print_progress_bar(self, progress, x0 = 0, y0 = 0, width = 0, attributes = curses.A_NORMAL):
        if self._current_window != None:
            if width == 0:
                width = curses.LINES - x0
            if progress < 0:
                progress = 0
            if progress > 100:
                progress = 100
            no_bar_size = 7
            bar_width = width - no_bar_size
            progress_width = int(progress * bar_width / 100)
            empty_progress_width = bar_width - progress_width
            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor position
            self._current_window.move(y0, x0)
            self._current_window.addch("[")
            for i in range(0, progress_width):
                self._current_window.addch("=")
            #self._current_window.addch(">")
            for i in range(0, empty_progress_width):
                self._current_window.addch("*")
            self._current_window.addch("]")
            self._current_window.addch(" ")
            self._current_window.addstr(str(progress))
            self._current_window.addch("%")
            # Restore attributes
            self._current_window.attroff(attributes)
            self._current_window.refresh()
        return None

    """
    Print book like.

    :return: returns nothing
    """

    def print_book(self, title, pages, author = ""):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            mid_y = (int)(y_max / 2)
            q_y = (int)(y_max * 3/4)
            q_x = (int)(x_max * 3/4)
            # Print title, author, and wait
            self.clear()
            self.print_message_center(title, mid_y)
            self.print_message_at(author, q_x, q_y)
            self.print_border()
            self.waitforkey()
            # Read each page
            for page in pages:
                self.clear()
                self.print_message_at(page, 1,1)
                self.print_border()
                self.waitforkey()
            # End
            self.clear()
            self.print_message_center("The end", y/2)
            self.print_border()
            self.waitforkey()
        return None

    """
    print 4 windows in a box.

    :return: returns win0, win1, win2, win3
    """

    def print_4windows(self):
        y_max, x_max = self._current_window.getmaxyx()
        y_2 = y_max / 2
        x_2 = x_max / 2
        win0 = curses.newwin(y_2, x_2, 0, 0)
        win1 = curses.newwin(y_2, x_2, 0, x_2)
        win2 = curses.newwin(y_2, x_2, y_2, 0)
        win3 = curses.newwin(y_2, x_2, y_2, x_2)
        self.rwait(1)
        win0.addstr(1, 1, "Window 0")
        win1.addstr(1, 1, "Window 1")
        win2.addstr(1, 1, "Window 2")
        win3.addstr(1, 1, "Window 3")
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE);
        win0.bkgd(curses.color_pair(2))
        win0.border()
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE);
        win1.bkgd(curses.color_pair(3))
        win1.border()
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_WHITE);
        win2.bkgd(curses.color_pair(4))
        win2.border()
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN);
        win3.bkgd(curses.color_pair(5))
        win3.border()
        return win0, win1, win2, win3

    """
    Create a simple interface.

    :return: Return option delimiter line
    """

    def create_simple_ui(self, window, options, title = "", print_title = True):
        simpleui = self.SimpleUserInterfaceCM(self, window, options, title, print_title)
        return simpleui


    """
    Nested class to manager a simple UI for you.

    """
    class SimpleUserInterfaceCM(object):
        _window = None
        _cm = None
        _title = None
        _options_size = 0
        _options = []
        _print_title = False
        _secondary_window = None
        _delimiter_line = 0

        """
        Initialize SimpleUserInterfaceCM
        """

        def __init__(self, curses_manager, window, options, title, print_title):
            option_size = len(options)
            if option_size <= 0:
                return None
            if window == None:
                return None
            self._window = window
            self._cm = curses_manager
            self._title = title
            self._option_size = option_size
            self._options = options
            self._print_title = print_title
            # Get terminal size
            y_max, x_max = self._window.getmaxyx()
            # Print title if needed
            if print_title:
                self._cm.print_message_center(title, 0)
                self._cm.reverseln(0, False)
            # Create secondary window
            sec_win_x0 = 0
            sec_win_y0 = 1
            sec_win_x = x_max
            sec_win_y = y_max - option_size - 2
            if not print_title:
                sec_win_y0 = 0
            self._secondary_window = curses.newwin(sec_win_y, sec_win_x, sec_win_y0, sec_win_x0)
            # Box secondary window
            self._secondary_window.border()
            # Calculate delimiter position
            self._delimiter_line = y_max - option_size - 1
            return None

        """
        Print UI and wait response. Change current window.

        :return: returns -1 if quit with q or ESC, option id from [0, N-1] if ENTER
        """

        def draw(self):
            self._cm.set_current_window(self._window)
            # Get terminal size
            y_max, x_max = self._window.getmaxyx()
            # Print bottom options
            col = 0
            for index,option in enumerate(self._options):
                col = index + 1
                self._cm.print_message_at(option, 0, y_max - col)
            # Reverse separator
            self._cm.reverseln(self._delimiter_line)
            return None

        """
        Clear secondary window. Modify current window!

        :return: None
        """

        def clear_secondary_window(self):
            self._cm.set_current_window(self._secondary_window)
            self._cm.clear()

        """
        Print command in reverse line

        :return: None
        """

        def print_command(self, message, x0 = 1):
            self._cm.set_current_window(self._window)
            self._cm.reverseln(self._delimiter_line, True)
            self._cm.print_message_at(message, x0, self._delimiter_line, curses.A_REVERSE)
            self._cm.rwait(1)
            return None

        """
        Getter to manage manually secondary window

        :return: Secondary window
        """

        def get_secondary_window(self):
            return self._secondary_window

        """
        Getter to have delimiter data

        :return: Secondary window
        """

        def get_delimiter_line(self):
            return self._delimiter_line

    """
    Template function.

    :return: returns nothing
    """

    def template(self):
        #
        return None

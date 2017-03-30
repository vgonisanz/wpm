import curses
import locale

from element_button import Button

"""
This python 3 class will manager a curses windows for you.

To generate HTML documentation for this module issue the command:

    pydoc -w cursesManager
"""

class CursesManager(object):
    _screen = None              # curses screen
    _current_window = None      # current widget object to render

    """
    Initialize CursesManager
    """

    def __init__(self, echo=False):
        print("Initializing curses Manager")

        # Set UTF-8
        locale.setlocale(locale.LC_ALL, '')
        #code = locale.getpreferredencoding()

        # Initialize screen
        self._screen = curses.initscr()
        return

    """
    Enter CursesManager
    """

    def __enter__(self):
        print("Enter curses Manager")
        return self

    """
    Exit CursesManager
    """

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit curses Manager")
        curses.endwin()
        return None

    """
    Initialize basic stuffs.

    :return: returns nothing
    """

    def init(self):
        print("Init basic stuffs")
        if curses.has_colors():
            curses.start_color()
        #stdscr.keypad(True)  # Allow F1, ...
        return None

    """
    Print screen info.

    :return: returns nothing
    """

    def print_screen_info(self):
        self._screen.addstr("\n  Userful info:")
        self._screen.addstr("\n  Terminal: %s" % curses.longname())
        self._screen.addstr("\n  Can use color: %s" % curses.has_colors())
        if curses.has_colors():
            self._screen.addstr("\n  Can change colors: %s" % curses.can_change_color())
            self._screen.addstr("\n  Terminal has %s colors" % curses.COLORS)
            self._screen.addstr("\n  Terminal has %s pairs of colors" % curses.COLOR_PAIRS)
        self._screen.addstr("\n  Number of lines: %s (y size) " % curses.LINES)
        self._screen.addstr("\n  Number of cols: %s (x size)" % curses.COLS)
        self._screen.border()
        self._screen.getkey()
        return None

    """
    Create button element.

    :return: returns nothing
    """

    def create_button(self):
        button = Button()
        return button

    """
    Create screen info popup.

    :return: returns nothing
    """

    def create_screen_info_popup(self):
        return None

    """
    Diagnose terminal and print info. Static, you can use githout instance.
    Give all info about curses and you terminal. Use it at the beginning to test.

    :return: returns nothing
    """
    @staticmethod
    def diagnose():
        window = curses.initscr()
        window.addstr("\n  Userful info:")
        window.addstr("\n  Terminal: %s" % curses.longname())
        window.addstr("\n  Can use color: %s" % curses.has_colors())
        if curses.has_colors():
            window.addstr("\n  Can change colors: %s" % curses.can_change_color())
            window.addstr("\n  Terminal has %s colors" % curses.COLORS)
            window.addstr("\n  Terminal has %s pairs of colors" % curses.COLOR_PAIRS)
        window.addstr("\n  Number of lines: %s (y size) " % curses.LINES)
        window.addstr("\n  Number of cols: %s (x size)" % curses.COLS)
        window.border()
        window.getkey()
        curses.endwin()
        return None

    """
    Create window object.

    :return: returns nothing
    """

    def create_window(self, width = 20, height = 20):
        print("Creating window with size: %sx%s" % (width, height))
        return None

    """
    Draw an object.

    :return: returns nothing
    """

    def draw(self):
        print("Drawing...")
        #self._stdscr.addstr(0, 0, "Hi!")
        #self._stdscr.refresh()
        return None

    """
    Close curses object.

    :return: returns nothing
    """

    def cleanup(self):
        curses.endwin()
        print("Cleaning up...")
        return None

    """
    Set current window to work. Use before print any message

    :return: returns nothing
    """

    def set_current_window(self, stdscr):
        self._current_window = stdscr
        return None

    """
    Clear current window.

    :return: returns nothing
    """

    def clear(self):
        if self._current_window != None:
            self._current_window.clear()
            self._current_window.refresh()
        return None

    """
    Get a key.

    :return: returns None
    """

    def getkey(self):
        if self._current_window != None:
            return self._current_window.getkey()
        return None

    """
    Get a char.

    :return: returns character
    """

    def getch(self):
        if self._current_window != None:
            return self._current_window.getch()
        return None

    """
    Get a string.

    :return: returns string entered
    """

    def getstr(self):
        if self._current_window != None:
            return self._current_window.getstr()
        return None

    """
    Wait for key.

    :return: returns None
    """

    def waitforkey(self, print_text = True, x0 = -1, y0 = -1):
        if self._current_window != None:
            self.rwait(1)
            if x0 > -1 and y0 > -1:
                self.set_window_cursor(x0, y0)
            if print_text:
                self.print_message("\n Press any key to continue.")
            return self._current_window.getkey()
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns None
    """

    def rwait(self, ms = 1):
        if self._current_window != None:
            self._current_window.refresh()
        curses.napms(ms)
        return None

    """
    Set cursor at position.

    :return: returns None
    """

    def set_cursor(self, x0, y0):
        if self._current_window != None:
            self._current_window.move(y0, x0)
        return None

    """
    Set cursor mode.
    0 = Invisible
    1 = Visible
    2 = Very visible

    :return: returns None
    """

    def set_cursor_mode(self, mode):
        if mode >= 0 and mode < 3:
            curses.curs_set(mode)
        return None

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
    Get cursor position.

    :return: returns x and y, or -1 if not window
    """

    def get_cursor(self):
        y = -1
        x = -1
        if self._current_window != None:
            y, x = self._current_window.getyx()
        return x, y

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
    Print background with color.

    :return: returns nothing
    """

    def print_background(self, color_character, color_background):
        if self._current_window != None:
            # Set color
            curses.init_pair(7, color_character, color_background);
            # Draw background
            self._current_window.bkgd(curses.color_pair(7));
            self.rwait(1)
        return None

    """
    Print border with elements.

    :return: returns nothing
    """

    def print_border(self, type = 0):
        if self._current_window != None:
            # Set border
            if type == 0:
                self._current_window.border()
            elif type == 1:
                self._current_window.border(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK)
            elif type == 2:
                self._current_window.border("|", "|", "-", "-", "x", "x", "x", "x")
            else:
                ls = "X"
                rs = "X"
                ts = "X"
                bs = "X"
                tl = "X"
                tr = "X"
                bl = "X"
                br = "X"
                self._current_window.border(ls, rs, ts, bs, tl, tr, bl, br)
            self.rwait(1)
        return None

    """
    Print a character string at current cursor position.

    :return: returns nothing
    """

    def print_ch(self, ch, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Print
            self._current_window.addch(ch)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a character string at current cursor position.

    :return: returns nothing
    """

    def print_ch_at(self, ch, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self._current_window.move(y0, x0)
            # Print
            self._current_window.addch(ch)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at current cursor position.

    :return: returns nothing
    """

    def print_message(self, message, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at y position centered.

    :return: returns nothing
    """

    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        if self._current_window != None:
            y_max, x_max = self._current_window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor
            self.set_cursor(indent, y0_int)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message slow with delay between character at cursor position.

    :return: returns nothing
    """

    def print_message_slow(self, message, inter_delay = 100, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            for char in message:
                self._current_window.addch(char)
                self._current_window.refresh()
                curses.napms(inter_delay)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message string at position.

    :return: returns nothing
    """

    def print_message_at(self, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self._current_window.move(y0, x0)
            # Print
            self._current_window.addstr(message)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

    """
    Print a message with delay between character. It cannot be skipped.

    :return: returns nothing
    """

    def print_message_slow_at(self, message, x0 = 0, y0 = 0, inter_delay = 100, attributes = curses.A_NORMAL):
        if self._current_window != None:
            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor position
            self._current_window.move(y0, x0)
            for char in message:
                self._current_window.addch(char)
                self._current_window.refresh()
                curses.napms(inter_delay)
            # Restore attributes
            self._current_window.attroff(attributes)
        return None

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
    Print an array of characters as a matrix with row size in a position (x0, y0) with a offset between values

    :return: returns nothing
    """

    def print_character_array(self, character_array, row_size, x0 = 0, y0 = 0, offset = 0, attributes = curses.A_NORMAL):
        if self._current_window != None:
            cols = int(len(character_array) / row_size)
            current_col = 0
            # Set attributes
            self._current_window.attrset(attributes)
            # Set cursor position
            self._current_window.move(y0, x0)
            for i in range(0, cols):
                for j in range(0, row_size):
                    value = i * row_size + j
                    self._current_window.addch(character_array[value])
                    for k in range(0, offset):
                        self._current_window.addch(" ")
                current_col = current_col + 1
                self._current_window.move(y0 + current_col, x0)
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
    Print a question and return answer.

    :return: returns string
    """

    def print_question(self, question, feedback = True, x0_question = -1, y0_question = -1, x0_answer = -1, y0_answer = -1):
        answer = ""
        if len(question) <= 0:
            return answer
        if self._current_window != None:
            if not (x0_question == -1 and y0_question == -1):
                self.set_cursor(x0_question, y0_question)
            self.print_message(question)
            if feedback == False:
                curses.noecho()
            else:
                curses.echo()
            if not (x0_answer == -1 and y0_answer == -1):
                self.set_cursor(x0_answer, y0_answer)
            answer = self.getstr()
        return answer

    """
    Create a simple interface.

    :return: Return option delimiter line
    """

    def create_simple_ui(self, window, options, title = "", print_title = True):
        simpleui = self.SimpleUserInterfaceCM(self, window, options, title, print_title)
        return simpleui

    """
    Create menu.

    :return: returns menu object
    """

    def create_menu(self, window, title, options, instructions):
        menu = self.MenuCM(self, window, title, options, instructions)
        return menu

    """
    Nested class to manager a menu for you.

    """
    class MenuCM(object):
        _window = None
        _cm = None
        _title = None
        _options_size = 0
        _options = []
        _instructions = None
        _offset_x = 15
        _offset_y = 0
        _title_padding = 1
        _instruction_padding = 1

        """
        Initialize MenuCM
        """

        def __init__(self, curses_manager, window, title, options, instructions = "", offset_x = 15, offset_y = 0, title_padding = 1, instruction_padding = 1):
            if len(options) <= 0:
                return None
            self._window = window
            self._cm = curses_manager
            self._title = title
            self._option_size = len(options)
            self._options = options
            self._instructions = instructions
            self._offset_x = offset_x
            self._offset_y = offset_y
            self._title_padding = title_padding
            self._instruction_padding = instruction_padding
            return None

        """
        Print menu and wait response.

        :return: returns -1 if quit with q or ESC, option id from [0, N-1] if ENTER
        """

        def run(self):
            self._cm.set_current_window(self._window)
            self._cm.clear()
            option_selected = 0
            quit_menu = False
            # Refresh menu
            self.__draw_menu(option_selected)
            while not quit_menu:
                event = self._cm.getch()
                if event == ord('t'):
                    option_selected = option_selected + 1
                if event == curses.KEY_UP or event == 65:
                    option_selected = option_selected - 1
                if event == curses.KEY_DOWN or event == 66:
                    option_selected = option_selected + 1
                if event == curses.KEY_ENTER or event == 10 or event == 13:
                    quit_menu = True
                # Refresh menu
                option_selected = self.__draw_menu(option_selected)
                if event == ord('q') or event == 28:
                    quit_menu = True
                    option_selected = -1
            return option_selected

        """
        Clear menu window.

        :return: None
        """

        def clear(self):
            self._cm.set_current_window(self._window)
            self._cm.clear()
            return None

        """
        Draw menu options. Private, autoinvoked.

        :return: returns option selected
        """

        def __draw_menu(self, option_selected):
            if option_selected < 0:
                option_selected = 0
            if option_selected >= self._option_size:
                option_selected = self._option_size - 1
            counter = 0
            self._cm.print_message_at(self._title, self._offset_x, self._offset_y, curses.A_UNDERLINE)
            for option in self._options:
                if option_selected == counter:
                    self._cm.print_message_at(option, self._offset_x, counter + self._offset_y + self._title_padding + 1, curses.A_REVERSE)
                else:
                    self._cm.print_message_at(option, self._offset_x, counter + self._offset_y + self._title_padding + 1)
                counter = counter + 1
            self._cm.print_message_at(self._instructions, self._offset_x, counter + self._offset_y + self._title_padding + self._instruction_padding + 1)
            return option_selected

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

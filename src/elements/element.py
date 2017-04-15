import curses
import logging

class Element(object):
    def __init__(self, width, height, x0, y0):
        # Initialize all variables
        self.logger = None
        self.window = None
        self._width = None
        self._height = None
        self._x = None
        self._y = None
        #attributes = curses.A_NORMAL # Change all attibutes param or use a general? TODO
        self._manual_draw = False
        self._window_copy = None    # Store list with window characters
        self._cursor_x_copy = 0     # Score X cursor position when copy
        self._cursor_y_copy = 0     # Score Y cursor position when copy

        # Assign
        self.logger = logging.getLogger("wpm")
        self._width = width
        self._height = height
        self._x = x0
        self._y = y0
        try:
            self.window = curses.newwin(height, width, y0, x0)
        except Exception as e:
            self.logger.debug("curses.newwin with height: %d, width: %d, x0: %d, y0: %d" % (height, width, y0, x0))
            self.logger.debug(e)
        return None

    """
    Check if point x, y is inside.

    :return: returns False if not.
    """
    def is_inside(self, x, y):
        if x < 0 or self._width <= x or y < 0 or self._height <= y:
            return False
        else:
            return True
    """
    Set cursor at position.

    :return: returns None
    """

    def set_cursor_position(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
            self.window.refresh()
        return None

    """
    Get cursor current position.

    :return: Current cursor position tuple (x, y)
    """

    def get_cursor_position(self):
        if self.window != None:
            y, x = self.window.getyx()
        return x, y

    """
    Clear current window.

    :return: returns nothing
    """

    def clear(self):
        if self.window != None:
            self.window.clear()
            self.window.refresh()
        return None

    """
    Clear line y.

    :return: returns None
    """

    def clearln(self, y0):
        if self.window != None:
            self.window.move(y0, 0)
            self.window.clrtoeol()
        return None

    """
    Reverse line y.

    :return: returns None
    """

    def reverseln(self, y0, clear = False):
        if self.window != None:
            self.window.move(y0, 0)
            if clear:
                self.window.clrtoeol()
            self.window.chgat(y0, 0, self._width, curses.A_REVERSE)
        return None

    """
    Clear line y.

    :return: returns None
    """

    def clearln(self, y0):
        if self.window != None:
            self.window.move(y0, 0)
            self.window.clrtoeol()
        return None

    """
    Clear line from (x, y) position.

    :return: returns None
    """

    def clrtoeol(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
            self.window.clrtoeol()
        return None

    """
    Clear terminal from (x, y) position.

    :return: returns None
    """

    def clrtobot(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
            self.window.clrtobot()
        return None

    """
    Print hline in (x, y) position.

    :return: returns None
    """

    def hline(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
            self.window.hline()
        return None

    """
    Print hline in (x, y) position.

    :return: returns None
    """

    def vline(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
            self.window.vline()
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
        if self.window != None:
            self.window.move(y0, 0)
            self.window.insertln()
        return None

    """
    Request delete line at line y

    :return: returns None
    """

    def deleteln(self, y0 = -1):
        if self.window != None:
            if y0 >= 0:
                self.window.move(y0, 0)
            self.window.deleteln()
        return None

    """
    Request delete character at position x0, y0

    :return: returns None
    """

    def delch(self, x0, y0):
        if self.window != None:
            self.window.delch(y0, x0)
        return None

    """
    Print a character. Choose a position. This affect to cursor.

    :return: returns nothing
    """

    def print_character(self, character, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self.window.move(y0, x0)
            # Print
            try:
                self.window.addch(character, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    """
    Print a message string into its window. Choose a position. This affect to cursor.

    :return: returns nothing
    """

    def print_message(self, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self.window.move(y0, x0)
            # Print
            try:
                self.window.addstr(message, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    """
    Print a message string into a window. Choose y position, x automatically in the center. This affect to cursor.

    :return: returns nothing
    """

    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        if self.window != None:
            y_max, x_max = self.window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            self.set_cursor_position(indent, y0_int)
            self.window.addstr(message, attributes)
            return True
        return False

    """
    Print a message with delay between character. It cannot be skipped.

    :return: returns nothing
    """

    def print_message_slow(self, message, x0 = -1, y0 = -1, inter_delay = 100, attributes = curses.A_NORMAL):
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self.window.move(y0, x0)
            for char in message:
                # Print
                try:
                    self.window.addch(char, attributes)
                    self.window.refresh()
                    curses.napms(inter_delay)
                except curses.error:
                    pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    """
    Print border with elements.

    :return: returns nothing
    """

    def print_border(self, type = 0):
        if self.window != None:
            # Set border
            if type == 0:
                self.window.border()
            elif type == 1:
                self.window.border(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK)
            elif type == 2:
                self.window.border("|", "|", "-", "-", "x", "x", "x", "x")
            else:
                ls = "X"
                rs = "X"
                ts = "X"
                bs = "X"
                tl = "X"
                tr = "X"
                bl = "X"
                br = "X"
                self.window.border(ls, rs, ts, bs, tl, tr, bl, br)
            # Refresh
            self.window.refresh()
        return None

    """
    Print an array of characters with colors as a matrix with row size in a position (x0, y0) with a offset between values

    :return: returns nothing
    """

    def print_sprite(self, sprite, x0 = 0, y0 = 0, attributes = curses.A_NORMAL):
        if self.window != None:
            current_col = 0
            # Set attributes
            self.window.attrset(attributes)
            # Set cursor position
            self.window.move(y0, x0)
            for i in range(0, sprite.height):
                for j in range(0, sprite.width):
                    value = i * sprite.width + j
                    color_id = sprite.colorpairs[value]
                    self.window.addch(sprite.characters[value], curses.color_pair(color_id) )
                current_col = current_col + 1
                self.window.move(y0 + current_col, x0)
            # Restore attributes
            self.window.attroff(attributes)
            self.window.refresh()
        return None

    """
    Print foreground with a pattern from (0, 0).

    :return: returns nothing
    """

    def fill_with_pattern(self, pattern):
        if self.window != None:
            y_max, x_max = self.window.getmaxyx()
            lenght = len( pattern )
            times = (int)(x_max * y_max / lenght)
            self.window.move(0, 0)
            for i in range(0, times):
                self.print_message(pattern)
        return None

    """
    Print foreground with color.

    :return: returns nothing
    """

    def change_color(self, color_character, color_foreground):
        if self.window != None:
            curses.init_pair(7, color_character, color_foreground)
            self.window.bkgd(curses.color_pair(7)) # Warning, color pair apply to all elements in curses, probably need a variable inside and change global this value!
            self.window.refresh()
        return None

    """
    Wait for key. TODO remove?

    :return: returns None
    """

    def waitforkey(self, print_text = False, x0 = -1, y0 = -1):
        # Print in window by default, check what need in a general way
        if x0 > -1 and y0 > -1:
            self.set_cursor_position(x0, y0)
        if print_text:
            self.print_message("\nPress any key to continue.")
        return self.window.getkey()

    """
    If input true, draw call won't be processed. All draw in this widget must be done manually with self.window.

    :return: returns None
    """

    def set_manual_draw(self, value):
        self._manual_draw = value
        return None

    """
    If input true, start taking keyboard events.

    :return: returns None
    """

    def set_input_mode(self, value):
        self.window.keypad(value)
        return None

    """
    Wait for a character. Need set input mode true

    :return: returns None
    """

    def get_character(self):
        # Set always NO DELAY?
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self.window.getch()


    def store_window(self):
        # Save cursor
        self._cursor_y_copy, self._cursor_x_copy = self.window.getyx()

        # Save whole window
        self.window.move(0, 0)
        self._window_copy = []
        for i in range(0, self._height):
            for j in range(0, self._width):
                charactertype = self.window.inch(i, j)
                self._window_copy.append(charactertype)
        return None

    def restore_window(self):
        if self._window_copy:
            value = 0

            # Restore whole window
            self.window.move(0, 0)
            for i in range(0, self._height):
                for j in range(0, self._width):
                    try:
                        character = self._window_copy[value]
                        self.window.addch(i, j, character)
                    except:
                        pass
                    value += 1

            # Restore pointer and refresh
            self.window.move(self._cursor_y_copy, self._cursor_x_copy)
            self.window.refresh()
            self._window_copy = None
        return None

    def draw(self):
        # if not self._manual_draw:
            # Override me
        return None

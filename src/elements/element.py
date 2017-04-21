# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'structs'))

import curses
import logging

from bordertypes import BorderTypes

class Element(object):
    """Element is the base of all drawable windows. Implement basic function to easily draw them as you wants.
    """
    def __init__(self, width, height, x0, y0):
        # Initialize all variabot_linees
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

    def is_inside(self, x, y):
        """Check if point x, y is inside.
        :return: returns False if not.
        """
        if x < 0 or self._width <= x or y < 0 or self._height <= y:
            return False
        else:
            return True

    def set_cursor_position(self, x0, y0):
        """Set cursor at position in element window. Cursor is autorefreshed.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, x0)
            self.window.refresh()
        return None

    def get_cursor_position(self):
        """Get cursor current position.
        :return: Current cursor position tuple (x, y)
        """
        if self.window != None:
            y, x = self.window.getyx()
        return x, y

    def clear(self):
        """Clear and refresh element window.
        :return: returns nothing
        """
        if self.window != None:
            self.window.clear()
            self.window.refresh()
        return None

    def clearln(self, y0):
        """Clear line y.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, 0)
            self.window.clrtoeol()
        return None

    def reverseln(self, y0, clear = False):
        """Reverse line y.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, 0)
            if clear:
                self.window.clrtoeol()
            self.window.chgat(y0, 0, self._width, curses.A_REVERSE)
        return None

    def clearln(self, y0):
        """Clear line y.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, 0)
            self.window.clrtoeol()
        return None

    def clrtoeol(self, x0, y0):
        """Clear line from (x, y) position.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, x0)
            self.window.clrtoeol()
        return None

    def clrtobot(self, x0, y0):
        """Clear terminal from (x, y) position.
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, x0)
            self.window.clrtobot()
        return None

    def hline(self, character, x0, y0, width):
        """Print hline in (x, y) position.
        :return: returns None
        """
        if self.window != None:
            for i in range(0, width):
                self.print_character(character, x0 + i, y0)
        return None

    def vline(self, character, x0, y0, height):
        """Print hline in (x, y) position.
        :return: returns None
        """
        if self.window != None:
            for i in range(0, height):
                self.print_character(character, x0, y0 + i)
        return None

    def flash(self):
        """Clear terminal from (x, y) position.
        :return: returns None
        """
        if self.window != None:
            curses.flash()
        return None

    def insertln(self, y0):
        """Request insert next line, moving down data
        :return: returns None
        """
        if self.window != None:
            self.window.move(y0, 0)
            self.window.insertln()
        return None

    def deleteln(self, y0 = -1):
        """Request delete line at line y
        :return: returns None
        """
        if self.window != None:
            if y0 >= 0:
                self.window.move(y0, 0)
            self.window.deleteln()
        return None

    def delch(self, x0, y0):
        """Request delete character at position x0, y0
        :return: returns None
        """
        if self.window != None:
            self.window.delch(y0, x0)
        return None

    def print_character(self, character, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        """Print a character. Choose a position. This affect to cursor.
        :return: returns nothing
        """
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

    def print_message(self, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        """Print a message string into its window. Choose a position. This affect to cursor.
        :return: returns nothing
        """
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                try:
                    self.window.move(y0, x0)
                except:
                    self.logger.warning("Overflow position x = %d, y = %d" % (x0, y0))
            # Print
            try:
                self.window.addstr(message, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        """Print a message string into a window. Choose y position, x automatically in the center. This affect to cursor.
        :return: returns nothing
        """
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

    def print_message_slow(self, message, x0 = -1, y0 = -1, inter_delay = 100, attributes = curses.A_NORMAL):
        """Print a message with delay between character. It cannot be skipped.
        :return: returns nothing
        """
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

    def print_border_type(self, border_type = BorderTypes.normal):
        """Print border with elements.
        # http://www.alanwood.net/unicode/box_drawing.html
        # http://www.alanflavell.org.uk/unicode/unidata25.html
        :return: returns nothing
        """
        if self.window != None:
            # Set border
            if border_type == BorderTypes.normal:
                self.window.border()
            elif border_type == BorderTypes.density:
                self.window.border(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.ACS_bot_lineOCK, curses.ACS_bot_lineOCK, curses.ACS_bot_lineOCK, curses.ACS_bot_lineOCK)
            elif border_type == BorderTypes.simplest:
                self.window.border("|", "|", "-", "-", " ", " ", " ", " ")
            elif border_type == BorderTypes.simple:
                top_left_corner = "·"
                top_right_corner = "·"
                bot_left_corner = "·"
                bot_right_corner = "·"
                top_line = "-"
                bot_line = "-"
                left_line = "|"
                right_line = "|"
                self.print_border(top_left_corner, top_right_corner, bot_left_corner, bot_right_corner, top_line, bot_line, left_line, right_line)
            elif border_type == BorderTypes.doubot_linee:
                top_left_corner = "\u2554"
                top_right_corner = "\u2557"
                bot_left_corner = "\u255A"
                bot_right_corner = "\u255D"
                top_line = "\u2550"
                bot_line = "\u2550"
                left_line = "\u2551"
                right_line = "\u2551"
                self.print_border(top_left_corner, top_right_corner, bot_left_corner, bot_right_corner, top_line, bot_line, left_line, right_line)
            elif border_type == BorderTypes.rounded:
                top_left_corner = "\u256D"
                top_right_corner = "\u256E"
                bot_left_corner = "\u2570"
                bot_right_corner = "\u256F"
                top_line = "\u2574"
                bot_line = "\u2576"
                left_line = "\u2575"
                right_line = "\u2577"
                self.print_border(top_left_corner, top_right_corner, bot_left_corner, bot_right_corner, top_line, bot_line, left_line, right_line)
            elif border_type == BorderTypes.quadrant:
                top_left_corner = "\u259B"
                top_right_corner = "\u259C"
                bot_left_corner = "\u2599"
                bot_right_corner = "\u259F"
                top_line = "\u2598"
                bot_line = "\u2596"
                left_line = "\u2598"
                right_line = "\u2597"
                self.print_border(top_left_corner, top_right_corner, bot_left_corner, bot_right_corner, top_line, bot_line, left_line, right_line)
            # Refresh
            self.window.refresh()
        return None

    def print_border(self, top_left_corner, top_right_corner, bot_left_corner, bot_right_corner, top_line, bot_line, left_line, right_line):
        """Print border using unicode character.
        :return: returns nothing
        """
        # Corners   1  top  2
        #           L       R
        #           3   bot 4

        # Custom parameters
        x_left = 0
        x_right = self._width - 1

        y_top = 0
        y_bot = self._height - 1

        self.print_character(top_left_corner, x_left, y_top)
        self.print_character(top_right_corner, x_right, y_top)
        self.print_character(bot_left_corner, x_left, y_bot)
        self.print_character(bot_right_corner, x_right, y_bot)

        self.hline(top_line, x_left + 1, y_top, x_right - 1)    # Top
        self.hline(bot_line, x_left + 1, y_bot, x_right - 1)    # Bot
        self.vline(left_line, x_left, 1, y_bot - 1)              # L
        self.vline(right_line, x_right, 1, y_bot - 1)             # R
        return None


    def print_frame(self, frame, x0 = 0, y0 = 0, attributes = curses.A_NORMAL):
        """Print an array of characters with colors as a matrix with row size in a position (x0, y0) with a offset between values
        :return: returns nothing
        """
        if self.window != None:
            current_col = 0
            # Set attributes
            self.window.attrset(attributes)
            # Set cursor position
            self.window.move(y0, x0)
            for i in range(0, frame.height):
                for j in range(0, frame.width):
                    value = i * frame.width + j
                    color_id = frame.colorpairs[value]
                    self.window.addch(frame.characters[value], curses.color_pair(color_id) )
                current_col = current_col + 1
                self.window.move(y0 + current_col, x0)
            # Restore attributes
            self.window.attroff(attributes)
            self.window.refresh()
        return None

    def fill_with_pattern(self, pattern):
        """Print foreground with a pattern from (0, 0).
        :return: returns nothing
        """
        if self.window != None:
            y_max, x_max = self.window.getmaxyx()
            lenght = len( pattern )
            times = (int)(x_max * y_max / lenght)
            self.window.move(0, 0)
            for i in range(0, times):
                self.print_message(pattern)
        return None

    def change_color(self, color_character, color_foreground):
        """Print foreground with color. *TODO* evaluate colors an change harcoded 7
        :return: returns nothing
        """
        if self.window != None:
            curses.init_pair(7, color_character, color_foreground)
            self.window.bkgd(curses.color_pair(7)) # Warning, color pair apply to all elements in curses, probably need a variabot_linee inside and change global this value!
            self.window.refresh()
        return None

    def waitforkey(self, print_text = False, x0 = -1, y0 = -1):
        """Wait for key. TODO remove?
        :return: returns None
        """
        # Print in window by default, check what need in a general way
        if x0 > -1 and y0 > -1:
            self.set_cursor_position(x0, y0)
        if print_text:
            self.print_message("\nPress any key to continue.")
        return self.window.getkey()

    def set_manual_draw(self, value):
        """If input true, draw call won't be processed. All draw in this widget must be done manually with self.window.
        :return: returns None
        """
        self._manual_draw = value
        return None

    def set_input_mode(self, value):
        """If input true, start taking keyboard events.
        :return: returns None
        """
        self.window.keypad(value)
        return None

    def get_character(self):
        """Wait for a character. Need set input mode true
        :return: returns None
        """
        # Set always NO DELAY?
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self.window.getch()

    def store_window(self):
        """Store cursor position, and all characters contained in element window
        :return: returns None
        """
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
        """Restore cursor position, and all characters contained in element window
        :return: returns None
        """
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
                        self.logger.warning("addch at i: %d, j: %d" % (i, j))
                    value += 1

            # Restore pointer and refresh
            self.window.move(self._cursor_y_copy, self._cursor_x_copy)
            self.window.refresh()
            self._window_copy = None
        return None

    def draw(self):
        """draw function prototype
        :return: returns None
        """
        success = False
        if not self._manual_draw:
            # Override me
            success = True
        return success

# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element

import random

class ToggleTable(Element):
    """ToggleTable: Table to set or toggle a character in cursor position with functions. Functionality at ToggleBoard class
    Coordinates
    [0,0]
        --------> X
        |   *   ·
        |       ·
    Y   v · · · (w, h)
    """
    def __init__(self, width, height, x0, y0, character = "*"):
        # Initialize all variables
        self._character = "*"
        self._table = {}

        # Assign
        super(ToggleTable, self).__init__(width, height, x0, y0)
        self._character = character
        return None

    def set_character(self, character):
        """Change character to be used when set or toggle.
        return: True if point is inside and is changed.
        """
        self._character = character
        return None

    def set(self, x, y):
        """Set point provided into table. Next call draw will be shown.
        return: True if point is inside and is changed.
        """
        inside = self.is_inside(x, y)
        if inside:
            self._table[x, y] = 1
            self.print_character(self._character, x, y)
        return inside

    def toggle(self, x, y):
        """Change a character for a space or viceverse at the location provided
        return: True if point is inside and is changed.
        """
        inside = self.is_inside(x, y)
        if inside:
            # If exist character in table, remove and empty character
            if (x, y) in self._table:
                del self._table[x, y]
                self.print_character(' ' , x, y)
            else:
                self._table[x, y] = 1
                self.print_character(self._character, x, y)
        return inside

    def generate_random_table(self):
        """Generate a random table
        return: None
        """
        self._table = {}
        for i in range(0, self._width):
            for j in range(0, self._height):
                if random.random() > 0.75:
                    self.set(i, j)
        return None

    def erase(self):
        """Erase table
        return: None
        """
        self.state = {}
        return None

    def draw(self):
        """Draw text if provided
        return: None
        """
        #self.window.addch(3, 3, self._character)
        #self.window.border()
        for i in range(0, self._width):
            for j in range(0, self._height):
                if (i, j) in self._table:
                    self.print_character(self._character, i, j)
                else:
                    self.print_character(' ' , i, j)
        #self.window.refresh()
        return None

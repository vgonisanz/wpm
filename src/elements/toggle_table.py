# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element

import random

"""
Table

[0,0]
    --------> X
    |       ·
    |       ·
Y   v · · · (w, h)

return: True if point is inside and is changed.
"""
class ToggleTable(Element):
    def __init__(self, width, height, x0, y0, character = "*"):
        # Initialize all variables
        _character = "*"
        _table = {}

        # Assign
        super(ToggleTable, self).__init__(width, height, x0, y0)
        self._character = character
        return None

    """
    Change character to be used

    return: True if point is inside and is changed.
    """
    def set_character(self, character):
        self._character = character
        return None

    """
    Set point provided into table. Next call draw will be shown.

    return: True if point is inside and is changed.
    """
    def set(self, x, y):
        inside = self.is_inside(x, y)
        if inside:
            self._table[x, y] = 1
            self.print_character(self._character, x-1, y-1)
        return inside

    """
    Change a character for a space or viceverse at the location provided

    return: True if point is inside and is changed.
    """
    def toggle(self, x, y):
        inside = self.is_inside(x, y)
        if inside:
            # If exist character in table, remove and empty character
            if (x, y) in self._table:
                del self._table[x, y]
                self.print_character(' ' , x-1, y-1)
            else:
                self._table[x, y] = 1
                self.print_character(self._character, x-1, y-1)
        return inside

    """
    Generate a random table

    return: None
    """
    def generate_random_table(self):
        self._table = {}
        for i in range(0, self._width):
            for j in range(0, self._height):
                if random.random() > 0.75:
                    self.set(i, j)
        return None

    """
    Erase table

    return: None
    """
    def erase(self):
        self.state = {}
        return None

    """
    Draw text if provided

    return: None
    """
    def draw(self):
        #self.window.addch(3, 3, self._character)
        #self.window.border()
        for i in range(0, self._width - 2):
            for j in range(0, self._height - 2):
                if (i, j) in self._table:
                    self.print_character(self._character, i + 1, j + 1)
                else:
                    self.print_character(' ' , i + 1, j + 1)
        self.window.refresh()
        return None

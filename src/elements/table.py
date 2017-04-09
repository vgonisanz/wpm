# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element

"""
Table

[0,0]
    --------> X
    |       ·
    |       ·
Y   v · · · (w, h)

return: True if point is inside and is changed.
"""
class Table(Element):
    title = ""
    width_data = 0
    height_data = 0
    x0 = 0
    y0 = 0
    cell_size = 0

    width_table = 0
    height_table = 0
    _x_offset = 2   # y_axi and separation line
    _y_offset = 3   # Title, separation line and x_axi
    _default_value = " "
    _data = [ [] ]

    """
    Initialize table element class. Always draw all elements with cell size

    return: True always
    """
    def __init__(self, width_data, height_data, x0, y0, cell_size = 1, default_value = " "):
        self.width_data = width_data
        self.height_data = height_data
        self.cell_size = cell_size
        self._default_value = default_value

        self.width_table = width_data * cell_size + self._x_offset
        self.height_table = height_data + self._y_offset

        super(Table, self).__init__(self.width_table, self.height_table, x0, y0)
        self._data = [[self._default_value for x in range(width_data)] for y in range(height_data)]
        return None

    """
    set a Title

    return: None
    """
    def set_title(self, title):
        self.title = title[:self.width_table]
        return None

    """
    set a data

    return: None
    """
    def set_data(self, data):
        self._data = data
        return None

    """
    Draw/Re-draw cell

    return: None
    """
    def draw_cell(self, i, j):
        value = self._data[j][i][:self.cell_size] # Crop to max cell size
        xpos = self._x_offset + i * self.cell_size
        ypos = self._y_offset + j
        self.print_message(value, xpos, ypos)
        return None

    """
    Draw X-axi

    return: None
    """
    def draw_axi_x(self):
        xpos_hline = self._x_offset - 1
        ypos_hline = self._y_offset - 1

        ypos_axi = self._y_offset - 2

        for i in range(0, self.width_data):
            value = "%d" % i
            xpos_axi = self._x_offset + i * self.cell_size

            self.print_message(value, xpos_axi, ypos_axi)
        self.window.hline(ypos_hline, xpos_hline, "-", self.width_table)
        return None

    """
    Draw Y-axi

    return: None
    """
    def draw_axi_y(self):
        xpos_vline = self._x_offset - 1
        ypos_vline = self._y_offset - 1

        xpos_axi = self._x_offset - 2

        for i in range(0, self.height_data):
            value = "%d" % i
            ypos_axi = self._y_offset + i

            self.print_message(value, xpos_axi, ypos_axi)

        self.window.vline(ypos_vline, xpos_vline, "|", self.height_table)
        return None

    """
    Draw complete table

    return: None
    """
    def draw(self):
        # Print title
        self.print_message(self.title, 0, 0)
        #self.print_message_center(self.title, 0)

        # Vertical line ad x = 0, y = 1
        self.draw_axi_x()
        self.draw_axi_y()

        # Print data cells
        for i in range(0, self.width_data):
            for j in range(0, self.height_data):
                self.draw_cell(i, j)
        self.window.refresh()
        return None

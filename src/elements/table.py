# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element

class Table(Element):
    """Table: Group of data tabulated.
    Diagram:
    [0,0]
        --------> X
        |       ·
        |       ·
    Y   v · · · (w, h)
    """
    def __init__(self, width_data, height_data, x0, y0, cell_size = 1, default_value = " "):
        """ Initialize table element class. Always draw all elements with cell size
        return: None
        """
        # Initialize all variables
        self.title = ""
        self.width_data = 0
        self.height_data = 0
        self.x0 = 0
        self.y0 = 0
        self.cell_size = 0
        #[' ','╶','╷','┌','╴','─','┐','┬','╵','└','│','├','┘','┴','┤','┼']│
        #self.corner
        self.corner_right_bot = "┌"
        self.corner_top_right_bot = "├"
        self.line_horizontal = "─"
        self.corner_bot_left = "┐"
        self.corner_top_bot_left = "┤"
        self.line_vertical = "│"
        self.corner_top_right = "└"
        self.corner_top_left = "┘"

        self.width_table = 0
        self.height_table = 0
        self._x_offset = 3   # y_axi and separation line
        self._y_offset = 3   # Title, separation line and x_axi
        self._cell_offset = 1
        self._bot_border = 1
        self._right_border = 1
        self._default_value = " "
        self._data = [ [] ]

        # Assign
        self.width_data = width_data
        self.height_data = height_data
        self.cell_size = cell_size
        self._default_value = default_value

        # Add +1 for border
        self.width_table = (width_data * cell_size) + (width_data * self._cell_offset - 1) + self._x_offset + self._right_border
        self.height_table = height_data + (self._cell_offset * height_data - 1) + self._y_offset + self._bot_border

        super(Table, self).__init__(self.width_table, self.height_table, x0, y0)
        self._data = [[self._default_value for x in range(width_data)] for y in range(height_data)]
        return None

    def set_title(self, title):
        """Set a Title to be printed
        return: None
        """
        self.title = title[:self.width_table]
        return None

    def set_data(self, data):
        """Set table data. Require (width_data x height_data) to be propertly drawn.
        return: None
        """
        self._data = data
        return None

    def draw_cell(self, i, j):
        """Draw/Re-draw cell
        return: None
        """
        value = self._data[j][i]
        length_data = len(str(value))
        if self.cell_size < length_data:
            length_data = self.cell_size # Crop to max cell size
        xpos = self._x_offset + i * (self.cell_size + self._cell_offset)
        ypos = self._y_offset + j * (1 + self._cell_offset)
        self.set_cursor_position(xpos, ypos)
        if isinstance( value, int ):
            self.print_character(value)
        else:
            for k in range(0, length_data):
                self.print_character(value[k])
        return None

    def draw_axi_x(self):
        """Draw X-axi
        return: None
        """
        xpos_hline = self._x_offset
        ypos_hline = self._y_offset - 1

        ypos_axi = self._y_offset - 2

        for i in range(0, self.width_data):
            value = "%2d" % i
            xpos_axi = self._x_offset + i * (self.cell_size + self._cell_offset)
            self.print_message(value, xpos_axi, ypos_axi)

        # Print all line
        self.hline(self.line_horizontal, xpos_hline, ypos_hline, self.width_table - self._bot_border - xpos_hline)
        self.hline(self.line_horizontal, xpos_hline, self.height_table - self._bot_border, self.width_table - self._bot_border - xpos_hline)
        return None

    def draw_axi_y(self):
        """Draw Y-axi and corners
        return: None
        """
        xpos_vline = self._x_offset - 1
        ypos_vline = self._y_offset - 1

        xpos_axi = self._x_offset - 3

        for i in range(0, self.height_data):
            value = "%2d" % i
            ypos_axi = self._y_offset + i * (1 + self._cell_offset)

            self.print_message(value, xpos_axi, ypos_axi)

        # Corners
        self.print_character(self.corner_top_right_bot, xpos_vline, ypos_vline)
        self.print_character(self.corner_top_bot_left, self.width_table - self._right_border, ypos_vline)
        self.print_character(self.corner_top_right, xpos_vline, self.height_table - self._bot_border)
        self.print_character(self.corner_top_left, self.width_table - self._right_border, self.height_table - self._bot_border)

        # Lines
        self.vline(self.line_vertical, xpos_vline, ypos_vline + 1, self.height_table - self._bot_border - ypos_vline - 1)
        self.vline(self.line_vertical, self.width_table - self._right_border, ypos_vline + 1, self.height_table - self._bot_border - ypos_vline - 1)
        return None

    def draw(self):
        """Draw complete table
        return: None
        """
        # Print title
        self.print_message(self.title, 0, 0)    # TODO add option?
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

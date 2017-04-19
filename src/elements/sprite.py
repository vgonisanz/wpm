# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element
from frame import Frame

class Sprite(Element):
    """Store a group of frames in a windows
    """
    def __init__(self, width, height, x0, y0):
        # Initialize all variables
        self._current_frame = 0
        self.frame_list = []

        # Assign
        super(Sprite, self).__init__(width, height, x0, y0)
        return None

    def add_frame(self, frame):
        self.frame_list.append(frame)
        return None

    def draw(self):
        """Draw current frame
        return: None
        """
        if not self.frame_list:
            return False
        else:
            self.print_frame(self.frame_list[self._current_frame], self._x, self._y)
            self._current_frame += 1
            max_frame = len(self.frame_list)
            if self._current_frame > max_frame:
                self._current_frame = 0
        return None

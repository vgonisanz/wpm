# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

from button import Button

class ButtonGroup(object):
    """ButtonGroup is a list of buttons to manage behavior into a widget. It is a dummy class.
    """
    def __init__(self):
        self._buttons = []
        self._current_button = 0
        return None

    def add_button(self, button):
        """Append a new button.
        :return: returns nothing
        """
        self._buttons.append(self._buttons)
        return None

    def select_button(self, button_id):
        """Try to select a button
        :return: result of the operation
        """
        result = False
        if button_id < len(self._buttons) and button_id >= 0:
            result = True
            self._buttons[self._current_button].set_focus(False)
            self._current_button = button_id
            self._buttons[self._current_button].set_focus(True)
            self._update_button_state()
        return result

    def next_button(self):
        """Try to select next button
        :return: result of the operation
        """
        next_id = self._current_button + 1
        if next_id > len(self._buttons):
            next_id = 0
        result = self.select_button(next_id)
        return result

    def previous_button(self):
        """Try to select previous button
        :return: result of the operation
        """
        previous_id = self._current_button - 1
        if previous_id < 0:
            previous_id = len(self._buttons) - 1
        result = self.select_button(previous_id)
        return result

    def get_button_size(self):
        """Check how many buttons are added
        :return: returns nothing
        """
        return len(self._buttons)

    def get_current_button(self):
        """Check how many buttons are added
        :return: returns nothing
        """
        return self._current_button

    def purge_buttons(self):
        """Remove all buttons added.
        :return: returns nothing
        """
        self._buttons = []
        return None

    def _update_button_state(self):
        """private method to redraw buttons
        :return: returns nothing
        """
        for button in self._buttons:
            button.draw()
        return None

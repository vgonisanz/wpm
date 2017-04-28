# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from eventobject import EventObject
from widget import ChildElement
from button import Button

class PopupOk(Widget):
    """Widget to open a window in front of the others. Remember store and restore that widget or element when call popup.run
    """
    def __init__(self, width, height, x0, y0, quit_key = ord('q'), print_title = False):
        # Initialize all variables
        self._title = " Popup with ok "
        self._print_title = False
        self._current_button = 0

        # Assign
        self._print_title = print_title
        super(PopupOk, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height
        self.background.logger.info("Creating popup ok")

        button_text = "Ok"
        button_width = 10
        button_x0 = x0 + int(width/2) - int(button_width/2)
        button_y0 = y0 + height - 2

        # Add textbox and button inside
        textbox = TextBox(width - 2 , height - 2, x0 + 1, y0 + 1)
        ok_button = Button(button_text, button_width, button_x0, button_y0)
        ok_button.set_on_push_callback(self.callback_quit)

        # Add children
        self.create_child("textbox", textbox)
        self.create_child("okbutton", ok_button)

        # Create event quit with q
        quit_description = "Press " + str(quit_key) + " to quit"
        event_quit = EventObject(quit_key, quit_description, self.callback_quit)
        self.add_event(event_quit)

        # Create event enter with ENTER
        event_enter = EventObject(10, "Press <ENTER> to select", self.callback_enter) # Shall be curses.KEY_ENTER = 10
        self.add_event(event_enter)

        # Add arrow controls
        event_up = EventObject(curses.KEY_UP, "Press <UP> to go up", self.callback_up)
        event_down = EventObject(curses.KEY_DOWN, "Press <DOWN> to go down", self.callback_down)
        event_left = EventObject(curses.KEY_LEFT, "Press <LEFT> to go left", self.callback_left)
        event_right = EventObject(curses.KEY_RIGHT, "Press <RIGHT> to go right", self.callback_right)
        self.add_event(event_up)
        self.add_event(event_down)
        self.add_event(event_left)
        self.add_event(event_right)
        return None

    def callback_quit(self):
        self.end_condition()
        return None

    def callback_up(self):
        self.select_button(0)
        return None

    def callback_left(self):
        self.select_button(0)
        return None

    def callback_right(self):
        self.select_button(0)
        return None

    def callback_down(self):
        self.select_button(0)
        return None

    def callback_enter(self):
        child = self.get_child("okbutton")
        child.push()
        return None

    def select_button(self, button_id):
        self._current_button = button_id
        child = self.get_child("okbutton")
        child.set_focus()
        child.draw()
        return None

    def set_title(self, title):
        """Set popup title
        return: None
        """
        self._title = title
        return None

    def set_message(self, message, centered = False):
        """Set a message into textbox
        return: None
        """
        child = self.get_child("textbox")
        child.set_text(message)
        if centered:
            child.set_cursor_center(True)
        return None

    def draw(self):
        """Re-draw element at current position
        return: None
        """
        # Update background
        self.background.clear()    # todo remove?
        self.background.window.border()
        if self._print_title:
            self.background.print_message_center(self._title, 0, curses.A_REVERSE)
        self.background.window.refresh()

        # Update foreground
        self.foreground.window.refresh()
        self._draw_children()   # Re-draw children if needed. Textbox by default.
        return None

    def run(self):
        """Run popup logic and autodraw
        return: None
        """
        self.background.logger.info("Run popup")
        self.draw()
        super(PopupOk, self).run()    # Widget autoiterate events
        return None

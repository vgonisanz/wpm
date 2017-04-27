# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from hwidget import HWidget
from textbox import TextBox
from widget import EventObject
from widget import ChildElement
from editabletextbox import EditableTextBox

class Question(HWidget):
    """Widget with ask a question and get the answer
    """
    def __init__(self, width, height, x0, y0):
        # Initialize all variables
        self._question_height = 0
        self._answer_height = 0
        self._answer_box = None

        # Assign
        super(Question, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height
        self._question_height = int(height/2)
        self._answer_height = int(height/2)

        # Add question inside
        question_box = TextBox(width, self._question_height, x0, y0)
        question_box_child = ChildElement("question", question_box)
        self.add_child(question_box_child)

        # Add answer inside
        self._answer_box = EditableTextBox(width, self._answer_height, x0, self._answer_height + 1)
        self._answer_box.draw()

        self.set_menu_options()
        self.background.logger.debug("question.newwin with height: %d, width: %d, x0: %d, y0: %d" % (self.background._width, self.background._height, self.background._x, self.background._y))
        help_message =  "Push e to edit question\n" + \
                        "Push ENTER after write question\n" + \
                        "Push q to quit\n"
        self.create_help(help_message)
        return None

    def callback_quit(self):
        """Callback to set true end condition and left run bucle.
        :return: None
        """
        self.end_condition()
        return None

    def set_menu_options(self):
        """Purge events and add quit and run edit mode
        :return: None
        """
        self.purge_events()

        # Create event quit with q
        event_quit = EventObject(ord('q'), "Press q to quit", self.callback_quit)
        self.add_event(event_quit)

        # Create event edit answer with e
        event_edit = EventObject(ord('e'), "Press e to edit mode", self.run_edit_mode)
        self.add_event(event_edit)
        return None

    def run_edit_mode(self):
        """Run child editabletextbox until finish
        return: None
        """
        self._answer_box.run()
        return None

    def set_question_text(self, text, centered = False):
        """Set text into question textbox
        return: None
        """
        child = self.get_child("question")
        child.set_text(text)
        return None

    def get_answer(self):
        """Get last answer
        return: None
        """
        return self._answer_box.get_text()

    def draw(self):
        """Re-draw element at current position
        return: None
        """
        # Border
        self.background.clear() 
        self.foreground.clear()    # todo remove?
        #self.foreground.window.border()
        self.foreground.window.refresh()

        # Print message
        self._draw_children()   # Re-draw children if needed. Textbox by default.
        return None

    def run(self):
        """Run question logic and autodraw
        return: None
        """
        self.background.logger.info("Run question")
        self.draw()
        super(Question, self).run()    # Widget autoiterate events
        return None

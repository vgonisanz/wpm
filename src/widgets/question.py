import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from widget import EventObject
from widget import ChildElement
from editabletextbox import EditableTextBox

class Question(Widget):
    _question_height = 0
    _answer_height = 0
    _answer_box = None

    def __init__(self, width, height, x0, y0):
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
        return None

    def callback_quit(self):
        self.end_condition()
        return None

    def set_menu_options(self):
        self.purge_events()

        # Create event quit with q
        event_quit = EventObject(ord('q'), self.callback_quit)
        self.add_event(event_quit)

        # Create event edit answer with e
        event_edit = EventObject(ord('e'), self.run_edit_mode)
        self.add_event(event_edit)
        return None

    """
    Run child editabletextbox until finish

    return: None
    """
    def run_edit_mode(self):
        self._answer_box.run()
        return None

    """
    Set text into question textbox

    return: None
    """

    def set_question_text(self, text, centered = False):
        child = self.get_child("question")
        child.set_text(text)
        return None

    """
    Get last answer

    return: None
    """

    def get_answer(self):
        return self._answer_box.get_text()
    """
    Re-draw element at current position

    return: None
    """

    def draw(self):

        # Border
        self._background.clear()    # todo remove?
        #self._background.window.border()
        self._background.window.refresh()

        # Print message
        self._draw_children()   # Re-draw children if needed. Textbox by default.
        return None

    """
    Run question logic and autodraw

    return: None
    """

    def run(self):
        self.draw()
        super(Question, self).run()    # Widget autoiterate events
        return None

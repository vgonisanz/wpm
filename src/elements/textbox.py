import curses   # TODO remove for my colors or color pairs.
from element import Element

class TextBox(Element):
    _text = ""

    def __init__(self, width, height, x0, y0, text = ""):
        super(TextBox, self).__init__(width, height, x0, y0)
        self._text = text
        return None

    def set_text(self, text):
        self._text = text
        return None

    def get_text(self):
        return self._text

    """
    Draw text if provided

    return: None
    """

    def draw(self):
        self.print_message(self._text)
        return None

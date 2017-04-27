# -*- coding: utf-8 -*-
class Frame(object):
    """Initialize frame class. If only provide width and colors, characters will be value at same_character. By default is a space
    Use ASCII (0 - 127) or unicode (\u0000 - \u9999) as character. Extended ASCII not allowed. *TODO* sample testing ranges.
    same_character by default is ASCII 32 = space
    """
    def __init__(self, width, colorpair_array, character_array = [], same_character = 32):
        # Initialize all variables
        self.width = 0
        self.height = 0
        self.size = 0
        self.characters = []
        self.colorpairs = []

        # Assign
        self.size = len(colorpair_array)
        self.width = width
        self.height = int(self.size / width)
        self.colorpairs = colorpair_array

        if not character_array:
            self.characters = [ same_character ] * self.size
        else:
            self.characters = character_array
        return None

    def is_valid():
        valid = False
        number_of_characters = len(self.characters)
        number_of_colors = len(self.colorpairs)
        if number_of_characters == number_of_colors:
            valid = True
        return valid

class Sprite(object):
    width = 0
    height = 0
    size = 0
    characters = []
    colorpairs = []

    """
    Initialize sprite class. If only provide width and colors, characters will be value at same_character. By default is a space
    Use ASCII code as character.

    return: True always
    """
    def __init__(self, width, colorpair_array, character_array = [], same_character = " "):
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
        if self.number_of_characters == self.number_of_colors:
            valid = True
        return valid

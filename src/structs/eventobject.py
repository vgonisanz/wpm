# -*- coding: utf-8 -*-
class EventObject(object):
    """EventObject is a Struct. It is added into a widget with add_event.
    It is automatically call with default event bucle into run directive.
    When you push a key, a event occur.
    It store:
        * Key: Character
        * Description: Small description to be printed if needed
        * Action: Callback to be call if character is pressed
        * Args: Arguments for the callback
    """
    def __init__(self, key_input, description = "", action_input = None, args_input = None):
        # check type() is type TODO

        # Initialize all variables
        self.key = None
        self.description = ""
        self.action = None
        self.args = []

        # Assign
        self.key = key_input
        self.description = description
        self.action = action_input
        self.args = args_input
        return None

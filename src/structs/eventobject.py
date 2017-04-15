# -*- coding: utf-8 -*-
class EventObject(object):
    """EventObject is a Struct. It is added into a widget with add_event.
    It is automatically call with default event bucle into run directive.
    When you push a key, a event occur.
    It store:
        * Key: Character
        * Action: Callback to be call if character is pressed
        * Args: Arguments for the callback
        * Description: Small description to be printed if needed
    """
    def __init__(self, key_input, action_input, args_input = None):
        # check type() is type TODO
        # Initialize all variables
        self.description = ""
        self.key = None
        self.action = None
        self.args = []

        # Assign
        self.key = key_input
        self.action = action_input
        self.args = args_input
        return None

# -*- coding: utf-8 -*-
class ChildElement(object):
    """ChildElement is a Struct.
    It is added into a widget with add_child.
    It is automatically call with default event bucle into run directive.
    It store:
        * Key: Character
        * Action: Callback to be call if character is pressed
        * Args: Arguments for the callbackcter is pressed
        * Args: Arguments for the callback
    """
    def __init__(self, child_id, child_element):
        # Initialize all variables
        self.cid = ""
        self.child_element = None

        # Assign
        self.cid = child_id
        self.celement = child_element
        return None

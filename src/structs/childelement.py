"""
ChildElement is a Struct.
It is added into a widget with add_child.
It is automatically call with default event bucle into run directive.
It store:
    * Key: Character
    * Action: Callback to be call if character is pressed
    * Args: Arguments for the callbackcter is pressed
    * Args: Arguments for the callback
"""
class ChildElement(object):
    cid = ""
    celement = None

    def __init__(self, child_id, child_element):
        self.cid = child_id
        self.celement = child_element
        return None

"""
OptionStruct is a Struct. It is added into a widget child with options using add_option.
A option shall be called manually. It is not like a event.
It store:
    * Text: String with option text
    * Action: Callback to be call if character is pressed
    * Args: Arguments for the callback
"""
class OptionStruct(object):
    text = ""
    action = None
    args = []

    def __init__(self, text_input, action_input = None, args_input = None):
        # check type() is type
        self.text = text_input
        self.action = action_input
        self.args = args_input
        return None

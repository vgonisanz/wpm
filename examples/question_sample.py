import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from question import Question

# Configuration
help_message = "Press q to quit\n Press e to edit answer"
help_x0 = 1
help_y0 = 1

question_width = 30
question_height = 10
question_x0 = 1
question_y0 = 5
question_text = "Do you like this example?"

# Variables
wpm = None
background = None
question = None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()
    return None

def print_help():
    background.print_message(help_message, help_x0, help_y0)
    return None

def create_question():
    global question

    # Create test question and run
    question = Question(question_width, question_height, question_x0, question_y0)
    question.set_question_text(question_text)
    question.run()
    return None

def write_last_answer():
    last_answer = question.get_answer()
    background.clear()
    background.print_message("Last answer: %s" % last_answer)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    print_help()
    create_question()
    write_last_answer()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

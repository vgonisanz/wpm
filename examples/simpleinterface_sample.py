import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from simpleinterface import SimpleInterface
from widget import EventObject
from menu import Menu
from toggle_board import ToggleBoard
from optionstruct import OptionStruct

# Configuration
interface_title = "My first interface"
interface_print_title = True

menu_title = "Buy menu"
menu_instructions = "Use arrows to move, enter to select"
menu_x0_offset = 1
menu_y0_offset = 1

tb_title = "Toggle board"

# Variables
interface = None
interface_background = None

buy_menu = None
toggle_board = None

def initialize():
    global wpm

    wpm = Wpm(True)
    wpm.logger.info("initialize")
    return None

def create_interface():
    global interface
    global interface_background

    # All screen widget
    interface_x0 = 0
    interface_y0 = 0
    interface_width, interface_height = wpm.get_window_size()

    interface = SimpleInterface(interface_width, interface_height, interface_x0, interface_y0, interface_title, interface_print_title)
    interface_background = interface.get_background()

    return None

def create_menu_widget():
    global buy_menu

    # Create options
    option_2 = OptionStruct("Option 2, do nothing")
    option_3 = OptionStruct("Option 3, me neither")

    # Create test menu and run
    menu_width, menu_height, menu_x0, menu_y0 = interface.get_secondary_widget_size()

    buy_menu = Menu(menu_width, menu_height, menu_x0, menu_y0, menu_title, menu_instructions)
    buy_menu.add_option(option_2)
    buy_menu.add_option(option_3)

    # Add key to interface
    event_run_buy = EventObject(ord('b'), callback_buy)
    event_run_buy.description = "Press <b> to launch buy menu"
    interface.add_event(event_run_buy)
    return None

def create_toggleboard_widget():
    global toggle_board

    # Create test tt and run
    tb_width, tb_height, tb_x0, tb_y0 = interface.get_secondary_widget_size()

    toggle_board = ToggleBoard(tb_width, tb_height, tb_x0, tb_y0, tb_title)

    # Add key to interface
    event_toggle_board = EventObject(ord('t'), callback_toggle_board)
    event_toggle_board.description = "Press <t> to launch toggle board"
    interface.add_event(event_toggle_board)
    return None


def run_interface():
    interface.run()
    return None

def callback_buy():
    option_index = buy_menu.run()
    interface.print_command("Option selected: %d" % option_index)
    return None

def callback_toggle_board():
    toggle_board.run()
    interface.print_command("Toggle board end")
    return None

def main(stdscr):
    initialize()
    create_interface()
    create_menu_widget()
    create_toggleboard_widget()
    run_interface()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

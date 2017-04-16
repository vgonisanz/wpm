import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from simpleinterface import SimpleInterface
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
    main_menu_list = {}
    main_menu_list['title'] = "Choose a weapon to buy"
    main_menu_list['names'] = ["Pistols", "Shotguns", "SMG", "Rifles", "MachineGuns", "Primary ammo", "Secondary ammo", "Equipment"]

    submenu_1_list = {}
    submenu_1_list['title'] = "Choose a pistol"
    submenu_1_list['names'] = ["USP .45ACP Tactical", "Glock 18C Select Fire", "Desert Eagle .50 AE", "SIG P228", "FN Five-Seven"]
    submenu_1_list['prices'] = ["400$", "400$", "650$", "600$", "750$"]

    submenu_2_list = {}
    submenu_2_list['title'] = "Choose a shotgun"
    submenu_2_list['names'] = ["M3 Super 90 Combat", "XM1014"]
    submenu_2_list['prices'] = ["1700$", "3000$"]

    submenu_3_list = {}
    submenu_3_list['title'] = "Choose a sub machine gun"
    submenu_3_list['names'] = ["MP5 Navy", "Streyr TMP", "FN P90", "MAC-10", "H&K UMP"]
    submenu_3_list['prices'] = ["1500$", "1250$", "2350$", "1400$", "1700$"]

    submenu_4_list = {}
    submenu_4_list['title'] = "Choose a rifle"
    submenu_4_list['names'] = ["AK47", "M4A1 Carbine/COLT", "SG552 Commando", "Steyr AUG", "Steyr Scout Sniper Rifle", "Artic Warfare Magnum", "SIG SG-550", "G3/SG1 Sniper Rifle"]
    submenu_4_list['prices'] = ["2500$", "3100$", "3500$", "3500$", "2750$", "4750$", "4200$", "5000$"]

    submenu_5_list = {}
    submenu_5_list['title'] = "Choose a machineGun"
    submenu_5_list['names'] = ["FN M249 PARA"]
    submenu_5_list['prices'] = ["5750$"]

    submenu_8_list = {}
    submenu_8_list['title'] = "Choose a equipment"
    submenu_8_list['names'] = ["Armor", "Armor|Helmet", "Flash", "Grenade", "Smoke", "Defuser", "NightVision", "Shield"]
    submenu_8_list['prices'] = ["650$", "1000$", "200$", "300$", "300$", "200$", "1250$", "1000$"]

    option_2 = OptionStruct("Option 2, do nothing")
    option_3 = OptionStruct("Option 3, me neither")

    # Create test menu and run
    menu_width, menu_height, menu_x0, menu_y0 = interface.get_secondary_widget_size()

    buy_menu = Menu(menu_width, menu_height, menu_x0, menu_y0, main_menu_list['title'])
    for submenu in main_menu_list['names']:
        buy_menu.create_option(submenu)

    # Add key to interface
    interface.create_event(ord('b'), "Press <b> to launch buy menu", callback_buy)
    return None

def create_toggleboard_widget():
    global toggle_board

    # Create test tt and run
    tb_width, tb_height, tb_x0, tb_y0 = interface.get_secondary_widget_size()

    toggle_board = ToggleBoard(tb_width, tb_height, tb_x0, tb_y0, tb_title)

    # Add key to interface
    interface.create_event(ord('t'), "Press <t> to launch toggle board", callback_toggle_board)
    return None


def run_interface():
    interface.run()
    return None

def callback_buy():
    interface.clear_events()
    interface.print_command("Buy menu launched")
    option_index = buy_menu.run()
    interface.draw_events()
    interface.print_command("Option selected: %d" % option_index)
    return None

def callback_toggle_board():
    interface.clear_events()
    interface.print_command("Toggle board launched")
    toggle_board.run()
    interface.draw_events()
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

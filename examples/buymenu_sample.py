import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from menu import Menu
from optionstruct import OptionStruct

# Configuration
buymenu_width = 30
buymenu_height = 15
buymenu_x0 = 5
buymenu_y0 = 5
buymenu_title = "Buy menu"
buymenu_instructions = "Use arrows to move, ENTER to select, q to quit"
buymenu_centered = True

# Variables
wpm = None
screen = None
buymenu = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()
    return None

def create_buymenu():
    global buymenu

    # Create submenu 1
    submenu_1_list = {}
    submenu_1_list['title'] = "Choose a pistol"
    submenu_1_list['names'] = ["USP .45ACP Tactical", "Glock 18C Select Fire", "Desert Eagle .50 AE", "SIG P228", "FN Five-Seven"]
    submenu_1_list['callbacks'] = [print_result, print_result, print_result, print_result, print_result]
    submenu_1_list['args'] = ["400$", "400$", "650$", "600$", "750$"]
    submenu_1 = create_menu(submenu_1_list['title'], submenu_1_list['names'], submenu_1_list['callbacks'], submenu_1_list['args'])

    submenu_2_list = {}
    submenu_2_list['title'] = "Choose a shotgun"
    submenu_2_list['names'] = ["M3 Super 90 Combat", "XM1014"]
    submenu_2_list['callbacks'] = [print_result, print_result]
    submenu_2_list['args'] = ["1700$", "3000$"]
    submenu_2 = create_menu(submenu_2_list['title'], submenu_2_list['names'], submenu_2_list['callbacks'], submenu_2_list['args'])

    submenu_3_list = {}
    submenu_3_list['title'] = "Choose a sub machine gun"
    submenu_3_list['names'] = ["MP5 Navy", "Streyr TMP", "FN P90", "MAC-10", "H&K UMP"]
    submenu_3_list['callbacks'] = [print_result, print_result, print_result, print_result, print_result]
    submenu_3_list['args'] = ["1500$", "1250$", "2350$", "1400$", "1700$"]
    submenu_3 = create_menu(submenu_3_list['title'], submenu_3_list['names'], submenu_3_list['callbacks'], submenu_3_list['args'])

    submenu_4_list = {}
    submenu_4_list['title'] = "Choose a rifle"
    submenu_4_list['names'] = ["AK47", "M4A1 Carbine/COLT", "SG552 Commando", "Steyr AUG", "Steyr Scout Sniper Rifle", "Artic Warfare Magnum", "SIG SG-550", "G3/SG1 Sniper Rifle"]
    submenu_4_list['callbacks'] = [print_result, print_result, print_result, print_result, print_result, print_result, print_result, print_result]
    submenu_4_list['args'] = ["2500$", "3100$", "3500$", "3500$", "2750$", "4750$", "4200$", "5000$"]
    submenu_4 = create_menu(submenu_4_list['title'], submenu_4_list['names'], submenu_4_list['callbacks'], submenu_4_list['args'])

    submenu_5_list = {}
    submenu_5_list['title'] = "Choose a machineGun"
    submenu_5_list['names'] = ["FN M249 PARA"]
    submenu_5_list['callbacks'] = [print_result]
    submenu_5_list['args'] = ["5750$"]
    submenu_5 = create_menu(submenu_5_list['title'], submenu_5_list['names'], submenu_5_list['callbacks'], submenu_5_list['args'])

    submenu_8_list = {}
    submenu_8_list['title'] = "Choose a equipment"
    submenu_8_list['names'] = ["Armor", "Armor|Helmet", "Flash", "Grenade", "Smoke", "Defuser", "NightVision", "Shield"]
    submenu_8_list['callbacks'] = [print_result, print_result, print_result, print_result, print_result, print_result, print_result, print_result]
    submenu_8_list['args'] = ["650$", "1000$", "200$", "300$", "300$", "200$", "1250$", "1000$"]
    submenu_8 = create_menu(submenu_8_list['title'], submenu_8_list['names'], submenu_8_list['callbacks'], submenu_8_list['args'])

    # Create test buymenu and run
    main_menu_list = {}
    main_menu_list['title'] = "Choose a weapon to buy"
    main_menu_list['names'] = ["Pistols", "Shotguns", "SMG", "Rifles", "MachineGuns", "Primary ammo", "Secondary ammo", "Equipment"]
    main_menu_list['callbacks'] = [launch_menu, launch_menu, launch_menu, launch_menu, launch_menu, print_result, print_result, launch_menu]
    main_menu_list['args'] = [submenu_1, submenu_2, submenu_3, submenu_4, submenu_5, ["Primary ammo", "100$"], ["Secondary ammo", "60$"], submenu_8]

    main_menu = create_menu(main_menu_list['title'], main_menu_list['names'], main_menu_list['callbacks'], main_menu_list['args'])
    main_menu.run()
    screen.waitforkey()
    return None


def create_menu(title, name_list, callback_list = None, args_list = None):
    menu = Menu(buymenu_width, buymenu_height, buymenu_x0, buymenu_y0, title)

    # Create options
    for i in range(0, len(name_list)):
        name = name_list[i]
        callback = None
        args = None
        if callback_list:
            callback = callback_list[i]
        if args_list:
            args = args_list[i]
        option = OptionStruct(name, callback, args)
        menu.add_option(option)
    return menu

def launch_menu(menu):
    menu.run()
    return None

def print_result(money):
    """Maybe menu implement a callback with a pointer to itself to read info.
    """
    screen.print_message("You buy for: %s" % money, 0, 0)
    screen.waitforkey()
    screen.clear()
    return None

def main(stdscr):
    initialize()
    create_buymenu()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

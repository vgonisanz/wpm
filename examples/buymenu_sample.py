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
buymenu_height = 10
buymenu_x0 = 5
buymenu_y0 = 5
buymenu_title = "Buy menu"
buymenu_instructions = "Use arrows to move, ENTER to select, q to quit"
buymenu_centered = True

# Variables
wpm = None
screen = None
buymenu = None

def callback_hello():
    screen.print_message("Hello")
    #screen.waitforkey()
    return None

def callback_print(message):
    screen.print_message(message)
    #screen.waitforkey()
    return None

def callback_quit():
    buymenu.callback_quit()
    return None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()
    return None

def create_buymenu():
    global buymenu

    # TODO remove
    option_0 = OptionStruct("Option 0", callback_hello)
    option_1 = OptionStruct("Option 1", callback_print, "Hello world")
    option_2 = OptionStruct("Option 2, do nothing")
    option_3 = OptionStruct("Option 3, me neither")
    option_4 = OptionStruct("Option quit", callback_quit)

    # Create options
    main_menu_list = {}
    main_menu_list['title'] = "Choose a weapon to buy"
    main_menu_list['names'] = ["Pistols", "Shotguns", "SMG", "Rifles", "MachineGuns", "Primary ammo", "Secondary ammo", "Equipment"]
    main_menu_list['callbacks'] = [launch_menu, launch_menu, launch_menu, launch_menu, launch_menu, launch_menu, print_result, print_result, launch_menu]
    main_menu_list['args'] = [None, None, None, None, None, None, ["Primary ammo", "100$"], ["Secondary ammo", "60$"], None]

    submenu_1_list = {}
    submenu_1_list['title'] = "Choose a pistol"
    submenu_1_list['names'] = ["USP .45ACP Tactical", "Glock 18C Select Fire", "Desert Eagle .50 AE", "SIG P228", "FN Five-Seven"]
    submenu_1_list['callbacks'] = [print_result, print_result, print_result, print_result, print_result]
    submenu_1_list['args'] = ["400$", "400$", "650$", "600$", "750$"]

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

    # Create test buymenu and run
    main_menu_options = create_option_list(main_menu_list['names'], main_menu_list['callbacks'], main_menu_list['args'])
    main_menu = create_menu(main_menu_list['title'], main_menu_options)
    main_menu.run()

    #submenu1_option_list = create_option_list(submenu_1_list['names'], submenu_1_list['callbacks'], submenu_1_list['args'])
    #submenu1 = create_menu(submenu_1_list['title'], submenu1_option_list)
    #submenu1.run()

    #buymenu.add_option(submenu1)

    #buymenu = Menu(buymenu_width, buymenu_height, buymenu_x0, buymenu_y0, "title")
    #buymenu.add_option(option_0)
    #option_index = buymenu.run()

    #screen.clear()
    screen.waitforkey()
    return None

def create_option_list(name_list, callback_list = None, args_list = None):
    option_list = []
    for i in reversed(range(0, len(name_list))):
        name = name_list[i]
        callback = None
        args = None
        if callback_list:
            callback = callback_list[i]
        if args_list:
            args = args_list[i]
        option = OptionStruct(name, callback, args)
    option_list.append(option)
    return option_list

def create_menu(title, option_list):
    menu = Menu(buymenu_width, buymenu_height, buymenu_x0, buymenu_y0, title)
    for option in option_list:
        menu.add_option(option)
    return menu

def launch_menu(menu):
    menu.run()
    return None

def print_result(money):
    screen.print_message("Money: %s" % money, 0, 0)
    screen.waitforkey()
    return None

def main(stdscr):
    initialize()
    #print_help()
    #print_result("test")
    create_buymenu()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))

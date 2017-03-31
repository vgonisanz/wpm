import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))
from curses import wrapper
from cursesManager import CursesManager

def launch_submenu(data):
    message = "Canceled purchase"
    menu = cm.create_menu(secondary_window, data['title'], data['names'], "")
    option_choose = menu.run()
    # If user cancel, default message
    if option_choose >= 0:
        message = "Launching submenu: " + data['names'][option_choose]
        simple_ui.print_command(message)
    if option_choose == 0:
        launch_printing_submenu(submenu_1_list)
    if option_choose == 1:
        launch_printing_submenu(submenu_2_list)
    if option_choose == 2:
        launch_printing_submenu(submenu_3_list)
    if option_choose == 3:
        launch_printing_submenu(submenu_4_list)
    if option_choose == 4:
        launch_printing_submenu(submenu_5_list)
    if option_choose == 5:
        message = "You paid 200$ for some " + data['names'][option_choose]
        simple_ui.print_command(message)
    if option_choose == 6:
        message = "You paid 75$ for some " + data['names'][option_choose]
        simple_ui.print_command(message)
    if option_choose == 7:
        launch_printing_submenu(submenu_8_list)
    return None

def launch_printing_submenu(data):
    message = "Canceled purchase"
    menu = cm.create_menu(secondary_window, data['title'], data['names'], "")
    option_choose = menu.run()
    if option_choose >= 0:
        message = "You paid " + data['prices'][option_choose] + " for a " + data['names'][option_choose]
    simple_ui.print_command(message)

def launch_ui(stdscr):
    global simple_ui
    global secondary_window

    # Create UI
    simple_ui = cm.create_simple_ui(stdscr, options, title)
    simple_ui.draw()
    secondary_window = simple_ui.get_secondary_window()

    # Interactive screen
    quit_ui = False
    while not quit_ui:
        # Update and quit if needed
        simple_ui.clear_secondary_window()
        simple_ui.draw()

        # Check if any option is selected
        event = cm.getch()
        if event == ord('h'):
            simple_ui.print_command(help_message)
        if event == ord('b'):
            simple_ui.print_command(instructions_message)
            launch_submenu(main_menu_list)
        if event == ord('q') or event == 28:
            quit_ui = True
    return None

def main(stdscr):
    # Edit global variables
    global cm

    # Initial curses manager
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.set_cursor_mode(0)

    launch_ui(stdscr)

    cm.cleanup()
    return None

if __name__ == "__main__":
    # Global variables
    cm = None
    simple_ui = None
    secondary_window = None

    title = "This is an advanced interface"
    help_message = "Do you need help?"
    instructions_message = "Use arrow keys to move, ENTER to select, q or ESC to abort."
    options = []
    options.append("Push <h> to see help")
    options.append("Push <q> to quit")
    options.append("Push <b> to buy")

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

    wrapper(main)

        # Create from simple menu? Json auto menu?
        # final call or selected value? array of values? <-- Good idea!

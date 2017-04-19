

"""
Selective clear
"""
def step6(stdscr):
    message = "Fill and clear.\n1.- Let's put text in all terminal"
    message2 = "2.- Let's clean from (4, 5) to end of line"
    message3 = "3.- Let's clean from (6, 7) to end of terminal"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message(message)
    cm.waitforkey()
    cm.fill_with_pattern("#===#")
    cm.waitforkey()
    cm.print_message_at(message2, 0, 0)
    cm.clrtoeol(4, 5)
    cm.waitforkey()
    cm.print_message_at(message3, 0, 0)
    cm.clrtobot(6, 7)
    cm.waitforkey()
    cm.cleanup()
    return None
"""
# Create a book
"""
def step8(stdscr):
    title = "My first book"
    pages = []
    author = "vgonisanz"
    page1 = "This is my first page."
    page2 = "This is my second page."
    page3 = "This is my third page."
    page4 = "This is my last page."
    pages.append(page1)
    pages.append(page2)
    pages.append(page3)
    pages.append(page4)

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_book(title, pages, author)
    cm.waitforkey()
    cm.cleanup()
    return None

def step9(stdscr):
    title = "My first menu"
    options = []
    option1 = "Option 1"
    option2 = "Option 2"
    option3 = "Option 3"
    options.append(option1)
    options.append(option2)
    options.append(option3)
    instructions = "Use arrow keys to move, ENTER to select, q or ESC to abort."

    cm = CursesManager()
    menu = cm.create_menu(stdscr, title, options, instructions)
    option_choose = menu.run()
    cm.print_message_at("Option chosen: %s" % option_choose, 1, 6)
    cm.waitforkey()
    cm.cleanup()
    return None

# Window demo
def step10(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    win0, win1, win2, win3 = cm.print_4windows()
    win0.refresh()
    win1.refresh()
    win2.refresh()
    win3.refresh()
    cm.set_current_window(win0)
    cm.waitforkey(0, 5)
    y_max, x_max = win3.getmaxyx()
    win3.addch(y_max - 2, x_max - 2, "f")
    win3.refresh()
    cm.waitforkey(0, 5)
    cm.cleanup()
    return None

# Create question and get answer
def step11(stdscr):
    question = "What is your name?"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    answer = cm.print_question(question, True, 1, 1, 1, 2)
    cm.print_message(" Your answer was: " + answer)
    cm.waitforkey()
    cm.cleanup()
    return None

# Playing with cursor
def step12(stdscr):
    ch = "a"
    message = "Lets try use cursor"
    message_cursor = "Cursor at x=%d and y=%d"
    #message_max = "win is width = %s and height = %s"

    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message_center(message, 0)
    x_max, y_max = cm.get_max_cursor()
    # Invalid value
    x = -1
    y = -1
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? (1,0) after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 1)
    cm.waitforkey()
    # Invalid value
    x = 20000
    y = 20000
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 2)
    cm.waitforkey()
    # Valid value
    x = (int)(x_max/2)
    y = (int)(y_max/2)
    # Corrected!
    x, y = cm.get_valid_cursor(x, y)
    cm.print_ch_at(ch, x, y, curses.A_REVERSE)
    # Where is? in the middle after write a character
    x_cur, y_cur = cm.get_cursor()
    cm.print_message_at(message_cursor % (x_cur, y_cur), 1, 3)
    cm.waitforkey()
    cm.cleanup()
    return None

def step13(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    title = "This is a progress bar"
    progress = 0
    bar_width = 30
    cm.print_message_at(title, 5, 5)
    while progress <= 100:
        cm.print_progress_bar(progress, 5, 6, bar_width)
        progress = progress + 1
        cm.rwait(100)
    cm.waitforkey()
    cm.cleanup()
    return None

def step14(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    title = "This is a matrix of characters"
    character_array = ["a", "b", "c", "a", "b", "c", "a", "b", "d"]
    cm.print_message_at(title, 0, 0)
    cm.print_character_array(character_array, 3, 0, 1, 1)
    cm.waitforkey()
    cm.cleanup()
    return None

def step15(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()
    cm.print_message("Printing different ascii characters...\n")
    locale.setlocale(locale.LC_ALL, "")
    for i in range(0,50):
        for j in range(1,16):
            s = unichr(16*i+j)
            stdscr.addstr(s.encode("utf-8"))
        stdscr.addstr("\n Index %d: " % i)
    #stdscr.addstr(u"\u27a0".encode("utf-8"))
    stdscr.getch()
    #for i in range(1,300):
    #    cm.print_ch(i)
    #cm.print_message_at(, 0, 0)
    cm.waitforkey()
    cm.cleanup()
    return None

def step16(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    cm.set_cursor_mode(0)

    title = "This is a simple interface"
    hello_message = "You choose say hello"
    info_message = "You choose more info"
    info_message_extended = " Well, you want more info.\n  This is a secondary window.\n  You can write here using sec_window object."
    options = []
    options.append("Push <q> to quit")
    options.append("Push <c> to clear last command")
    options.append("Push <h> to say hello")
    options.append("Push <i> to print more info")

    # Initial screen
    simple_ui = cm.create_simple_ui(stdscr, options, title)
    simple_ui.draw()

    # Get secondary window
    sec_win = simple_ui.get_secondary_window()

    # Interactive screen
    quit_ui = False
    while not quit_ui:
        # Update and quit if needed
        simple_ui.draw()

        # Check if any option is selected
        event = cm.getch()
        if event == ord('h'):
            simple_ui.print_command(hello_message)
        if event == ord('c'):
            simple_ui.print_command("")
            sec_win.clear()
            sec_win.refresh()
            sec_win.border()
        if event == ord('i'):
            simple_ui.print_command(info_message)
            # Extend info in second window
            cm.set_current_window(sec_win)
            cm.print_message_at(info_message_extended, 1, 5)
            cm.print_border_type()
            cm.rwait(1)
            cm.set_current_window(stdscr)

        if event == ord('q') or event == 28:
            quit_ui = True

    cm.cleanup()
    return None

def step17(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    cm.waitforkey()
    cm.cleanup()
    return None

# Print constants,
# Note: These are available only after initscr() has been called.
def step18(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    # Chr: ACS_BBSS
    # Colors: COLOR_BLACK
    cm.waitforkey()
    cm.cleanup()
    return None

def template(stdscr):
    cm = CursesManager()
    cm.set_current_window(stdscr)
    cm.clear()

    cm.waitforkey()
    cm.cleanup()
    return None

def tryit():
    # Configuration
    curses.echo()
    curses.curs_set(1)
    curses.setsyx(10, 10)
    curses.doupdate()
    # Click put, clicky, mouse diagnose
    # paint sith matrix or lists
    # Secure print no out of bounds?

if __name__ == "__main__":
    #wrapper(diagnose)
    #wrapper(step1)         # Print slow text
    #wrapper(step2)         # Print messages
    #wrapper(step3)         # Attributes usage
    #wrapper(step4)         # Basic bucle with getch
    #wrapper(step5)         # Color terminal!
    #wrapper(step6)         # Selective clear
    #wrapper(step7)         # Cursor types
    wrapper(step8)          # Move to class!!! TODO
    #wrapper(step9)      # Menu
    #wrapper(step10)
    #wrapper(step11)
    #wrapper(step12)
    #wrapper(step13)
    #wrapper(step14)
    #wrapper(step15)
    #wrapper(step16)    # Simple interface, review
    #wrapper(step17)     # xxx
    #wrapper(step18)
    print("Thanks for using curses guide")

# TODO Check create pads

# Widget python library

wpm = Widget python manager

[![Build Status](https://travis-ci.org/vgonisanz/wpm.svg?branch=master)](https://travis-ci.org/vgonisanz/wpm)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1b17a8abfe964a1ea304529d755cffa7)](https://www.codacy.com/app/vgonisanz/wpm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vgonisanz/wpm&amp;utm_campaign=Badge_Grade)

## Requeriments

1. Install dependencies
```
pip install -r requirements.txt # None right now, numpy is not needed unless 3d
```
1. Install curses manually
  * Go to this repository: http://www.lfd.uci.edu/~gohlke/pythonlibs/
  * Download wheel file with your python version, in example: 'curses‑2.2‑cp36‑cp36m‑win_amd64.whl'
  * Install it manually with: ```python -m pip install curses‑2.2‑cp36‑cp36m‑win_amd64.whl```

## Basic concepts

### Basic classes types

* Wpm is a class manage screen and associated widgets, elements and functions. Manager to initialize/respoter terminal, manage widget stack and control all UI.
* Element is a Dummy interactive class with a low level functionality. It contains a curses WindowClass. Calling its functions can be drawn in different ways.
* Widget is a interactive class with high level functionality. It have a element with width, height, x and y. Also run function to take I/O control. It ccan generate control and actions externally.

* TODO: Remove window parameter. Apply with manager all actions a current windows only (easier) or allow to use window parameter (more complicated, more versatile)?

### Design rules

* All data struct shall be classes without constructor.
* Manager will use a internal stack to manage different widgets.
* All operations are applied to last widget.
* Classes shall use heiratch
* Widget types:
  * Widget_activity
    * Widget_menu (buy_menu example)
    * more...
  * Widget_button: (button example)
  * Widget_popup
    * Widget_popup_warning: Warning message, ok button. Yellow or special movie.
    * Widget_popup_okcancel: Ask user ok or cancel button.
    * Widget_help: Print a message, ok button.

### Ideas

* themes: Change different themes to use different colors. (Use a palette, change a color type without affect others)

### Documentation /  Full Description

#### Elements

A element is an object with low level logic. It hierachy from window, adding functions to print inside.

* All element have a status
* It can be draw calling draw method.

### Button

A button is a class with 4 states:

* Normal: The button is active. It is selectable.
* Inactive: The button is not selectable.
* Focus: The button is ready to be pushed.
* Pushed: The buttons has been pushed and will release.

## Widget

A widget is an object with high level logic. All widget can contain one or more elements and a function to take control.

* It can be draw calling draw method. This refresh all child elements. Update first background and then front elements.

# Software design

## General

wpm is using curses. But it shall transparent to the users. Users shall not parse exceptions while using wpm, but all problems shall be reported in a error file.

## Output

Logs are required. Print into a file.

## Exceptions

All exceptions shall be in a try, and pass the execution, reporting problem in a error.log

# Static code analysis

Using Codacy to analyze code status

# Test

Using travis to test library

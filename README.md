# Widget python library

This manager could be a widget library --> wpm = Widget python manager

[![Build Status](https://travis-ci.org/vgonisanz/wpm.svg?branch=master)](https://travis-ci.org/vgonisanz/wpm)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1b17a8abfe964a1ea304529d755cffa7)](https://www.codacy.com/app/vgonisanz/wpm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vgonisanz/wpm&amp;utm_campaign=Badge_Grade)

## Requeriments

## Concepts

* Wpm is a class manage screen and associated widgets, elements and functions.
* Element is a interactive class with a low level functionality.
* Widget is a interactive class with high level functionality.

## Organization

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

## wpm

* print: All functions starting with print shall apply to current widget in widget stack. Exist a group of interesting print elements.

## Elements

A element is an object with low level logic.

* All element have a status
* It can be draw calling draw method.

### Button

A button is a class with 3 states:

* Normal: The button is active. It is selectable.
* Inactive: The button is not selectable.
* Focus: The button is ready to be pushed.
* Pushed: The buttons has been pushed and will release.

## Widget

All widget can contain one or more elements.

* It can be draw calling draw method. This refresh all child elements. Update first background and then front elements.

# Static code analysis

Using Codacy to analyze code status

# Test

Using travis to test library

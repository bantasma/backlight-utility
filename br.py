#!/usr/bin/python

'''
br - brightness control
7/17/23

'''

import sys

backlight_path = "/sys/class/backlight/amdgpu_bl0/brightness"

min_brightness = 0
max_brightness = 255
cli_args = sys.argv[1:]

def get_current_brightness():
    with open(backlight_path) as file:
        return file.read().strip()


def set_current_brightness(val):
    with open(backlight_path, 'w') as file:
        file.write(str(int(val)))


def convert_to_percent(val): # percentage for user 
    val = int(val)
    return int(val / 255 * 100)
    

def convert_to_brightness(val): # gets written to file
    val = int(val)
    return int(val * 255 / 100)


def change_brightness(val, op):
    original = convert_to_percent(get_current_brightness())
    if op == "+":
        new = int(original) + int(val)
        if new > 100:
            new = 100
    elif op == "-":
        new = int(original - int(val))
        if new < 0:
            new = 0
    screen_value = convert_to_brightness(new)
    set_current_brightness(screen_value)
    print(f"screen brightness: {original}% -> {new}%")


def set_brightness(val):
    original = convert_to_percent(get_current_brightness())
    screen_value = convert_to_brightness(val)
    set_current_brightness(screen_value)
    print(f"screen brightness: {original}% -> {val}%")



try: 
    user_var = cli_args[0]
except IndexError:
    print()
    print("> provide a brightness value as a percent\n")
    print("> examples:")
    print("-> br +50 -> increase brightness by 50%")
    print("-> br -25 -> decrease brightness by 25%")
    print("-> br 75  -> set brightness to 75%")
    print()
    sys.exit()

if user_var[0] == "+" or user_var[0] == "-":
    change_brightness(user_var[1:], user_var[0])

else:
    set_brightness(user_var)
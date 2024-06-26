#!/usr/bin/python3

"""Module to add command-line argument to a list and save them to JSON file.
The module handles the case where the file doesn't exist by creating a new list
and saving the arguments.It uses external functions to save to
and load from a JSON file.
"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \

    __import__('8-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
        items.extend(sys.argv[1:])
        save_to_json_file(items, "add_item.json")

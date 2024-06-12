#!/usr/bin/python3
"""
Module prints text
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each
         occurrence of ".", "?", and ":".

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent_marks = [".", "?", ":"]
    lines = []
    current = ""

    for i, char in enumerate(text):
        if char.isspace() and (i == 0 or text[i-1] in indent_marks):
            continue
        current += char
        if char in indent_marks:
            lines.append(current.strip())
            lines.append("")
            current = ""

    if current:
        lines.append(current.strip())

    for i, line in enumerate(lines):
        end = "\n" if i < len(lines) - 1 else ""
        print(line, end=end)

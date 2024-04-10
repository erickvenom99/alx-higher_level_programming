def text_indentation(text):
        """
    Prints a text with two new lines after each occurrence of ".", "?", and ":".

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
parts = text.splitlines()

for part in parts:
    part = part.strip()
    if part[-1] in indent_marks:
        print(part)
        print()
    else:
        print(part)

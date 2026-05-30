#!/usr/bin/python3
"""Module that defines a function to append to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

"""
generator.py - Generates the passwords.
"""

# Imports
from random import choice # To generate random letters
import json # To import the letter groups

# Load letter groups
with open("letter-groups.json", mode="r") as f:
    letter_groups = json.load(f)

def get_random_letter(letters):
    """
    Gets a random letter out of letters.
    """

    return choice(letters)

def get_letters(letter_group_settings):
    """
    Gets all letters from a option set of letter groups.

    """

    return "".join([letter_groups[i] for i in letter_group_settings if i in letter_groups])

def generate_password(letter_groups, length):
    """
    Generates a password of length `length` and the letter groups `letter_groups`.
    """

    letters = get_letters(letter_groups)

    password = "".join([get_random_letter(letters) for _ in range(length)])

    return password

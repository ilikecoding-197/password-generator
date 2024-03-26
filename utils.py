"""
Utils.
"""

YES = [
    "y",
    "yes",
    "yas",
    "yea",
    "yeah",
    "fax",
    "fax no printer",
    "true",
    "period",
    "1",
    "on",
    "true"
]

def get_yes_or_no(prompt):
    """
    Gets a yes or a no from the user.
    """

    user_input = input(prompt)

    return user_input in YES

def spilt_number_into_two_halves(number):
    """
    Split a number into two halves.
    """

    first_half = number // 2
    second_half = number - first_half

    return first_half, second_half
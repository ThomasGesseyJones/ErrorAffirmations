""" Affirmations

This module adds affirmations to the end of Python error messages, so that
you feel better about your errors.
"""

import sys
import random


# List of affirmations to choose from, users can edit this list to add their
# own or remove ones they don't like.
affirmations = [
    "You only learn by making mistakes.",
    "At least you know that there is a problem, an invisible error is the "
    "worst kind.",
    "Keep trying, we are sure your code will be perfect soon.",
    "Why not have a quick break? You deserve it, and it might help you "
    "solve this error.",
    "Thank you for using ErrorAffirmations, you have our full support in "
    "debugging this difficult error.",
]


# Function to select a random affirmation from the list.
def get_random_affirmation() -> str:
    """ Returns a random affirmation from the list of affirmations.

    Returns
    -------
    affirmation: str
        An encouraging message to help you feel better about your errors.
    """
    return random.choice(affirmations)


# Code to replace the default Python excepthook with one that prints an
# affirmation after the error message.
sys.base_excepthook = sys.excepthook


def affirming_excepthook(*args):
    """ Prints an affirmation after the standard error message. """
    sys.base_excepthook(*args)
    sys.stderr.write(f'\n{get_random_affirmation()}\n')


sys.excepthook = affirming_excepthook

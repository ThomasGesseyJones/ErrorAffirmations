"""Affirmations.

This module adds affirmations to the end of Python error messages, so that
you feel better about your errors.
"""

# Required libraries
import sys
import random
import os


# Parameters
DEFAULT_FILE = os.path.join(os.path.dirname(__file__),
                            "data",
                            "affirmations.txt")


# Set of affirmations to choose from, users can edit this set to add their
# own or remove ones they don't like using the functions below. This set
# should not be edited directly.
_affirmations = set()


def add_affirmation(affirmation: str) -> None:
    """Add an affirmation to the set of affirmations.

    Parameters
    ----------
    affirmation: str
        An encouraging message to help you feel better about your errors.
    """
    _affirmations.add(affirmation)


def remove_affirmation(affirmation: str) -> None:
    """Remove an affirmation from the set of affirmations.

    Parameters
    ----------
    affirmation: str
        An encouraging message to help you feel better about your errors.
    """
    _affirmations.remove(affirmation)


def clear_affirmations() -> None:
    """Clear the set of affirmations."""
    _affirmations.clear()


def load_affirmations_from_file(file: str, append: bool = True) -> None:
    """Load affirmations from a file.

    Parameters
    ----------
    file: str
        Path to file containing affirmations, one per line.
    append: bool, optional
        Whether to append affirmations to the existing set of affirmations
    """
    with open(file, "r") as f:
        if not append:
            clear_affirmations()

        for line in f:
            add_affirmation(line.strip())


def get_affirmations() -> set:
    """Return a copy of the set of affirmations.

    Returns
    -------
    affirmations: set
        A set of encouraging messages to help you feel better about your
        errors.
    """
    return _affirmations.copy()


def get_random_affirmation() -> str:
    """Return a random affirmation.

    Returns
    -------
    affirmation: str
        An encouraging message to help you feel better about your errors.
    """
    return random.choice(list(_affirmations))


# Load affirmations from default file
load_affirmations_from_file(DEFAULT_FILE)

# Core functionality to add affirmations to error messages. This is done by
# replacing the default Python excepthook with one that prints an affirmation
# after the error message.
sys.base_excepthook = sys.excepthook


def affirming_excepthook(*args) -> None:
    """Print an affirmation after the standard error message.

    Parameters
    ----------
    *args: tuple
        Arguments passed to the standard sys excepthook
    """
    sys.base_excepthook(*args)
    sys.stderr.write(f'\n{get_random_affirmation()}\n')


# Override the default excepthook with the affirming one
sys.excepthook = affirming_excepthook

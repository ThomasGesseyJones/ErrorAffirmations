"""Affirmations.

This module adds affirmations to the end of Python error messages, so that
you feel better about your errors.
"""

# Required libraries
from typing import Iterable, Union
import sys
import random
from pkg_resources import resource_stream


# Parameters
DEFAULT_FILE = resource_stream("erroraffirmations",
                               "data/affirmations.txt")
AFFIRMATIONS = Union[str, Iterable[str]]

# Set of affirmations to choose from, users can edit this set to add their
# own or remove ones they don't like using the functions below. This set
# should not be edited directly.
_affirmations = set()


def add_affirmations(affirmations: AFFIRMATIONS) -> None:
    """Add affirmation(s) to the set of affirmations.

    Parameters
    ----------
    affirmations: str or iterable of str
        An encouraging message to help you feel better about your errors.
        Or a collection of such messages.
    """
    if isinstance(affirmations, str):
        _affirmations.add(affirmations)
        return
    elif isinstance(affirmations, Iterable):
        _affirmations.update(affirmations)
        return
    else:
        raise TypeError("affirmations must be a string or iterable of strings")


def remove_affirmations(affirmations: AFFIRMATIONS) -> None:
    """Remove affirmation(s) from the set of affirmations.

    Parameters
    ----------
    affirmations: str or iterable of str
        An encouraging message to help you feel better about your errors.
        Or a collection of such messages.
    """
    if isinstance(affirmations, str):
        _affirmations.remove(affirmations)
        return
    elif isinstance(affirmations, Iterable):
        _affirmations.difference_update(affirmations)
        return
    else:
        raise TypeError("affirmations must be a string or iterable of strings")


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
            add_affirmations(line.strip())


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


def reset_affirmations() -> None:
    """Reset affirmations to the defaults from the default file."""
    load_affirmations_from_file(DEFAULT_FILE.name, append=False)


# Load default affirmations from default file
reset_affirmations()

# Option to turn off affirmations
_affirmations_enabled = True  # On by default (why else would you use this?)


def disable_affirmations() -> None:
    """Disable affirmations."""
    global _affirmations_enabled
    _affirmations_enabled = False


def enable_affirmations() -> None:
    """Enable affirmations."""
    global _affirmations_enabled
    _affirmations_enabled = True


def affirmations_enabled() -> bool:
    """Return whether affirmations are enabled.

    Returns
    -------
    affirmations_enabled: bool
        Whether affirmations are enabled.
    """
    return _affirmations_enabled


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
    # Start with normal error message
    sys.base_excepthook(*args)  # type: ignore

    # End there are no affirmations, or affirmations are disabled
    if (len(_affirmations) == 0) | (not _affirmations_enabled):
        return

    # Otherwise, print a random affirmation
    sys.stderr.write(f'\n{get_random_affirmation()}\n')


# Override the default excepthook with the affirming one
sys.excepthook = affirming_excepthook

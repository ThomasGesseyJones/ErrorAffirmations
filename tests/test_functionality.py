"""Test the core functionality of the project."""

import pytest
import erroraffirmations as ea


# Custom error class for testing.
class CustomError(Exception):
    """A custom error class."""
    pass


@pytest.mark.parametrize("exception", [Exception, ValueError, TypeError,
                                       CustomError])
def test_adding_affirmations(exception):
    """Test raises the correct error type."""
    with pytest.raises(exception):
        raise exception("Test exception")


@pytest.mark.parametrize("exception", [Exception, ValueError, TypeError,
                                       CustomError])
def test_adding_no_affirmations(exception):
    """Test having no affirmations no longer raise an unexpected error."""
    ea.clear_affirmations()
    with pytest.raises(exception):
        raise exception("Test exception")

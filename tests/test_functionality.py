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

    # Reset affirmations for other tests
    ea.reset_affirmations()


@pytest.mark.parametrize("exception", [Exception, ValueError, TypeError,
                                       CustomError])
def test_adding_no_affirmations(exception):
    """Test having no affirmations no longer raise an unexpected error."""
    ea.clear_affirmations()
    with pytest.raises(exception):
        raise exception("Test exception")

    # Reset affirmations for other tests
    ea.reset_affirmations()

# It is unclear to me how to test that affirmations are actually added to
# error messages. Because the code modifies the excepthook, it has no
# effect unless an error is not caught. However, if an error is not caught,
# the test will fail. I am not sure how to get around this.
# Any suggestions?

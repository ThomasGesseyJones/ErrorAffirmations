"""Test the affirmations interface."""

import pytest
import erroraffirmations as ea


@pytest.mark.parametrize("affirmation", ["Test affirmation", "Another test",
                                         "A multi-line\naffirmation"])
def test_add_affirmation(affirmation):
    """Test that add_affirmation() adds an affirmation.

    Parameters
    ----------
    affirmation : str
        The affirmation to add.
    """
    ea.add_affirmation(affirmation)
    assert affirmation in ea.get_affirmations()

"""Test the example scripts."""

import sys
from erroraffirmations import enable_affirmations
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.joinpath('examples')))


# Run each example script
def test_quick_start_example():
    """Test that quick_start.py runs with expected Exception."""
    try:
        import quick_start  # noqa: F401
    except Exception as e:
        assert isinstance(e, Exception)
        assert str(e) == 'Something went wrong'


def test_editing_affirmations_example():
    """Test that editing_affirmations.py runs with expected Exception."""
    try:
        import editing_affirmations  # noqa: F401
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert str(e) == "1 + 1 is not equal to 3"


def test_loading_affirmations_example():
    """Test that loading_affirmations.py runs with expected Exception."""
    try:
        import loading_affirmations  # noqa: F401
    except ZeroDivisionError as e:
        assert isinstance(e, ZeroDivisionError)


def test_disabling_affirmations_example():
    """Test that disabling_affirmations.py runs with expected Exception."""
    try:
        import disabling_affirmations  # noqa: F401
    except TypeError as e:
        assert isinstance(e, TypeError)
        assert str(e) == "Boring regular error message"

    # Renable affirmations for other tests
    enable_affirmations()


def test_empty_affirmations_examples():
    """Test that empty_affirmations.py runs with expected Exception."""
    try:
        import empty_affirmations  # noqa: F401
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert str(e) == "A normal error message"

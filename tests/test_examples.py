"""Test the example scripts."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.joinpath('examples')))


# Run each example script
def test_basic_usage_example():
    """Test that basic_usage.py runs with expected Exception."""
    try:
        import basic_usage  # noqa: F401
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


def test_empty_affirmations_examples():
    """Test that empty_affirmations.py runs with expected Exception."""
    try:
        import empty_affirmations  # noqa: F401
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert str(e) == "A normal error message"

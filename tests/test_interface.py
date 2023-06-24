"""Test the affirmations interface."""

import pytest
import erroraffirmations as ea
import os


# Set path to data file
test_affirmations_file = os.path.join(os.path.dirname(__file__), 'test_data',
                                      'test_affirmations.txt')


# Start of tests
def test_get_affirmations():
    """Test that get_affirmations() returns a set of default affirmations."""
    assert isinstance(ea.get_affirmations(), set)

    affirmations = ea.get_affirmations()
    assert len(affirmations) > 0

    for affirmation in affirmations:
        assert isinstance(affirmation, str)


def test_get_random_affirmation():
    """Test that get_random_affirmation() returns a random affirmation."""
    affirmation = ea.get_random_affirmation()
    assert isinstance(affirmation, str)
    assert affirmation in ea.get_affirmations()


@pytest.mark.parametrize("affirmations", ["Test affirmation",
                                          "Another test",
                                          "A multi-line\naffirmation",
                                          ["A list of strings",
                                           "A second string",
                                           "A third string"]])
def test_add_affirmations(affirmations):
    """Test that add_affirmation() adds affirmation(s).

    Parameters
    ----------
    affirmations : str or Iterable of str
        The affirmation(s) to add.
    """
    ea.add_affirmations(affirmations)
    if isinstance(affirmations, str):
        affirmations = [affirmations]
    for affirmation in affirmations:
        assert affirmation in ea.get_affirmations()


@pytest.mark.parametrize("invalid", [1, 1.0, True, None, object, dict])
def test_add_invalid_affirmations(invalid):
    """Test that add_affirmations() raises TypeError for invalid input.

    Parameters
    ----------
    invalid : object
        An object that is not a string or iterable of strings."""
    with pytest.raises(TypeError):
        ea.add_affirmations(invalid)  # type: ignore


@pytest.mark.parametrize("affirmations", ["Test affirmation",
                                          "Another test",
                                          "A multi-line\naffirmation",
                                          ["A list of strings",
                                           "A second string",
                                           "A third string"]])
def test_remove_affirmations(affirmations):
    """ Test that remove_affirmation() removes affirmation(s).

    Parameters
    ----------
    affirmations : str or Iterable of str
        The affirmation(s) to remove.
    """
    input_affirmations = affirmations

    ea.add_affirmations(input_affirmations)
    if isinstance(affirmations, str):
        affirmations = [affirmations]
    for affirmation in affirmations:
        assert affirmation in ea.get_affirmations()

    ea.remove_affirmations(input_affirmations)
    for affirmation in affirmations:
        assert affirmation not in ea.get_affirmations()


@pytest.mark.parametrize("invalid", [1, 1.0, True, None, object, dict])
def test_remove_invalid_affirmations(invalid):
    """Test that remove_affirmations() raises TypeError for invalid input.

    Parameters
    ----------
    invalid : object
        An object that is not a string or iterable of strings.
    """
    with pytest.raises(TypeError):
        ea.remove_affirmations(invalid)  # type: ignore


def test_clear_affirmations():
    """Test that clear_affirmations() clears the set of affirmations."""
    ea.clear_affirmations()
    assert len(ea.get_affirmations()) == 0

    # Reset affirmations for other tests
    ea.reset_affirmations()


def test_load_affirmations_from_file():
    """Test that load_affirmations_from_file() loads from file."""
    # Test default behaviour to append
    current_num_affirmations = len(ea.get_affirmations())
    ea.load_affirmations_from_file(test_affirmations_file)
    assert len(ea.get_affirmations()) == current_num_affirmations + 3
    assert "A test affirmation" in ea.get_affirmations()

    # Test resetting affirmations
    ea.reset_affirmations()
    assert len(ea.get_affirmations()) == current_num_affirmations

    # Test loading a file with append=False
    ea.load_affirmations_from_file(test_affirmations_file, append=False)
    assert len(ea.get_affirmations()) == 3


# Test enabling and disabling affirmations
def test_enable_affirmations():
    """Test that enable_affirmations() enables affirmations."""
    # Check on by default
    assert ea.affirmations_enabled()

    ea.disable_affirmations()
    assert not ea.affirmations_enabled()
    ea.enable_affirmations()
    assert ea.affirmations_enabled()

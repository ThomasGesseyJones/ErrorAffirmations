"""Example of how to use ErrorAffirmations to load affirmations from a file."""

from erroraffirmations import load_affirmations_from_file
import os

# Add affirmations from a file
load_affirmations_from_file(
    os.path.join(os.path.dirname(__file__), "my_affirmations.txt"),
    append=False)

_ = 1/0

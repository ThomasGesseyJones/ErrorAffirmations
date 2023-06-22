"""Example of ErrorAffirmations behaviour when there are no affirmations."""

from erroraffirmations import clear_affirmations

# Remove all existing affirmations
clear_affirmations()

# No affirmation is displayed
raise ValueError("A normal error message")

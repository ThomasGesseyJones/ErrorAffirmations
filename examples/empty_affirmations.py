""" This is an example of ErrorAffirmations behaviour when the user has
cleared the affirmations """
from erroraffirmations import clear_affirmations

# Remove all existing affirmations
clear_affirmations()

# No affirmation is displayed
raise ValueError("A normal error message")

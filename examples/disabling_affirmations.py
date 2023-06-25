"""Example of how to use disable ErrorAffirmations."""

from erroraffirmations import disable_affirmations, affirmations_enabled

# Defaults to on
print(affirmations_enabled())

# Turn off affirmations
disable_affirmations()

# Now affirmations are off
print(affirmations_enabled())

# And finally show that affirmations are not displayed
raise TypeError("Boring regular error message")

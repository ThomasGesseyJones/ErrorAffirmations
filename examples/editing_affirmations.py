"""Example of how to use ErrorAffirmations to add your own affirmations."""

from erroraffirmations import add_affirmations, remove_affirmations, \
    get_affirmations, clear_affirmations

# Let us start by clearing the affirmations
clear_affirmations()

# Add some affirmations
add_affirmations(["You are doing great!", "An affirmation we don't like"])

# Show the current set of affirmations
print(get_affirmations())
print("\n")

# Remove an affirmation
remove_affirmations("An affirmation we don't like")

# Show the current set of affirmations
print(get_affirmations())

# And finally show the affirmations in action
raise ValueError("1 + 1 is not equal to 3")

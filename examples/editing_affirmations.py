""" This is an example of how to use ErrorAffirmations to add your own
affirmations to the list """
from erroraffirmations import add_affirmation, get_affirmations, \
    clear_affirmations

# Show part of the current list of affirmations
for affirmation in list(get_affirmations())[:5]:
    print(affirmation)
print("\n")

# Remove all existing affirmations
clear_affirmations()

# Add your own affirmations
add_affirmation("You are doing great!")

# Show new list of affirmations
print(get_affirmations())
print("\n")

# Let us see it in action
raise ValueError("1 + 1 is not equal to 3")

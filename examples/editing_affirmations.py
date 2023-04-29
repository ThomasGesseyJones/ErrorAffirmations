""" This is an example of how to use ErrorAffirmations to add your own affirmations to the list """
from erroraffirmations.affirmations import affirmations

# Show current list of affirmations
for affirmation in affirmations:
    print(affirmation)
print("\n")

# Remove all existing affirmations
affirmations.clear()

# Add your own affirmations
affirmations.append("You are doing great!")

# Show new list of affirmations
print(affirmations)
print("\n")

# Let us see it in action
raise ValueError("1 + 1 is not equal to 3")

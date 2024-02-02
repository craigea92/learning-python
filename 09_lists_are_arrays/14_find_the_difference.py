"""
FIND THE DIFFERENCE

We keep track of each character's level in a list. 
When someone's level changes we want to know about it so we can congratulate them! 
"""

# Assignment
# Find any differences between the old_character_levels and new_character_levels lists and print the index where the values are different.
# Fill in the loop with code that prints the indexes where the items in the lists differ.

# Solution
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 43]

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] != new_character_levels[i]:
            print(i)

# Tests
def test():
    print("Differences found on indexes:")
    check_character_levels()
    print("=====================================")

def main():
    test()

main()

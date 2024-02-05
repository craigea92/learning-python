"""
LIST OPERATIONS - CONTAINS

Checking whether a value exists in a list is also really easy in Python, just use the in keyword.

fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True
"""

# Assignment
# Complete the is_top_weapon function. It should return True if the weapon is in the top_weapons list, otherwise it should return False.

# Solution
def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    return weapon in top_weapons    

# Tests
run_cases = [
    ("sword of justice", True),
    ("bronze mace", False),
    ("sword of slashing", True),
]

submit_cases = run_cases + [
    ("", False),
    ("great axe", True),
    ("silver bow", True),
    ("golden spear", False),
    ("spiked knuckles", True),
    ("spellbook", True),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:")
    print(f" * Weapon: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_top_weapon(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

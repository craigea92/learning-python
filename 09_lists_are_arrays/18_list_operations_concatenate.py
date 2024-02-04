"""
LIST OPERATIONS - CONCATENATE

Concatenating two lists (smushing them together) is easy in Python, just use the + operator.

total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]


"""

# Assignment
# Create a new list that combines favorite_weapons, favorite_armor, and favorite_items in this order.

# Solution
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    list = favorite_weapons + favorite_armor + favorite_items

    return list

# Tests
run_cases = [
    (
        ["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"],
        (["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
    ),
]

submit_cases = run_cases + [
    (
        ["lance"],
        ["shield"],
        ["potions"],
        (["lance", "shield", "potions"]),
    ),
    (
        ["bow", "staff"],
        ["breastplate"],
        ["scrolls", "bedroll"],
        (["bow", "staff", "breastplate", "scrolls", "bedroll"]),
    ),
    ([], [], [], ([])),
]

def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = concatenate_favorites(input1, input2, input3)
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


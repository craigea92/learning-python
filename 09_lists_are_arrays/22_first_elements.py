"""
FIRST ELEMENT

In Python, not is a logical operator used to negate a boolean value. 
It returns True if the operand is False, and False if the operand is True.
"""

# Assignment
# Write a function that returns the first element from a list. 
# If the list is empty then return the string ERROR instead.

# Solution
def get_first_item(items):
    if not items:
        return "ERROR"
    else:
        return items[0]

# Tests
run_cases = [([1, 2], 1), (["Healing Potion"], "Healing Potion")]

submit_cases = run_cases + [
    (["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
    ([], "ERROR"),
    (["Apple", "Banana", "Cherry"], "Apple"),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
    ([False, True, False], False),
    ([None, "None", 0], None),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_first_item(input1)
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
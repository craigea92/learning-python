"""
COMPARISON OPERATOR EVALUATIONS

When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.

Take the following two examples:

is_bigger = 5 > 4

is_bigger = True

In both of the above cases, we're creating a Boolean variable called is_bigger with a value of True.

Because 5 is greater than 4, is_bigger is assigned the value of True.
"""

# Assignment
# Create the following variables. 
# Use comparison operators to determine their boolean values. 
# Return them in this order:

# is_bob_as_tall_as_elon
# is_sara_as_tall_as_elon
# is_jill_as_tall_as_sara

# Solution
def compare_heights(elon_height, sara_height, jill_height, bob_height):
    is_bob_as_tall_as_elon = bob_height == elon_height
    is_sara_as_tall_as_elon = sara_height == elon_height
    is_jill_as_tall_as_sara = jill_height == sara_height
    return is_bob_as_tall_as_elon, is_sara_as_tall_as_elon, is_jill_as_tall_as_sara

# Tests
run_cases = [
    (5, 5, 7, 5, (True, True, False)),
    (6, 6, 5, 5, (False, True, False)),
]

submit_cases = run_cases + [
    (4, 4, 4, 4, (True, True, True)),
    (2, 2, 2, 2, (True, True, True)),
    (8, 8, 8, 7, (False, True, True)),
    (5, 7, 9, 11, (False, False, False)),
    (11, 9, 7, 5, (False, False, False)),
]

def test(elon, sara, jill, bob, expected):
    print("---------------------------------")
    print(f"Inputs: {elon}, {sara}, {jill}, {bob}")
    print(f"Expecting: {expected}")
    result = compare_heights(elon, sara, jill, bob)
    print(f"Actual: {result}")
    if result == expected:
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
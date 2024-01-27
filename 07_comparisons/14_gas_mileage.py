"""
GAS MILEAGE

There isn't a gas station between Tyler's house and his work. 
He is trying to figure out if his car has enough gas to get him to work and back home.
"""

# Assignment
# Complete the has_enough_gas function.
# Do some Pythonic math with the miles_one_way and miles_per_gallon variables to determine how many gallons are needed. 
# Tyler should get to work AND make it back home after he gets off work. Assign the result to a gallons_needed variable.
# Return True if there are at least enough gallons in the tank based on the gallons_needed variable, and False otherwise.

# Solution
def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = (miles_one_way * 2) / miles_per_gallon

    if gallons_in_car >= gallons_needed:
        return True
    return False

# Tests
run_cases = [
    (8, 50, 22, True),
    (9, 100, 20, False),
]

submit_cases = run_cases + [
    (10, 50, 18, True),
    (3, 105, 22, False),
    (1, 1, 2, True),
    (2, 1, 1, True),
    (1, 2, 1, False),
]

def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = has_enough_gas(input1, input2, input3)
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
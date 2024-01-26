"""
IF PRACTICE

Remember, you can use the == operator to check if two values are equal. 
For example:

is_equal = 5 == 5
# is_equal is True
"""

# Assignment
# Complete the check_swords_for_army function. 
# If the number of swords and the number of soldiers match, return the string: "correct amount"
# Otherwise, return the string: "incorrect amount"

# Solution
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    return "incorrect amount"

# Tests
run_cases = [
    (500, 1000, "incorrect amount"),
    (800, 800, "correct amount"),
]

submit_cases = run_cases + [
    (1500, 1000, "incorrect amount"),
    (200, 200, "correct amount"),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_swords_for_army(input1, input2)
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

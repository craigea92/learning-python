"""
UNIT TESTS

Up until this point, all the coding lessons you've completed have been testing you based on your code's console output. 
For example, a lesson might expect your code to print something like:

Armor: 2
Health: 18

Going forward, you'll encounter unit tests. A unit test is just an automated program that tests a small "unit" of code. Usually just a function or two.

These new unit-test-style lessons will test your code's functionality rather than its output. 
If your code returns the correct values, you pass. If it doesn't, you fail.

Two things to note here:

In the real world, you'll be writing unit tests and running them against your code to make sure it works as expected.
You can run and debug your code with print statements, and leave those print statements in when you submit. 
"""
# Assignment
# Complete the total_xp function to pass the test cases

# Solution
def total_xp(level, xp_to_add):
    current_level = level * 100
    total_xp = xp_to_add + current_level
    return total_xp

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = total_xp(input1, input2)
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
"""
CHANGING IN PLACE

It's fairly common to want to change the value of a variable based on its current value.

player_score = 4
player_score = player_score + 1
# player_score now equals 5

player_score = 4
player_score = player_score - 1
# player_score now equals 3

Don't let the fact that the expression player_score = player_score - 1 is not a valid mathematical expression be confusing. 
It doesn't matter, it is valid code. It's valid because the way the expression should be read in English is:

Assign to player_score the old value of player_score minus 1
"""

# Assignment
# Complete the update_player_score function. It should add increment to current_score and then return the new current_score.

# Solution
def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score

# Tests
run_cases = [
    (0, 100, 100),
    (100, 200, 300),
]

submit_cases = run_cases + [
    (300, 300, 600),
    (600, 50, 650),
    (0, 0, 0),
    (1, 1, 2),
    (100, -50, 50),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = update_player_score(input1, input2)
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
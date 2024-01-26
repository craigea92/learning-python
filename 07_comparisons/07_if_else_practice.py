"""
IF-ELSE PRACTICE

Here are some basic rules with if/else blocks.

You can't have an elif or an else without an if
You can have an else without an elif

Remember, to check if two values are the same use the == operator.

same = 5 == 6
# same is false

same = 6 == 6
# same is true
"""

# Assignment
# There is a bug in the check_high_score function! Add the proper conditional statement to fix the bug.

# Solution
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

# Tests
run_cases = [
    ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
    ("brock", "ash ketchum", "You are not the highest scoring player!"),
]

submit_cases = run_cases + [
    ("misty", "brock", "You are not the highest scoring player!"),
    ("", "", "You are the highest scoring player!"),
    ("same", "same", "You are the highest scoring player!"),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_high_score(input1, input2)
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
"""
IF-ELSE
An if statement can be followed by zero or more elif (which stands for "else if") statements, which can be followed by zero or one else statement. 
For example:

if score > high_score:
    print('High score beat!')
elif score > second_highest_score:
    print('You got second place!')
elif score > third_highest_score:
    print('You got third place!')
else:
    print('Better luck next time')

First the if statement is evaluated. If it is True then the if statement's body is executed and all the other elses are ignored.

If the first if is false then the next elif is evaluated. Likewise, if it is True then its body is executed and the rest are ignored.

If none of the if statements evaluate to True then the final else statement will be the only body executed.
"""

# Assignment
# Complete the player_status function. If the player's health less than or equal to 0, return the string: "dead"
# Otherwise, if it's less than or equal to 5 return the string: "injured"
# Otherwise, return the string: "healthy"

# Solution
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"

# Tests
run_cases = [
    (0, "dead"),
    (4, "injured"),
]

submit_cases = run_cases + [
    (6, "healthy"),
    (5, "injured"),
    (1, "injured"),
    (10, "healthy"),
    (-1, "dead"),
]

def test(health, expected_status):
    print("---------------------------------")
    print(f"Health: {health}")
    print(f"Expecting: {expected_status}")
    result = player_status(health)
    print(f"Result: {result}")
    if result == expected_status:
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
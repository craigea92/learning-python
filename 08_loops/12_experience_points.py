"""
EXPERIENCE POINTS

You've been hired by a game studio to work on their latest role-playing game, in this game adventurers need experience points (XP) to level up and become stronger. 
You've been tasked with creating a function to calculate the total amount of XP needed for a player to reach a specific level.

Each character starts with 0 XP at level 1. 
To reach the next level, they need 5 XP more than the last level required. So reaching level 2 requires just 5 XP more, while reaching level 3 requires 10 XP more.
"""

# Assignment
# Complete the calculate_experience_points function.
# The calculate_experience_points function takes a single parameter named level. 
# Determine how many XP are required to get to the specified level from level 1 with 0 XP.

# Solution
def calculate_experience_points(level):
    xp_needed = 0
    for lvl in range(1, level + 1):
        xp_needed += (lvl - 1) * 5
    return xp_needed

# Tests
run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = calculate_experience_points(input1)
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
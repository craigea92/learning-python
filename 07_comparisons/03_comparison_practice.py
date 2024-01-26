"""
COMPARISON PRACTICE

car_size = 4
truck_size = 5
is_smaller = car_size < truck_size
# is_smaller is True 
"""

# Assignment
# Complete the can_withstand_blow function. 
# It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.

# Solution
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

# Tests
run_cases = [
    (175, 250, False),
    (250, 175, True),
]

submit_cases = run_cases + [
    (250, 250, True),
    (0, 0, True),
    (1, 1, True),
    (2, 3, False),
    (3, 2, True),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = can_withstand_blow(input1, input2)
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

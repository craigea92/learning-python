"""
COMBAT ADVANTAGE

A new text-based RPG you are building doesn't have any way for players to know if they are strong enough to fight certain enemies.

If a player's power level is greater than the enemies' defense that player has an advantage
If the player's power and enemies' defense are equal they are evenly matched
Otherwise, that player has a disadvantage.
"""

# Assignment
# Write an if/elif/else block. 
# It should either set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.

# Solution
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power < enemy_defense:
        disadvantage = True
    else:
        evenly_matched = True

    return advantage, disadvantage, evenly_matched

# Tests
run_cases = [
    (101, 100, True, False, False),
    (50, 100, False, True, False),
    (100, 100, False, False, True),
]

submit_cases = run_cases + [
    (150, 70, True, False, False),
    (80, 150, False, True, False),
    (0, 0, False, False, True),
    (1, 1, False, False, True),
    (1000, 500, True, False, False),
    (500, 1000, False, True, False),
]

def test(input1, input2, expected_output1, expected_output2, expected_output3):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output1}, {expected_output2}, {expected_output3}")
    result = combat_evaluation(input1, input2)
    print(f"Actual: {result}")
    if result == (expected_output1, expected_output2, expected_output3):
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
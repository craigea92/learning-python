"""
COUNTING PRACTICE

CHECKING FOR EXISTENCE

If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False
"""

# Assignment
# Complete the count_enemies function. It takes a list of enemy names as input. 
# It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.

# Solution
def count_enemies(enemy_names):
    enemy_counts = {}  # Initialize an empty dictionary to store counts

    for enemy in enemy_names:
        if enemy in enemy_counts:
            enemy_counts[enemy] += 1  # Increment count if enemy already exists in dictionary
        else:
            enemy_counts[enemy] = 1  # Set count to 1 if enemy is encountered for the first time
    
    return enemy_counts

# Tests
run_cases = [
    (["jackal", "kobold", "soldier"], {"jackal": 1, "kobold": 1, "soldier": 1}),
    (["jackal", "kobold", "jackal"], {"jackal": 2, "kobold": 1}),
]

submit_cases = run_cases + [
    ([], {}),
    (["jackal"], {"jackal": 1}),
    (
        [
            "jackal",
            "kobold",
            "jackal",
            "kobold",
            "soldier",
            "kobold",
            "soldier",
            "soldier",
            "jackal",
            "jackal",
            "gremlin",
            "jackal",
            "jackal",
        ],
        {"jackal": 6, "kobold": 3, "soldier": 3, "gremlin": 1},
    ),
    (["jackal", "kobold", "gremlin"], {"jackal": 1, "kobold": 1, "gremlin": 1}),
    (["jackal", "jackal", "jackal"], {"jackal": 3}),
    (["gremlin", "gremlin", "gremlin"], {"gremlin": 3}),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_enemies(input1)
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
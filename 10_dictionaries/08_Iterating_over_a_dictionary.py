"""
ITERATING OVER A DICTIONARY IN PYTHON

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny
"""

# Assignment
# Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count. 
# If there are no enemies, return None.

# Solution
def get_most_common_enemy(enemies_dict):
    if not enemies_dict:  # Check if the dictionary is empty
        return None
    
    max_count = float("-inf")
    most_common_enemy = None
    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            most_common_enemy = enemy
    
    return most_common_enemy

# Tests
run_cases = [
    ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
    ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
]

submit_cases = run_cases + [
    ({"jackal": 2, "gremlin": 7}, "gremlin"),
    ({"jackal": 3}, "jackal"),
    ({}, None),
    ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
    ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_most_common_enemy(input1)
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
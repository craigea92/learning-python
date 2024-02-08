"""
TOTAL SCORE

A website that tracks basketball scores and stats is having trouble with its data. 
The first-half score and second-half score are stored in separate dictionaries, making it difficult for them to parse the overall score. 
They have asked you to help them write a program that merges the two dictionaries and another function that calculates the total score.
"""

# Assignment
# Complete the merge and total_score functions.
# The merge function accepts two score dictionaries as input and returns a single merged dictionary that contains all of the keys and values from the input dictionaries.
# The total_score function should take a single score dictionary as input and return the total score calculated from the values of that dictionary. 
# Take a look at the test suite near the top of the file for the names of keys to expect. If no points were scored, the function should return 0.

# Solution
def merge(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1 to avoid modifying it
    merged_dict.update(dict2)  # Update with the contents of dict2
    return merged_dict

def total_score(score_dict):
    total = 0
    for key, value in score_dict.items():
        if key.endswith('_quarter'):
            total += value
    return total

# Tests
run_cases = [
    (
        {"first_quarter": 24, "second_quarter": 31},
        {"third_quarter": 29, "fourth_quarter": 40},
        124,
    ),
    (
        {"first_quarter": 12, "second_quarter": 2},
        {"third_quarter": 32, "fourth_quarter": 87},
        133,
    ),
]

submit_cases = run_cases + [
    (
        {"first_quarter": 25, "second_quarter": 2},
        {"third_quarter": 31, "fourth_quarter": 0},
        58,
    ),
    (
        {"first_quarter": 10, "second_quarter": 20},
        {"third_quarter": 30, "fourth_quarter": 40},
        100,
    ),
    (
        {"first_quarter": 15, "second_quarter": 25},
        {"third_quarter": 0, "fourth_quarter": 0},
        40,
    ),
    ({}, {}, 0),
    (
        {"first_quarter": 0, "second_quarter": 0},
        {"third_quarter": 0, "fourth_quarter": 0},
        0,
    ),
    (
        {"first_quarter": 100, "second_quarter": 100},
        {"third_quarter": 100, "fourth_quarter": 100},
        400,
    ),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_half: {input1}")
    print(f" * second_half: {input2}")
    print(f"Expecting: {expected_output}")
    merged = merge(input1, input2)
    result = total_score(merged)
    print(f"Actual: {result}")
    if result == expected_output:
        if len(merged) == 4 or expected_output == 0:
            print("Pass")
            return True
        print("Dictionaries merged incorrectly")
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
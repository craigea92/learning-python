"""
APPENDING IN PYTHON

It's common to create an empty list then fill it with values using a loop. 
We can add values to the end of a list using the .append() method:

cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
"""

# Assignment
# Let's finish the generate_user_list function. Use the body of the loop to add the unique ID's to the player_ids list.

# Solution
def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# Tests
run_cases = [
    (5, list(range(5))),
    (10, list(range(10))),
]

submit_cases = run_cases + [
    (0, []),
    (1, [0]),
    (100, list(range(100))),
    (25, list(range(25))),
    (50, list(range(50))),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = generate_user_list(input1)
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
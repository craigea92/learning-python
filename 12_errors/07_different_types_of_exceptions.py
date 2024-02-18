"""
DIFFERENT TYPES OF EXCEPTIONS

We haven't covered classes and objects yet, which is what an Exception really is at its core. 
We'll go more into that in the object-oriented programming course that we have lined up for you next.

For now, what is important to understand is that there are different types of exceptions and that we can differentiate between them in our code.

SYNTAX
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

Which will print:

0 division
index error

As you can see in the example above, we can print the exception message by aliasing the exception using the as keyword.
"""

# Assignment
# Complete the handle_get_player_record() function. 
# It should return the result of get_player_record but if an IndexError is raised it will instead return the string: index is too high. 
# Otherwise, if any other exception is raised it will just return the exception itself.

# Solution
def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

# Tests
run_cases = [
    (0, {"name": "Slayer", "level": 128}),
    (1, {"name": "Dorgoth", "level": 300}),
    (3, "index is too high"),
    (-1, "negative ids not allowed"),
]

submit_cases = run_cases + [
    (2, {"name": "Saruman", "level": 4000}),
    (10, "index is too high"),
    (-5, "negative ids not allowed"),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    result = handle_get_player_record(input)
    print(f"Actual: {result}")
    if isinstance(result, Exception):
        result = f"{result}"
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

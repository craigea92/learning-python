"""
RAISING YOUR OWN EXCEPTIONS

Errors are not something to be scared of. 
Every program that runs in production is expected to manage errors on a constant basis. 
Our job as developers is to handle the errors gracefully and in a way that aligns with our user's expectations.

ERRORS ARE NOT BUGS

When something in our own code happens that we don't expect, we should raise our own exceptions. 
For example, if someone passes some bad inputs to a function we write, we should not be afraid to raise an exception to let them know they did something wrong.

An error or exception is raised when something bad happens, but as long as our code handles it as users expect it to, it's not a bug. 
A bug is when code behaves in ways our users don't expect it to.

For example, if a player tries to forge an iron sword out of bronze metal, we might raise an exception and display an error message to the player. 
However, that's the expected behavior of the game, so it's not a bug. 
If a player can forge the iron sword out of bronze, that may be considered a bug because that's against the rules of the game.

SYNTAX FOR RAISING EXCEPTIONS

raise Exception("something bad happened")
"""

# Assignment
# Raise an error if a player_id that doesn't exist is passed into the get_player_record function. 
# The exception should say player id not found.

# Solution
class PlayerNotFoundError(Exception):
    pass

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise PlayerNotFoundError("player id not found")

# Tests
run_cases = [
    (1, {"name": "Slayer", "level": 128}),
    (4, "player id not found"),
    (3, {"name": "Saruman", "level": 4000}),
]

submit_cases = run_cases + [
    (2, {"name": "Dorgoth", "level": 300}),
    (5, "player id not found"),
    (0, "player id not found"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * player_id: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result = get_player_record(input1)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
    except Exception as e:
        print(f"Actual: {str(e)}")
        if str(e) == expected_output:
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
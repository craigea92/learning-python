"""
SCIENTIFIC NOTATION

A float is a positive or negative number with a fractional part.

You can add the letter e or E followed by a positive or negative integer to specify that you're using scientific notation.

print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

It's a way of expressing numbers that are too large or too small to conveniently write normally.

In a nutshell, the number following the e specifies how many places to move the decimal to the right for a positive number, or to the left for a negative number.

UNDERSCORES FOR READABILITY

Python also allows you to represent large numbers in the decimal format using underscores as the delimiter instead of commas to make it easier to read.

num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
"""

# Assignment
# Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static values:
# The max players on a "small" server: 1,024,000,000,000,000,000
# The max players on a "medium" server: 10,240,000,000,000,000,000
# The max players on a "large" server: 102,400,000,000,000,000,000

# Solution
def max_players_on_server():
    max_players_small_server = 1.024e18
    max_players_medium_server = 1.024e19
    max_players_large_server = 1.024e20
    return max_players_small_server, max_players_medium_server, max_players_large_server

# Tests
run_cases = [
    (1.024e18, 1.024e19, 1.024e20),
]

submit_cases = run_cases


def test(expected1, expected2, expected3):
    print("---------------------------------")
    print(f"Expecting: {(expected1, expected2, expected3)}")
    result = max_players_on_server()
    print(f"Actual: {result}")
    if result == (expected1, expected2, expected3):
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in run_cases:
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
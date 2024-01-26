"""
BITWISE "|" OPERATOR

As you may have guessed, the bitwise OR operator is similar to the bitwise AND operator in that it works on binary rather than boolean values. 
However, the bitwise OR operator ORs the bits together. Here's an example:

0101 = 5
|
0111 = 7
=
0111 = 7

A 1 in binary is the same as True, while 0 is False. 
So a bitwise operation is just a bunch of logical operations that are completed in tandem. 
When two binary numbers are ORed together, the result has a 1 in any place where either of the input numbers has a 1 in that place.

| is the bitwise OR operator in Python. 5 | 7 = 7 and 5 | 2 = 7 as well!

0101 = 5
|
0010 = 2
=
0111 = 7
"""

# Assignment
# Complete the calculate_party_perms function. 
# It should return a binary number that represents the permissions of all the members of the party (Glorfindel, Galadriel, Elendil and Elrond).
# Use bitwise OR operations to calculate the superset of all the permissions.

# Solution
def calculate_party_perms(glorfindel, galadriel, elendil, elrond):
    party = glorfindel | galadriel | elendil | elrond
    return party

# Tests
run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = run_cases + [
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_output}")
    result = calculate_party_perms(input1, input2, input3, input4)
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
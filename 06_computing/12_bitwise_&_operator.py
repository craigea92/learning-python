"""
BITWISE "&" OPERATOR

Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value. 
For example, say you had the numbers 5 and 7 represented in binary. 
You could perform a bitwise AND operation and the result would be 5.

0101 = 5
&
0111 = 7
=
0101 = 5

A 1 in binary is the same as True, while 0 is False. 
So really a bitwise operation is just a bunch of logical operations that are completed in tandem.

Ampersand & is the bitwise AND operator in Python. 
AND is the name of the bitwise operation, while ampersand & is the symbol for that operation. 
For example, 5 & 7 = 5, while 5 & 2 = 0.

0101 = 5
&
0010 = 2
=
0000 = 0

BINARY NOTATION

When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number.

0b0101 is 5
0b0111 is 7
"""

# Assignment
# Complete each of the can_x_bits functions. 
# They should each return the result of a bitwise AND operation on the user's permission bits and the bits for the permission in question.
# Use the appropriate one of the four provided permission values at the top of the code:

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

# Solution
def can_create_bits(user_permissions):
    return user_permissions & can_create_guild

def can_review_bits(user_permissions):
    return user_permissions & can_review_guild

def can_delete_bits(user_permissions):
    return user_permissions & can_delete_guild

def can_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

# Tests
run_cases = [
    (0b0110, False, True, True, False),
    (0b1111, True, True, True, True),
    (0b0000, False, False, False, False),
]

submit_cases = run_cases + [
    (0b1001, True, False, False, True),
    (0b1000, True, False, False, False),
    (0b0100, False, True, False, False),
    (0b0010, False, False, True, False),
    (0b0001, False, False, False, True),
]

def test(
    input1, expected_output1, expected_output2, expected_output3, expected_output4
):
    print("---------------------------------")
    print(f"Inputs: {input1:04b}")
    print(f"Expecting can_create: {expected_output1}")
    print(f"Expecting can_review: {expected_output2}")
    print(f"Expecting can_delete: {expected_output3}")
    print(f"Expecting can_edit: {expected_output4}")

    result1 = can_create_bits(input1) == can_create_guild
    result2 = can_review_bits(input1) == can_review_guild
    result3 = can_delete_bits(input1) == can_delete_guild
    result4 = can_edit_bits(input1) == can_edit_guild
    print(f"Actual can_create: {result1}")
    print(f"Actual can_review: {result2}")
    print(f"Actual can_delete: {result3}")
    print(f"Actual can_edit: {result4}")
    if (
        result1 == expected_output1
        and result2 == expected_output2
        and result3 == expected_output3
        and result4 == expected_output4
    ):
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
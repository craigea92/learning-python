"""
BOOLEAN LOGIC

Boolean logic refers to logic dealing with boolean (True or False) values. For example,

Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must be true)

Cars are cool if they go faster than 200 MPH, or if they are electric. (At least one condition must be true)

LOGICAL OPERATORS REVIEW

As we discussed earlier, the logical operators and and or can be used to perform boolean logic.

"AND" REVIEW

The and operator returns True if both of the conditions on either side evaluates to True:

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

Let's go over how this function evaluates given the parameters num_legs=4 and weight=99:

return 4 == 4 and 99 < 100
return True and True
return True

Let's see what would happen with 3 and 98 instead:

return 3 == 4 and 98 < 100
return False and True
return False

"OR" REVIEW

The or operator returns True if at least one of the conditions on either side evaluates to True:

def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric

return 250 > 200 or False
return True or False
return True
"""

# Assignment
# Complete the does_attack_hit function. The function should return True if either of the following conditions are met:
# The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class
# The attack roll is a 20
# Otherwise, it should return False.

# Solution
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20

# Tests
run_cases = [
    (17, 18, False),
    (20, 25, True),
]

submit_cases = run_cases + [
    (1, 0, False),
    (16, 13, True),
    (5, 5, True),
    (1, 1, False),
    (20, 20, True),
    (15, 10, True),
    (2, 3, False),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = does_attack_hit(input1, input2)
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
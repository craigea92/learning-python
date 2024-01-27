"""
PARKING METER

A parking enforcement officer was assigned to check on some faulty parking meters on Main Street. 
He determined that the meters were giving tickets to cars whose parking duration had not yet expired.
"""

# Assignment 
# Create a check_parking_meter function. It takes two inputs:
# time_parked - the amount of time the car has been parked in minutes
# time_purchased - the amount of time the driver purchased on the meter in minutes
# If time_parked meets or exceeds time_purchased return the string "overtime charged"
# Otherwise, return the string "no charges yet"

# Solution 
def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    return "no charges yet"

# Tests
run_cases = [
    (3, 4, "no charges yet"),
    (5, 2, "overtime charged"),
]

submit_cases = run_cases + [
    (2, 2, "overtime charged"),
    (0, 1, "no charges yet"),
    (1, 1, "overtime charged"),
    (100, 2, "overtime charged"),
    (2500, 3, "overtime charged"),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_parking_meter(input1, input2)
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
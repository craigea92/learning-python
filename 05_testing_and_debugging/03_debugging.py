"""
DEBUGGING

As a professional developer, you'll typically write code on your computer and test it by yourself before it's deployed to users.

That first part of the process is called debugging. 
You write some code, run it, and if it doesn't work, you fix the bugs. 
You repeat this process until you're confident that your code works as expected.
"""

# Assignment
# Complete the take_magic_damage function.

def take_magic_damage(health, resist, amp, spell_power):
    total_maximum_damage = spell_power * amp
    total_damage = total_maximum_damage - resist
    health -= total_damage
    return health

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1),
    (100, 2, 3, 1, 99),
    (2500, 3, 2, 2, 2499),
]

def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_output}")
    result = take_magic_damage(input1, input2, input3, input4)
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
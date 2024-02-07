"""
TEST SCORES 2

The teacher you helped earlier was so satisfied with how easy your program made it for her to grade her student's tests that she wants to take this further! 
She wants a more flexible program that can grade all of her student's tests.
"""

# Assignment
# Complete the get_test_score function. It should calculate a report that describes the percentage of multiple-choice answers a student got right on their test.

# Solution
def get_test_score(answer_sheet, student_answers):
    correct = 0
    total = 0
    name = student_answers[0]

    for ans_sheet, stud_ans in zip(answer_sheet, student_answers[1:]):
        if ans_sheet == stud_ans:
            correct += 1
        total += 1
    
    score = (correct / total) * 100

    return name, score

# Tests
run_cases = [
    (
        [
            "A",
            "A",
            "C",
            "D",
            "D",
            "B",
            "C",
            "A",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "D",
            "C",
            "B",
            "A",
            "D",
            "A",
        ],
        [
            "Allan",
            "A",
            "C",
            "C",
            "B",
            "D",
            "B",
            "C",
            "A",
            "C",
            "B",
            "A",
            "A",
            "C",
            "B",
            "D",
            "C",
            "B",
            "A",
            "D",
            "A",
        ],
        ("Allan", 85.0),
    ),
    (
        [
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "C",
            "D",
            "A",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
        ],
        [
            "John",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "C",
            "D",
            "A",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
        ],
        ("John", 100.0),
    ),
]

submit_cases = run_cases + [
    (
        [
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        [
            "Tim",
            "D",
            "D",
            "C",
            "C",
            "B",
            "B",
            "A",
            "A",
            "D",
            "D",
            "C",
            "C",
            "B",
            "B",
            "A",
            "A",
            "D",
            "D",
            "C",
            "C",
        ],
        ("Tim", 0.0),
    ),
    (
        [
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        [
            "Sally",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        ("Sally", 100.0),
    ),
    (
        [
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        [
            "Jeremy",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
        ],
        ("Jeremy", 0.0),
    ),
    (
        [
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        [
            "Jeremy",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        ("Jeremy", 100.0),
    ),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nanswer_sheet: {input1}\nstudent_answers: {input2}")
    print(f"Expecting: {expected_output}")
    result = get_test_score(input1, input2)
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

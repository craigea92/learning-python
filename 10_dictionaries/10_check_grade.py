"""
CHECK GRADE

A local college is having trouble with its student administration program. 
They have asked you to help them print a student's grade from their English_1010 class.

Here's the structure of a student dictionary:

{
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}
"""

# Assignment
# Complete the get_english_grade function. It accepts a student nested dictionary and returns the student's grade in English 1010.

# Solution
def get_english_grade(student):
    if "type" in student and "student" in student["type"]:
        if "courses" in student["type"]["student"]:
            if "English_1010" in student["type"]["student"]["courses"]:
                return student["type"]["student"]["courses"]["English_1010"]["current_grade"]
    return None

# Tests
run_cases = [
    (
        {
            "type": {
                "student": {
                    "name": "Allan",
                    "courses": {
                        "math_1050": {
                            "current_grade": "C",
                        },
                        "English_1010": {
                            "current_grade": "A-",
                        },
                    },
                }
            }
        },
        "A-",
    ),
    (
        {
            "type": {
                "student": {
                    "name": "Lane",
                    "courses": {
                        "math_1050": {
                            "current_grade": "D-",
                        },
                        "English_1010": {
                            "current_grade": "B+",
                        },
                    },
                }
            }
        },
        "B+",
    ),
]

submit_cases = run_cases + [
    (
        {
            "type": {
                "student": {
                    "name": "Breanna",
                    "courses": {
                        "math_1050": {
                            "current_grade": "A",
                        },
                        "English_1010": {
                            "current_grade": "A",
                        },
                    },
                }
            }
        },
        "A",
    ),
    (
        {
            "type": {
                "student": {
                    "name": "Tiff",
                    "courses": {
                        "math_1050": {
                            "current_grade": "A-",
                        },
                        "English_1010": {
                            "current_grade": "B-",
                        },
                    },
                }
            }
        },
        "B-",
    ),
    (
        {
            "type": {
                "student": {
                    "name": "Ali",
                    "courses": {
                        "math_1050": {
                            "current_grade": "B+",
                        },
                        "English_1010": {
                            "current_grade": "C-",
                        },
                    },
                }
            }
        },
        "C-",
    ),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Student Dictionary: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_english_grade(input1)
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
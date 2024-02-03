"""
SLICING LISTS

Python makes it easy to slice and dice lists to work only with the section you care about. 
One way to do this is to use the simple slicing operator, which is just a colon :.

With this operator, you can specify where to start and end the slice, and how to step through the original. 
List slicing returns a new list from the existing list.

The syntax is as follows:

my_list[ start : stop : step ]

For example,

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

OMITTING SECTIONS

You can also omit various sections ("start", "stop", or "step"). 
For example, numbers[:3] means "get all items from the start up to (but not including) index 3". 
numbers[3:] means "get all items from index 3 to the end".

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

USING ONLY THE "STEP" SECTION

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

NEGATIVE INDICES

Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]
"""

# Assignment
# Complete the given get_champion_slices function. 
# It takes a list of champions and should return three new lists based on the given champions:

# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
# Next, return a slice of the champions list that starts at the beginning of the list and ends with the third champion from the end (inclusive).
# Last, return a slice of the champions list that only includes the champions in even numbered indexes.

# Solution
def get_champion_slices(champions):
    # Slice from the third champion to the end of the list
    first_slice = champions[2:]

    # Slice from the beginning of the list to the third champion from the end (inclusive)
    second_slice = champions[:-2]

    # Slice to include only the champions in even numbered indexes
    third_slice = champions[::2]

    return first_slice, second_slice, third_slice


# Tests
run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
]

submit_cases = run_cases + [
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
    (([]), ([], [], [])),
]

def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expecting:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
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

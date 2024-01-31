"""
INDEXING INTO LISTS

Now that we know how to create new lists, we need to know how to access specific items in the list.

We access items in a list directly by using their index. 
Indexes start at 0 (the first item) and increment by one with each successive item. 
The syntax is as follows:

best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided
"""

# Assignment
# Fix our get_leather_scraps function by changing the value of item_index to the index in inventory that holds the value "Leather Scraps".

# Solution
def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

# Tests
run_cases = [
    ("Leather Scraps",),
]

submit_cases = run_cases + [
    ("Leather Scraps",),
]

def test(expected_output):
    print("---------------------------------")
    print(f"Expecting: {expected_output}")
    result = get_leather_scraps()
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
"""
MORE LOOPS PRACTICE

As a reminder, a "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)
"""

# Assignment
# In the print_numbers_from_five_to function, the for-loop starts at '0'. Edit the for-loop to start at 5.

# Solution
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

# Tests
def test(end):
    print(f"Printing numbers from 5 until {end}:")
    print_numbers_from_five_to(end)
    print("=====================================")

def main():
    test(16)
    test(6)
    test(11)

main()

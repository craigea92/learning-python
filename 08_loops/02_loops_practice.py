"""
LOOPS PRACTICE

As a reminder, a "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)
"""

# Assignment
# In the print_numbers function, write a for-loop from scratch that logs the numbers 0-199 to the console.

# Solution
def print_numbers():
    for i in range(0, 200):
        print(i)

# Tests
def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")

def main():
    test()

main()

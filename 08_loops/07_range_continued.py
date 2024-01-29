"""
RANGE CONTINUED

The range() function we've been using in our for loops actually has an optional 3rd parameter: the "step".

for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

The "step" parameter determines how much to add to i in each iteration of the loop. You can even go backwards:

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
"""

# Assignment
# Fix the for loop in the count_down function so that it prints the numbers counting down from start to (but not including) end in order.

# Solution
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

# Tests
def test(start, end):
    print(f"Printing numbers from {start} until {end}:")
    count_down(start, end)
    print("=====================================")

def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)

main()

"""
LOOPS

Loops are a programmer's best friend. 
Loops allow us to do the same operation multiple times without having to write it explicitly each time.

For example, let's pretend I want to print the numbers 0-9.

I could do this:

print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

Even so, it would save me a lot of time typing to use a loop. 
Especially if I wanted to do the same thing one thousand or one million times.

A "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)

In English, the code says:

1. Start with i equals 0. (i in range(0)
2. If i is not less than 10 (range(0, 10)), exit the loop.
3. Print i to the console. (print(i))
4. Add 1 to i. (range defaults to incrementing by 1)
5. Go back to step 2

The result is that the numbers 0-9 are logged to the console in order.
"""

# Assignment
# Complete the missing sections of the for-loop in the print_numbers function so that it prints the numbers 0-99 to the console.

# Solution
def print_numbers():
    for i in range(0, 100):
        print(i)

# Tests
def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")

def main():
    test()

main()

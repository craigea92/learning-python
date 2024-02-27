"""
FIZZBUZZ

Fizzbuzz is a commonly overused little toy-program that comes up in entry-level interviews.
"""

# Assignment
# Complete the fizzbuzz function that loops over all the numbers from start to end (excluding the end value) and prints them. 
# If the number is a multiple of 3, instead of printing the number, print "fizz". If the number is a multiple of 5, instead print "buzz". 
# If it is a multiple of 3 and 5 then instead print "fizzbuzz".

# Solution
def fizzbuzz(start, end):
    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Tests
def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)

def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")

main()

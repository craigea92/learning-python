"""
ROCKET LAUNCH

A team of scientists is getting ready to launch the rockets they have been working on. 
You've been asked to write a program that will countdown to the rockets' launch.
"""

# Assignment 
# In the countdown_to_blastoff function, write a loop that counts down from 10 to 1. At each iteration, it should print:
# NUM...
# Where NUM is replaced with the current number in the countdown. However, when NUM is 1, it should instead print:
# NUM... Blastoff!

# Solution
def countdown_to_blastoff():
    for i in range(10, 0, -1):
        if i == 1:
            print(str(i) + "... Blastoff!")
        else:
            print(str(i) + "...")

# Tests
def test():
    print("Counting down to blastoff:")
    countdown_to_blastoff()
    print("=====================================")

def main():
    test()

main()



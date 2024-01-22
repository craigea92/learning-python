"""
WHERE TO DECLARE FUNCTIONS

You've probably noticed that a variable needs to be declared before it's used. 
For example, the following doesn't work:

print(my_name)
my_name = 'Craig Eaton'

It needs to be:

my_name = 'Craig Eaton'
print(my_name)

Lines of code execute in order from top to bottom, so a variable needs to be created before it can be used.
That means that if you define a function, you can not call that function until after the definition.

The main() function is a convention used in many programming languages to specify the entry point of an application. 
By defining a single main function, and only calling main() at the end of the entire program we ensure that all of our functions are defined before they're called.
"""

# Assignment
# Fix the order of this code block

main()
print("Game is running!")
def main():
    print("Fantasy Quest is booting up...")

# Solution
def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()


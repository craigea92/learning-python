"""
ORDER OF FUNCTIONS

All functions must be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be just right. 
As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining all the functions in their program first, then finally calling the "entry point" function last. 
Conventionally this "entry point" function is usually called main to keep things simple and consistent.

If you follow this pattern you can forget about ordering. All of the functions have been read by the Python interpreter before the first one is called.

def main():
    func2()

def func2():
    func3()

def func3():
    print("I'm function 3")

# call entrypoint last
main()
"""

# Question 01

# Functions must be defined before they can be called

# True
# False

# Answer = True

# Question 02

# Python functions must be defined in the order they call one another

# True
# False

# Answer = False

# Question 03

# The entrypoint function must be called 'main'

# Yes
# No, but it must be called 'entrypoint'
# No, but developers usually call it 'main' to keep things consistent

# Answer = No, but developers usually call it 'main' to keep things consistent
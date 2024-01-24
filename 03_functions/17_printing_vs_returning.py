"""
PRINTING VS RETURNING

Some new developers get hung up on the difference between print() and return.

It can be particularly tricky when the test suite we provide prints the output of your functions to the console. 
This makes it seem like print() and return are interchangeable, but they are not!

print():
A function that prints a value to the console.
It does NOT return a value.

return:
A keyword that ends the function execution.
It gives the specified value back to the caller of the function.
It does NOT print anything to the console.

PRINTING TO DEBUG YOUR CODE

Printing values and running your code in the console is a great way to debug your code. 
You can see what values are stored in various variables, find your mistakes, and fix them. 
Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

In the real world make sure not to leave print() statements in your code once you're done debugging. 
"""
# Assignment 
# Fix the get_title function so it returns the title

# Solution
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title

# Tests
def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")

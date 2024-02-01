"""
NO-INDEX SYNTAX

Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. 
If you don't need the index number you can use the following syntax:

trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple

tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. 
If we don't need to update the item and only need to access its value then this is a more clean way to write the code.
"""

# Question 01

# When should we use the no-index syntax?

# When we want to write code that is harder to read
# When we need our code to be faster
# When we don't need to know the index, just the value

# Answer = When we don't need to know the index, just the value

# Question 02

# Which method of writing for-loops is considered more 'clean' assuming both options will work?

# for item in items
# for i in range(0, len(items))


# Answer = for item in items
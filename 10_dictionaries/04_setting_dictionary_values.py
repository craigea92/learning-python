"""
SETTING DICTIONARY VALUES

You don't need to create a dictionary with values already inside. 
It is common to create a blank dictionary then populate it later using dynamic values. 
The syntax is the same as getting data out of a key, just use the assignment operator (=) to give that key a value.

names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_lst = name.split()

    # here we update the dictionary
    names_dict[name_lst[0]] = name_lst[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}
"""

# Question 01

# Which is the correct syntax to create a new key/value pair in an existing dictionary?

# dict[key] = value
# dict[key] -> value
# dict...key = value
# dict(key) = value

# Answer = dict[key] = value
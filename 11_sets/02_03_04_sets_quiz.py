"""
SETS QUIZ

Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

ADDING VALUES

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

EMPTY SET

Because the {} syntax creates an empty dictionary, to create an empty set, just use the set() function.

fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}

ITERATE OVER VALUES IN A SET (ORDER IS NOT GUARANTEED)

fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

REMOVING VALUES

fruits = {'apple', 'banana', 'grape'}
fruits.remove('apple')
print(fruits)
# Prints: {'banana', 'grape'}
"""

# Question 01

# How do I remove an item from a set?

# my_set.remove('item')
# my_set.del('item')
# delete my_set['item']
# del my_set['item']

# Answer = my_set.remove('item')

# Question 02

# What is the type of my_val in the following statement: my_val = {}

# Set
# Map
# List
# Dictionary

# Answer = Set

# Question 03

# Which would be a good use of a set?

# To store id -> user pairs
# To store all the possible spells in a game
# To store all the enemies in a game by difficulty

# Answer = To store all the enemies in a game by difficulty
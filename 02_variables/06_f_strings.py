"""
F-STRINGS IN PYTHON

you can create a string with dynamic values by using f-strings in Python.
It's a beautiful syntax that I wish more programming languages used.

num_bananas = 10
print(f"You {num_bananas} bananas)
# You have 10 bananas

The opening quotes must be preceded by an f.
Any variables within curly brackets have their values "interpolated" (injected) into the string.
"""

# Assignment
# Fix the code below to insert the dynamic values

name = "Yarl"
age = 37
race = "dwarf"

print(f"Yarl is a dwarf who is 37 years old.")

# Solution
name = "Yarl"
age = 37
race = "dwarf"

print(f"{name} is a {race} who is {age} years old.")

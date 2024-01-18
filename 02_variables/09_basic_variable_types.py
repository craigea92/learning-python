"""
BASIC VARIABLE TYPES

In Python there are several basic data types.

STRING TYPE

They are called strings because they are a list of characters strung together.
Strings are declared in Python by using single quotes or double quotes.
For consistency's sake, we prefer double quotes.

here_is_a_string_variable = "Craig is learning Python"

NUMERIC TYPES

Numbers aren't surrounded by quotes when created, but they can have decimals and negative signs.

integers = 5
negative_integers = -5

float = 5.2
negative_float = -5.2

BOOLEAN TYPE

A boolean (or bool) is a type that can only have one of two values: True or False.
As you may have heard computers really only use 1's and 0's.
These 1's and 0's are just Boolean values

0 = False
1 = True

is_boolean = True
"""

# Assignment
# Fix the variable types in the code below.

player_health = "100"
player_has_magic = "True"

print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")

# Solution
player_health = 100
player_has_magic = True

print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")
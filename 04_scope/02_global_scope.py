"""
GLOBAL SCOPE

So far we've been working in the global scope. 
That means that when we define a variable or a function, that name is accessible in every other place in our program, even within other functions.

pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius

Because pi was declared in the parent "global" scope, it is usable within the get_area_of_circle() function.
"""

# Assignment
# Declare a variable player_level at the top of the global scope and set it to 4.

# Solution
player_level = 4

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

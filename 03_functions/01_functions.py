"""
FUNCTIONS

Functions allow us to reuse and organise code.
For example, say we've written some code that calculates the area of a circle:

radius = 5
area = 3.14 * radius * radius

This works great! The problem arises when we want to calculate the area of more circles, each with their own radius.
We could just copy the code and change the variable names like this:

radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2

radius3 = 11
area3 = 3.14 * radius3 * radius3


But we want to reuse the same code. Instead, we can declare a new function, lets call it area_of_circle.
Notice the def keyword is written before the function name, this tell the Python interpreter that we're defining a new function.

def area_of_circle(r):
    pi = 3.14
    return pi * r * r

The area_of_circle function takes one input (which can also be called a "parameter" or "argument") and returns one output. 
The body of the function is indented and contains the code that will be executed when the function is called. 
The return keyword tells the function to return the value of the expression that follows it.

To use or "call" this function we can now pass in any number as the input (in this case, the radius), and capture the output into a new variable:

radius = 5
area = area_of_circle(radius)
print(area)

Here's a full example:

def area_of_circle(r):
    pi = 3.14
    return pi * r * r

radius = 5
area = area_of_circle(radius)
print(area)
# 78.5

radius = 6
area = area_of_circle(radius)
print(area)
# 113.04
"""

# Assignment
# We need to calculate the size of a weapon's "attack area".
# The axe_area and spear_area variables should be set to the correct values instead of 0. 
# You'll need to use the axe_length and spear_length variables.

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
axe_length = 0.5
spear_length = 2.0

# Solution
sword_area = area_of_circle(sword_length)
axe_area = area_of_circle(axe_length)
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Axe length:", axe_length, "meters.")
print("Axe attack area:", axe_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")



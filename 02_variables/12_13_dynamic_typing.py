"""
DYNAMIC TYPING

Python is dynamically typed.
All this means is that a variable can store any type, and that can change.

For example, if I make a number variable, I can later change that variable to a string:

This is valid:

speed = 5
speed = "five"

JUST BECAUSE YOU CAN DOESN"T MEAN YOU SHOULD!

In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one.

For example:
speed = 5
speed_description = "five"

WHAT IF IT WEREN"T DYNAMICALLY TYPED?

Statically typed languages like Go are statically typed instead of dynamically typed.
In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash your program.

If Python were statically-typed, the first example from before would crash on the second line, speed = "five". 
The computer would give an error along the lines of you can't assign a string value ("five") to a number variable (speed).

TYPE INFERENCE

Newer Languages (e.g. TypeScript, Go and Rust) feature type inference.
This combines static typing with a simpler syntax, allowing the compiler to infer types from initial values
"""

# Question 01

# Is changing the type of a variable generally a good idea?

# Yes
# No

# Answer = No

# Question 02

# What kind of typing does Python employ?

# Static
# Dynamic

# Answer = Dynamic
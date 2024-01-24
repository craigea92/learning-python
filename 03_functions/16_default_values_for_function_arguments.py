"""
DEFAULT VALUES FOR FUNCTION ARGUMENTS

Python has a way to specify a default value for function arguments. 
This can be convenient if a function has arguments that are essentially "optional", and you as the function creator want to use a specific default value in case the caller doesn't provide one.

A default value is created by using the assignment (=) operator in the function signature.

def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

get_greeting("lane@example.com", "Lane")
# Hello Lane welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there welcome! You've registered your email: lane@example.com

If the second parameter is omitted, the default "there" value will be used in its place. 
As you may have guessed, for this structure to work, optional arguments that have defaults specified come after all the required arguments.
"""

# Assignment
# Complete both the get_punched and get_slashed functions. They should each take 2 arguments.
# Change the functions so if no armor argument is passed, armor defaults to 0.
# Getting punched does 50 damage. Getting slashed does 100 damage.

# Solution
def get_punched(health, armor=0):
    damage_taken = 50 - armor
    health -= damage_taken
    return health

def get_slashed(health, armor=0):
    damage_taken = 100 - armor
    health -= damage_taken
    return health

# Tests
def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")

test(400, 5)
test(300, 3)
test(200, 1)


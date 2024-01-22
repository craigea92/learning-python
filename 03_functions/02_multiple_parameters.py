"""
MULTIPLE PARAMETERS

Functions can have multiple parameters (which is just a fancy name for "inputs"). 
For example, this subtract function accepts 2 parameters: a and b.

def subtract(a, b):
    result = a - b
    return result

Naming parameters doesn't matter as much as setting their order. 
The first parameter is the first value that you pass in, the second parameter is the second value that you pass in, and so on. 
In this example, the subtract function is called with a = 5 and b = 3:

result = subtract(5, 3)
print(result)

This next function accepts 4 parameters: name, age, height, and weight.

def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + ". You are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

It could be called like this:

intro = create_introduction("John", 30, 1.8, 80)
print(intro)
# Your name is John. You are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
"""

# Assignment
# Complete the calculate_damage function and return the results of adding all the damage together.

# Solution
def calculate_damage(opening_attack, core_damage, finishing_move):
  total_damage = opening_attack + core_damage + finishing_move
  return total_damage

dmg_one = 2
dmg_two = 4
dmg_three = 3
print("Getting damage for", dmg_one, dmg_two, "and", dmg_three, "...")
print(calculate_damage(dmg_one, dmg_two, dmg_three), "points of damage dealt!")
print("=====================================")

dmg_four = -1
dmg_five = 10
dmg_six = 5
print("Getting damage for", dmg_four, dmg_five, "and", dmg_six, "...")
print(calculate_damage(dmg_four, dmg_five, dmg_six), "points of damage dealt!")
print("=====================================")

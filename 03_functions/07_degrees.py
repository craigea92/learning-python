"""
FUNCTIONS PRACTICE - DEGREES

Conversion Formula

celsius = 5/9 * (fahrenheit-32)
"""

# Assignment
# Write a function called to_celsius that returns the temperature converted from Fahrenheit to Celsius

# Solution
def to_celsius(fahrenheit):
  celsius = 5/9 * (fahrenheit-32)
  return celsius

def test(fahrenheit_input):
    celcius_rounded = round(to_celsius(fahrenheit_input), 2)
    print(fahrenheit_input, "degrees fahrenheit is", celcius_rounded, "degrees celsius")

test(100)
test(88)
test(104)
test(112)

# 100 degrees fahrenheit is 37.78 degrees celsius
# 88 degrees fahrenheit is 31.11 degrees celsius
# 104 degrees fahrenheit is 40.0 degrees celsius
# 112 degrees fahrenheit is 44.44 degrees celsius
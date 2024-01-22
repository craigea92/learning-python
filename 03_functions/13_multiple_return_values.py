"""
MULTIPLE RETURN VALUES

In Python, we can return more than one value from a function.

First, we can return multiple values on one line by separating them with commas.

# returns email, age, and status of the user
def get_user():
    return "name@domain.com", 21, "active"

When we call this function, we need to assign all the returned values to an equal number of variables by separating them with commas. 
The values will be assigned according to the order they are returned.

# sets email, age, and status to values returned from get_user() function
email, age, status = get_user()
print(email, age, status)
# name@domain.com 21 active
"""

# Assignment
# Complete the become warrior function.
# It accepts 3 inputs, it should return 2 values:
# First, a string of this format: "first_name last_name the warrior"
# Second, the power input after adding 1 to it.

# Solution
def become_warrior(first_name, last_name, power):
  title_string = first_name + " " + last_name + " the warrior"
  power_level = power + 1
  return title_string, power_level

def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power_level):
    title_string, power = become_warrior(first_name, last_name, power_level)
    print(title_string, "has a power level of:", power)

main()
"""
UPDATING DICTIONARY VALUES

If you try to set the value of a key that already exists, you'll end up just updating the value of that key.

full_names = ["jack bronson", "james mcarty", "jack denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

print(names_dict)
# {
#   'jack': 'denver',
#   'james': 'mcarty'
# }
"""

# Question 01

# What happens if you assign a new value to an existing key?

# The value updates
# The key and value are deleted
# A collision error occurs

# Answer = The value updates
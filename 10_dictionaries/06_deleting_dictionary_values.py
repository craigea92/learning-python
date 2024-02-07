"""
DELETING DICTIONARY VALUES

You can delete existing keys using the del keyword.

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['joe']

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

DELETING KEYS THAT DON'T EXIST

Notice that if you try to delete a key that doesn't exist, you'll get an error.

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['unknown']
# ERROR HERE, key doesn't exist
"""

# Question 01

# What happens if you try to 'del' a key that doesn't exist in the dictionary?

# The existing value is returned
# Nothing
# Error

# Answer = Error
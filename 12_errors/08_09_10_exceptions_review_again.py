"""
RAISING EXCEPTIONS REVIEW
As you've noticed, there are many kinds of exceptions. 
Many specific exceptions are built into the language like IndexError and ZeroDivisionError, and (almost) all Exceptions count as the parent Exception type.
"""

# Question 01

try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")

# In the code sample, what will happen?

# The program will crash with an uncaught error
# It will print 'zero'

# Answer = The program will crash with an uncaught error

# Question 02
    
try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")

# In the code sample, what will happen?

# The program will crash with an uncaught error
# It will print 'zero'
# It will print 'other'

# Answer = It will print 'other'

# Question 03
    
try:
    10/0
except Exception as e:
    print("other")

# In the code sample, what will happen?

# The program will crash with an uncaught error
# It will print 'other'

# Answer = False
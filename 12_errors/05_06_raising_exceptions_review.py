"""
RAISING EXCEPTIONS REVIEW

Software applications aren't perfect, and user input and network connectivity are far from predictable. 
Despite intensive debugging and unit testing, applications will still have failure cases.

Loss of network connectivity, missing database rows, out of memory issues, and unexpected user inputs can all prevent an application from performing "normally". 
It is your job to catch and handle any and all exceptions gracefully so that your app keeps working. 
When you are able to detect that something is amiss, you should be raising the errors yourself, in addition to the "default" exceptions that the Python interpreter will raise.

raise Exception("something bad happened")
"""

# Question 01

# Which keyword triggers an exception in Python?

# throw
# raise
# exception
# error

# Answer = raise

# Question 02

# Good code doesn't need to handle errors, it should be error-free

# True
# False

# Answer = False
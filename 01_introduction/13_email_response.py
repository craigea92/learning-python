"""
EMAIL RESPONSE

A new online store has been migrating to a new software system for its inventory management. 
The last thing they need to do for the new system to be fully operational is complete their survey response messages.

They assigned someone with no Python experience to work on it. 
As you'd expect, there are now bugs in the code, and you have been asked to fix the report.
"""

# Assignment
# The print section of the report should be:

"Thank you for shopping at Bootmart!"
"Your total today was:"

# Solution
items_in_cart = 5
cost_of_each_item = 2.50
total_cost = items_in_cart * cost_of_each_item

# Don't Touch Above This line

print("Thank you for shopping at Bootmart!")
print("Your total today was:")

# Don't Touch Below This Line

print(f"${total_cost:.2f}")


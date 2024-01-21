"""
EMAIL OUTPUT

An e-commerce store has configured an automated receipt, but can't figure out how to print the email message in the correct order.
"""

# Assignment
# Add some print statements to the end of the code to get the expected output:

# Thank you for shopping with us!
# Your total today was: $20.25
# Please consider filling out our customer survey.

email_start = "Thank you for shopping with us!"
email_middle = "Your total today was: "
email_end = "Please consider filling out our customer survey."
dollar_sign = "$"
total_price = "20.25"

# Solution

print(email_start)
print(email_middle + dollar_sign + total_price)
print(email_end)
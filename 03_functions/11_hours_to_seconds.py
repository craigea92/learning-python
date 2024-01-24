"""
HOURS TO SECONDS

We need to be able to display the current time to our players.
The problem is that the time is stored as a number of hours, but we want to display it as a number of seconds.
"""

# Assignment
# Write the hours_to_seconds function. It should convert hours to seconds.

# Solution
def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

# Tests
def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)

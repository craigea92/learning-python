"""
SQUARING NUMBERS

John is finishing some math homework and needs to calculate the square of some numbers. 
However, he's getting tired of entering each of them into a calculator individually.

"""

# Assignment
# In the calculate_squares function, write a loop that calculates and prints the squares of the numbers from the start parameter up to the given end parameter.
# Use the following format to print each line:
# NUM squared = SQUARE

# Solution
def calculate_squares(start, end):
    for num in range(start, end):
        square = num * num
        print(f"{num} squared = {square}")

# Tests
def test(start, end):
    print(f"Calculating squares from {start} until {end}:")
    calculate_squares(start, end)
    print("=====================================")

def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)

main()

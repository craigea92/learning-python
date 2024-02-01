"""
POP VALUES

.pop() is the opposite of .append(). 
Pop removes the last element from a list and returns it for use. For example:

vegetables = ["broccoli", "cabbage", "kale", "tomato"];
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'
"""

# Assignment
# Pop the last element from the inventory list until there is nothing left. 
# Pop the elements into an item variable so that each prints in turn.

# Solution
def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    for i in range(0, len(inventory)):
        item = inventory.pop()

        print(f"Selling: {item}")
        print(f"inventory: {inventory}")

# Tests
def test():
    clear_inventory()
    print("=====================================")

def main():
    test()

main()

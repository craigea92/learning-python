"""
LIST UPDATES

We can also change the item that exists at a given index. 
For example, we can change Leather to Leather Armor in the inventory list in the following way:

inventory = ["Leather", "Healing Potion", "Iron Ore"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Healing Potion', 'Iron Ore']
"""

# Assignment
# On line 7, update the Iron Ore element in the list to be an Iron Bar.

# Solution
def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
    print(f"Inventory: {inventory}")

    inventory[1] = "Iron Bar"

    return inventory

# Tests
def test():
    inventory = smelt_ore()
    print(f"Smelting ore: {inventory}")
    print("=====================================")

def main():
    test()

main()

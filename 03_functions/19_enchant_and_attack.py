"""
ENCHANT AND ATTACK

In Fantasy Quest, a weapon can be enchanted to do bonus damage.
"""

# Assignment
# Calculate and store the "enchanted damage" in a new variable. The enchanted damage should be the input damage plus 10.
# Calculate and store the "new health" in a new variable. The new health should be the input player_health minus the enchanted damage.
# Create a new variable called enchanted_weapon. It should be the input weapon with the string "enchanted " added to the beginning of it.

# Solution
def enchant_and_attack(player_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = player_health - enchanted_damage
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health

# Tests
def test(player_health, damage, weapon):
    print("The victim has", player_health, "health.")
    print(weapon, "does", damage, "damage. Enchanting and attacking...")
    enchanted_weapon, new_health = enchant_and_attack(player_health, damage, weapon)
    print("The victim has been attacked with the", enchanted_weapon)
    print("The victim has", new_health, "health remaining.")
    print("=====================================")

def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")

main()
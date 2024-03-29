"""
CURSE

An enemy's weapons can be cursed so that they don't deal as much damage.
"""

# Assignment
# Complete the curse function. It accepts a weapon_damage parameter and returns two values:
# The lesser_cursed damage: 50% of the input weapon_damage.
# The greater_cursed damage: 25% of the input weapon_damage.

# Solution
def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed

# Tests
def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

def main():
    test(100)
    test(500)
    test(1000)

main()
"""
FIX YOUR FIRST BUG
The combat system in Fantasy Quest isn't working as intended! 
It appears that players are gaining health when attacked instead of losing it.
"""

# Assignment
# Fix the math bug in this code.

sword_damage = 10
player_health = 100
health_after_attack = player_health + sword_damage

print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred is hit by a sword for {sword_damage} damage...")
print(f"Lollilfred's health is now: {health_after_attack}")


# Solution
sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred is hit by a sword for {sword_damage} damage...")
print(f"Lollilfred's health is now: {health_after_attack}")
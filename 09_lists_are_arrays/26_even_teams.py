"""
EVEN TEAMS

Students at the local wizarding school have been spending too much time trying to split their players up into even teams. 
The coach has provided you with a list of the players in the class and has asked you to write a program that will split the players into even teams.
"""

# Assignment 
# Complete the split_players_into_teams function:
# even_team should have the players with even-numbered indexes.
# odd_team should have the players with odd-numbered indexes.
# Return even_team and odd_team in that order.

# Solution
def split_players_into_teams(players):
    even_team = players[0::2]
    odd_team = players[1::2]

    return even_team, odd_team

# Tests
run_cases = [
    (
        [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ],
        (
            ["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],
            [
                "Hermione",
                "Ginny",
                "Neville",
                "Luna",
                "Gregory",
                "Michael",
                "Frank",
                "Allan",
            ],
        ),
    ),
    (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])),
]

submit_cases = run_cases + [
    (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
    ([], ([], [])),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = split_players_into_teams(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

if "__RUN__" in globals():
    test_cases = run_cases
else:
    test_cases = submit_cases

main()
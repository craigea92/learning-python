"""
FILTER MESSAGES

You are about to write a bit more code in a single function than you have before.

Do not try to write it all at once. Start with the outermost loop, and work your way inwards. 
Add extra print() statements and run your code often to make sure it's doing what you expect. 
Just make sure to remove the extra print() statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called "debugging". 
All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.
"""

# Assignment
# Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:
# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.

# Solution
def filter_messages(messages):
    filtered_messages = []
    word_counts_removed = []

    for message in messages:
        words = message.split()  # Split the message into a list of words
        clean_message = []  # Create a new empty list for non-bad words
        count_removed = 0  # Counter for removed words

        for word in words:
            if word == "dang":
                count_removed += 1
            else:
                clean_message.append(word)

        clean_message_str = " ".join(clean_message)  # Join the non-bad words into a single string
        filtered_messages.append(clean_message_str)  # Append the clean message to the list of filtered messages
        word_counts_removed.append(count_removed)  # Append the count of bad words removed to its list

    return filtered_messages, word_counts_removed

# Tests
run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]

def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expecting:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
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

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
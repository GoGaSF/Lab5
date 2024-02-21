import re

def match_pattern(text):
    pattern = r'ab{2,3}'
    match = re.search(pattern, text)

    if match:
        print("String matches the pattern.")
    else:
        print("String does not match the pattern.")
if __name__ == "__main__":
    test_strings = ["abb", "abbb", "abbbb", "a", "abc", "aabb", "ab"]

    for test_string in test_strings:
        print(f"Testing string: {test_string}")
        match_pattern(test_string)

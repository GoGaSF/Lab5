import re

def match_pattern(text):
    pattern = r'ab*'  
    match = re.match(pattern, text)

    if match:
        print("String matches the pattern.")
    else:
        print("String does not match the pattern.")

if __name__ == "__main__":
    test_strings = ["ab", "abb", "a", "abbb", "ac"]

    for test_string in test_strings:
        print(f"Testing string: {test_string}")
        match_pattern(test_string)

import re

def replace_with_colon(text):

    pattern = r'[ ,.]'


    result = re.sub(pattern, ':', text)

    return result
if __name__ == "__main__":
    test_string = "This is, a test. String with spaces, commas. and dots."
    replaced_string = replace_with_colon(test_string)

    print("Original string:", test_string)
    print("String with space, comma, and dot replaced with colon:", replaced_string)

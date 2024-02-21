import re

def insert_spaces(string):

    pattern = r'(?<!^)(?=[A-Z])'
    modified_string = re.sub(pattern, ' ', string)

    return modified_string


if __name__ == "__main__":
    input_string = "ThisIsAStringWithWordsStartingWithCapitalLetters"
    modified_string = insert_spaces(input_string)
    print(input_string)
    print( modified_string)

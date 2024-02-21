import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, text)

    return sequences
if __name__ == "__main__":
    test_string = "hello_world is_a_sequence abc_def_xyz test_test_test"
    sequences = find_sequences(test_string)

    if sequences:
        print("Sequences found:")
        for sequence in sequences:
            print(sequence)
    else:
        print("No sequences found.")

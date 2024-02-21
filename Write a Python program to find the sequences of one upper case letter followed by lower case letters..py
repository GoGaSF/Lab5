import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'

    sequences = re.findall(pattern, text)

    return sequences
if __name__ == "__main__":
    test_string = "The Quick Brown fox Jumps over the Lazy Dog"
    sequences = find_sequences(test_string)

    if sequences:
        print("Sequences found:")
        for sequence in sequences:
            print(sequence)
    else:
        print("No sequences found.")

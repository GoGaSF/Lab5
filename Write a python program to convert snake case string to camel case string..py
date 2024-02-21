def snake_to_camel(snake_case_str):
    words = snake_case_str.split('_')

    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case_str = ''.join(camel_case_words)

    return camel_case_str

if __name__ == "__main__":
    snake_case_string = "hello_world_this_is_snake_case"
    camel_case_string = snake_to_camel(snake_case_string)
    print("Snake case string:", snake_case_string)
    print("Camel case string:", camel_case_string)

def camel_to_snake(camel_case_str):
    snake_case_str = ''
    for char in camel_case_str:
        if char.isupper():
            snake_case_str += '_' + char.lower()
        else:
            snake_case_str += char
    if snake_case_str.startswith('_'):
        snake_case_str = snake_case_str[1:]
    return snake_case_str
if __name__ == "__main__":
    camel_case_string = "convertThisCamelCaseStringToSnakeCase"
    snake_case_string = camel_to_snake(camel_case_string)
    print(camel_case_string)
    print( snake_case_string)

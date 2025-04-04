import re

#Task 1
def match_a_followed_by_b(s):
    return bool(re.fullmatch(r'ab*', s))

#Task 2
def match_a_followed_by_2to3_b(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

#Task 3
def find_lowercase_with_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

#Task 4
def find_upper_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

#Task 5
def match_a_anything_b(s):
    return bool(re.fullmatch(r'a.*b', s))

#Task 6
def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]', ':', s)

#Task 7
def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

#Task 8
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

#Task 9
def insert_spaces_before_capitals(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

#Task 10
def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


if __name__ == "__main__":
    print(match_a_followed_by_b("ab"))
    print(match_a_followed_by_2to3_b("abb"))
    print(find_lowercase_with_underscore("hello_world test_case"))
    print(find_upper_followed_by_lower("Hello World Test"))
    print(match_a_anything_b("axb"))
    print(replace_space_comma_dot("Hello, world. How are you?"))
    print(snake_to_camel("hello_world_test"))
    print(split_at_uppercase("HelloWorldTest"))
    print(insert_spaces_before_capitals("helloWorldTest"))
    print(camel_to_snake("HelloWorldTest"))
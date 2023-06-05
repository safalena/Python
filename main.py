# Tasks 1
def fizz_buzz_task():
    for i in range(1, 101):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if len(result) == 0:
            result = i
        print(result)


# Task 2
def find_min_max_task():
    initial_list = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    converted_numbers = []
    for i in initial_list:
        if str(i).lstrip('-').replace('.', '').isdigit():
            converted_numbers.append(int(i))
    print(f'Initial list: {initial_list}')
    print(f'Converted list: {converted_numbers}.')
    min_value = converted_numbers[0]
    max_value = converted_numbers[0]
    for i in converted_numbers:
        if min_value > i:
            min_value = i
        if max_value < i:
            max_value = i
    print(f"Min: {min_value}, Max: {max_value}")


# Task 3
def letters_count_task(text):
    import re
    import string

    clean_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    words = clean_text.split(' ')
    characters_only = re.sub(' ', '', clean_text)
    characters_only.lower()
    # print(characters_only)
    character_count = 0
    max_character = 'a'
    max_count = 0
    for i in string.ascii_lowercase:
        for character in characters_only:
            if character == i:
                character_count += 1
        if max_count<character_count:
            max_count = character_count
            max_character = i
        character_count = 0
    python_count = 0
    for word in words:
        if word == 'Python':
            python_count += 1
    # print(words)
    print(f'Word "Python" appears in text {python_count} times.')
    print(f'Character {max_character} is the most popular character, it appears in text {max_count} times.')


# Task4
def file_size_conversion_task(size_in_bytes):
    # size_in_bytes = int(input())
    converted_size = str(size_in_bytes)
    if size_in_bytes//(1024**3) > 0:
        converted_size = str(round(size_in_bytes/(1024**3), 1)) + 'Gb'
    elif size_in_bytes//(1024**2) > 0:
        converted_size = str(round(size_in_bytes/(1024**2), 1)) + 'Mb'
    elif size_in_bytes//(1024) > 0:
        converted_size = str(round(size_in_bytes/(1024), 1)) + 'Kb'
    else:
        converted_size = str(size_in_bytes) + '.0B'
    return converted_size


# Task 5
def sum_of_multiples_task(number):
    sum_of_multiples = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples


print('Task 1', fizz_buzz_task())

print('Task 2')
find_min_max_task()

print('Task 3')
text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
   Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
   Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!"""
letters_count_task(text)

print('Task 4')
assert file_size_conversion_task(19) == '19.0B'
assert file_size_conversion_task(12345) == '12.1Kb'
assert file_size_conversion_task(1101947) == '1.1Mb'
assert file_size_conversion_task(572090) == '558.7Kb'
assert file_size_conversion_task(999999999999) == '931.3Gb'
print('All checks passed')

print('Task 5')
for count in [10, 100, 1000, 10000, 100000000]:
    print(f'For {count} sum of multiples 3 and 5 is {sum_of_multiples_task(count)}.')
#sum_of_multiples_task(1000)
#sum_of_multiples_task(1000000)
#sum_of_multiples_task(1000000000)
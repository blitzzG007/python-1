#String concatenation joins two or more strings together into a single string
my_str1 = 'Hello'
my_str2 = 'World'

together_str = my_str1 + ' ' + my_str2

print(together_str)

sound = 'ha'

repeated_sound = sound + 'HA' * 7

print(repeated_sound)

name = 'John Doe'
age = 23

name_and_age = name + ' ' + 'is' + ' ' + str(age)

print(name_and_age)



#String Interpolation (this one is for the f/F string(it's the easiest), there are more)
Name = 'Alice'
Age = 24

print(f'Hello, {Name}! You are {Age} years old.')

print(f'In a few months you will be {Age + 1}, so happy early birthday {Name} 🥳🎂')


#String slicing
#string = Hello
# print(string[1:4]) #ello
greeting = 'Hello World'

print(greeting[1:11]) # output = ello World





# Common String Methods

# upper(): Returns a new string with all characters converted to uppercase.
# my_str = 'hello world'
# uppercase_my_str = my_str.upper()
# print(uppercase_my_str) # output = HELLO WOLRD


# lower(): Returns a new string with all characters converted to lowercase.
# my_str = 'Hello World'
# lowercase_my_str = my_str.lower()
# print(lowercase_my_str) # output = hello world


# strip(): : Returns a new string with the specified leading and trailing characters removed.
# If no argument is passed it removes leading and trailing whitespace.
# my_str = '  hello world  '
# trimmed_my_str = my_str.strip()
# print(trimmed_my_str)  # output = "hello world"


# replace(old, new): Returns a new string with all occurrences of old replaced by new.
# my_str = 'Hey Alice do wanna jump me to the theater later?'
# replaced_word = my_str.replace('jump', 'join')
# print(replaced_word)  # output = Hey Alice do wanna join me to the theater later?


#split(separator): Splits a string on a specified separator into a list of strings.
# If no separator is specified, it splits on whitespace.
# my_str = 'banana cherry watermelon apple orange kiwi'
# split_words = my_str.split()
# print('What is your favourite fruit out of this 6 fruits?: ', split_words)
# output = What is your favourite fruit out of this 6 fruits?:  ['banana', 'cherry', 'watermelon', 'apple', 'orange', 'kiwi']


# join(iterable): Joins elements of an iterable into a string with a separator.
# my_list = ['Banana', 'Apple', 'Orange']
# joined_my_str = ' '.join(my_list)
# print(joined_my_str)  # output = Banana Apple Orange


# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.
# my_str = 'hello world'
# starts_with_hello = my_str.startswith('hello')
# print(starts_with_hello) # output = True


# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
# my_str = 'hello world'
# ends_with_world = my_str.endswith('world')
# print(ends_with_world) # output = True


# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
#my_str = 'hello world'
# ends_with_world = my_str.find('world')
# print(ends_with_world) # output = 6


# count(substring): Returns the number of times a substring appears in a string.
# my_str = 'hello world'
# o_count = my_str.count('l')
# print(o_count) # output = 3


# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
# my_str = 'hello world'
# capitalized_my_str = my_str.capitalize()
# print(capitalized_my_str) # output = Hello world


# isupper(): Returns True if all letters in the string are uppercase and False if not.
# my_str = 'hello world'
# is_all_upper = my_str.isupper()
# print(is_all_upper) # output = False

# my_str = 'HELLO WORLD'
# is_all_upper = my_str.isupper()
# print(is_all_upper) # output = True


# islower(): Returns True if all letters in the string are lowercase and False if not.
# my_str = 'hello world'
# is_all_lower = my_str.islower()
# print(is_all_lower) # output = True

# my_str = 'HELLO WORLD'
# is_all_lower = my_str.islower()
# print(is_all_lower) # output = False


# title(): Returns a new string with the first letter of each word capitalized.
# my_str = 'HELLO WORLD'
# title_case_my_str = my_str.title()
# print(title_case_my_str) # output = Hello World



line_1 = '------------------------------------------------------------------'
line_2 = '------------------------------------------------------------------'
print(line_1)
print(line_2)


#Employee Profile Generator = Exercise
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:]
print(last_three)
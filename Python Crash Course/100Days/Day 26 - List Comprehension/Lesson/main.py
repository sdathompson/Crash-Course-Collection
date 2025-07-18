double_num = [x * 2 for x in range(1,5)]

print(double_num)

# Conditional List Comprehension
# Only change the element if the test passes
# new_list = [new_item for item in list if test_passed]

names = ['Alex', 'Aang', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# Only adds names to the new list that are less than or equal to 4 characters long
short_names = [name for name in names if len(name) <= 4]
# Only adds name that are longer than 4 characters. Makes them all caps
all_caps_names = [name.upper() for name in names if len(name) >= 4]

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [str(x) for x in list_of_strings]
result = [x % 2 == 0 for x in numbers]
print(result)

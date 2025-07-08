string_list = input('Input the list of numbers separated by coma: ')

numbers = string_list.split(',')

max_number = 0

for number in numbers:
    cast_number = float(number)
    if cast_number > max_number:
        max_number = cast_number

print('The largest number is ', max_number)
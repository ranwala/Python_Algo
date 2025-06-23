def string_to_numbers(input_value):
    return [int(char.strip()) for char in input_value.split(",")]

def counter(numbers, target):
    # count = 0
    # numbers = string_to_numbers(input_string)
    # for number in numbers:
    #     if number == seeking_number:
    #         count = count + 1

    count = numbers.count(target)
    print(f"Then number {target} appears {count} in the list")

input_string = input("Enter a list of numbers separated by a comma: ")
seeking_number = int(input("Enter the number you want to count: "))
number_list = string_to_numbers(input_string)
counter(number_list, seeking_number)



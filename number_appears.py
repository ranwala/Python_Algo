input_string = input("Enter a list of numbers separated by a comma: ")
seeking_number = int(input("Enter the number you want to count: "))

def string_to_numbers(input_value):
    char_list = input_value.split(",")
    print(char_list)
    return [int(char) for char in char_list]

def counter():
    count = 0
    numbers = string_to_numbers(input_string)
    for number in numbers:
        if number == seeking_number:
            count = count + 1

    print(f"Then number {seeking_number} appears {count} in the list")

counter()



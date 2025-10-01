is_calculation_complete = False

def add(num1, num2): return num1 + num2

def sub(num1, num2): return num1 - num2

def mul(num1, num2): return num1 * num2

def div(num1, num2): return num1 / num2

def mod(num1, num2): return num1 % num2

def power(num1, num2): return num1 ** num2

def sqrt(num1): return num1 ** (1 / 2)

operations = {
    '1': ('+', add, 2),
    '2': ('-', sub, 2),
    '3': ('*', mul, 2),
    '4': ('/', div, 2),
    '5': ('%', mod, 2),
    '6': ('**', power, 2),
    '7': ('Square root', sqrt, 1),
}

print('Simple Calculator')
print('================')

content="""Choose an operation:
    1. Addition(+)
    2. Subtraction(-)
    3. Multiplication(*)
    4. Division(/)
    5. Modulus(%)
    6. Exponentiation(**)
    7. Square root(**)
    8. Exit
"""

while True:
    if is_calculation_complete:
        repeat = input('Do you want to perform another calculation? (y/n): ')
        if not repeat == 'y':
            print('Thank you for using the calculator.')
            is_calculation_complete = False
            break

    print(content)
    choice = input('Enter your choice(1-8): ')

    if choice == '8':
        print('Thank you for using the calculator.')
        break

    if choice not in operations:
        print('Invalid operation. Try again.')
        continue

    opp, func, args = operations[choice]

    try:
        if args == 1:
            num = float(input('Enter a number: '))
            result = func(num)
            print(f'The {opp} of {num}: {result}')
        else:
            number1 = float(input('Enter the number1: '))
            number2 = float(input('Enter the number2: '))
            result = func(number1, number2)
            print(f'Result {number1} {opp} {number2}: {result}')

        is_calculation_complete = True

    except ZeroDivisionError:
        print('Invalid Input.')
    except Exception as e:
        print(e)
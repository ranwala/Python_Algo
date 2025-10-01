is_calculation_complete = False

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def sqrt(num1):
    return num1 ** (1 / 2)

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
    else:
        if choice == '7':
            number1 = float(input('Enter first number: '))
        else:
            number1 = float(input('Enter first number: '))
            number2 = float(input('Enter second number: '))

    try:
        if choice == '1':
            result = add(number1, number2)
            print(f'Result: {number1} + {number2} = {result}')
            is_calculation_complete = True
        elif choice == '2':
            result = sub(number1, number2)
            print(f'Result: {number1} - {number2} = {result}')
            is_calculation_complete = True
        elif choice == '3':
            result = mul(number1, number2)
            print(f'Result: {number1} * {number2} = {result}')
            is_calculation_complete = True
        elif choice == '4':
            result = div(number1, number2)
            print(f'Result: {number1} / {number2} = {result}')
            is_calculation_complete = True
        elif choice == '5':
            result = mod(number1, number2)
            print(f'Result: {number1} % {number2} = {result}')
            is_calculation_complete = True
        elif choice == '6':
            result = power(number1, number2)
            print(f'Result: {number1} ** {number2} = {result}')
            is_calculation_complete = True
        elif choice == '7':
            result = sqrt(number1)
            print(f'Square root of: {number1} = {result}')
            is_calculation_complete = True
        else:
            print('Invalid choice.')

    except ZeroDivisionError:
        print('Invalid Input.')
    except Exception as e:
        print(e)
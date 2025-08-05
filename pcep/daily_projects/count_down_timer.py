import time

# is_valid_number = True
# message = ''
#
# try:
#     while is_valid_number:
#         number = int(input('Enter a number: '))
#
#         if number < 0:
#             print('Please enter a positive number')
#             continue
#         else:
#             message = input('Enter your final message: ')
#
#             for i in range(number, 0, -1):
#                 print(i)
#                 time.sleep(1)
#             break
#
#     print(f'{message.capitalize()}!')
# except ValueError:
#     print('Entered value is wrong!')

number = input('Please enter starting number: ')
message = input('Please enter the message: ')

if number.isdigit() and int(number) > 0:
    for i in range(int(number),0,-1):
        print(i)
        time.sleep(1)
    print(f'{message.capitalize()}!')
else:
    print('Enter a positive value.')
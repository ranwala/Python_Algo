# import time
#
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i, 'Mississippi')
#     time.sleep(5)
# print('Ready or not, here I come!')

largest_number = -999999
counter = 0

while True:
    number = int(input('Enter a number: '))

    if number == -1:
        continue
    print('hello')
    counter += 1
    if number > largest_number:
        largest_number = number
if counter != 0:
    print('The largest number is', largest_number)
else:
    print("You haven't entered any number")
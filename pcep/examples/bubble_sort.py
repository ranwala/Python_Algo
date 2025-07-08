numbers = []
swaped = True
list_length = int(input('Enter how many elements you need to sort: '))

for i in range(list_length):
    number = float(input('Enter a list element: '))
    numbers.append(number)

while swaped:
    swaped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            swaped = True
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

print(numbers)
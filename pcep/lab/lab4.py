number = int(input('Enter a number: '))

hypothesis = number
steps = 0

while hypothesis != 1:

    if hypothesis % 2 == 0:
        hypothesis = hypothesis / 2
        print('Even ', hypothesis)
    else:
        hypothesis = 3 * hypothesis + 1
        print('Odd ', hypothesis)

    steps += 1

print('Steps', steps)
number = int(input('Enter the grid size: '))

print(f'Multiplication table {number} x {number}')

for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{i * j:<4}', end='')
    print()
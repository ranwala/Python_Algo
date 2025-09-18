number = 5

for i in range(number):
    print(f"i={i}")
    print(" " * (number-i), end="")

    num = 1
    for j in range(i + 1):
        print(f"j={j}")
        print(num, end=' ')
        print(f'a={i-j} - b={j+1} - c={(i-j) // (j+1)}')
        num = num * (i-j) // (j+1)
        print(f'num= {num}')
    print()
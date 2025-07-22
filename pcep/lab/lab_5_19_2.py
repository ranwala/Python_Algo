def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

prime_numbers = []
not_prime_numbers = []

for i in range(100):
    if is_prime(i):
        prime_numbers.append(i)
    else:
        not_prime_numbers.append(i)

print(f'Prime numbers: {prime_numbers}')
print(f'Not prime numbers: {not_prime_numbers}')
def factorial(n):
    product = 1

    if n < 0:
        return None

    if n < 2:
        return 1

    return n * factorial(n-1)

    # for i in range(2, n + 1):
    #     product *= i
    # return product

print(factorial(5))
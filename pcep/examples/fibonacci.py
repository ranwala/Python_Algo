def fibonacci(n):
    if n < 1:
        return None

    if n < 3:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

    # item1 = item2 = 1
    # total = 0
    # for i in range(3, n + 1):
    #     total = item1 + item2
    #     item1, item2 = item2 , total
    #
    # return total

print(fibonacci(4))
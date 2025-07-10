import random

count = 0

weather = [[random.randint(0, 100) for h in range(24)] for d in range(31)]

for day in weather:
    if day[11] > 20.0:
        count += 1

print(count)

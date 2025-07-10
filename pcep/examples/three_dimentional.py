import random

vacancies = 0

information = [[[random.choice([True, False]) for r in range(20)] for f in range(15)] for h in range(3)]

for r in range(20):
    if information[2][14][r]:
        vacancies += 1

print(vacancies)
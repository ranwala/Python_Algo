# devisable_numbers = []

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         devisable_numbers.append(i)

devisable_numbers = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

print(f'Numbers from 1 to 100 devisable by 3 and 5 are: {devisable_numbers}')
print(f'Total count: {len(devisable_numbers)}')
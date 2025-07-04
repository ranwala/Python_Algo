number = int(input('Enter a number: '))

height = 0
count = 0
for i in range(1, number + 1):
    count += i
    if count > number:
        height = i - 1
        break
    # else: continue

print('Height = ', height)


# print('################################')
#
# number = int(input('Enter a number: '))
# h = 0
# inner = 1
#
# while inner <= number:
#     number -= inner
#     h += 1
#     inner += 1
#
# print(h)
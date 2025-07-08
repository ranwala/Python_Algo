start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))

numbers = [1,2,3,4,5,6,7,8,9,10]

# for number in numbers[start:end+1]:
#     total += number

# selected = [number for number in numbers if start <= number <= end + 1]
total = sum(numbers[start:end+1])

print(f'The sum of all numbers from {start} to {end} is: {total}')
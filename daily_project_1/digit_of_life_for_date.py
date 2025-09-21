birth_date = input('Enter your birth date(YYYYMMDD/YYYYDDMM/DDMMYYYY): ')

def sum_word(number):
    count = 0
    for ch in number:
        count += int(ch)

    return count

if not birth_date.isdigit():
    print('Please enter only numbers.')
else:
    total = sum_word(birth_date)

    while len(str(total)) > 1:
        total = sum_word(str(total))

    print(total)


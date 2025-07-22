school_class = {}

while True:
    name = input('Enter the student name: ')

    if name == '':
        break

    score = int(input('Enter the student\'s score (1-10): '))

    if score not in range(0,11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

    for value in school_class.keys():
        total_score = 0
        count = 0

        for score in school_class[value]:
            total_score += score
            count += 1

        print(f'{value.capitalize()} -> {total_score/count}')


import pandas as pd
import os

def get_grade(avg):
    if 75 <= avg <= 100:
        return 'A'
    elif 65 <= avg <= 74:
        return 'B'
    elif 55 <= avg <= 64:
        return 'C'
    elif 35 <= avg <= 54:
        return 'D'
    else:
        return 'F'

def average(scores_list):
    avg = sum(scores_list) / len(scores_list)

    grade = get_grade(avg)

    status = 'Pass' if avg >= 60 else 'Fail'

    return round(avg, 2), grade, status

def string_to_list_converter(scores_input):
    str_list = scores_input.split(',')
    try:
        numbers_list = [float(score) for score in str_list]

        validations = [0 <= score <= 100 for score in numbers_list]
        if False in validations:
            return None
        else:
            return numbers_list

    except ValueError:
        return None

def store(data):
    df = pd.DataFrame(data)

    if not os.path.exists('../files/daily_project/student_data.csv'):
        df.to_csv('../files/daily_project/student_data.csv', index=False)
    else:
        df.to_csv('../files/daily_project/student_data.csv', mode='a', header=False, index=False)


while True:
    student_name = input('Enter your name: ')
    score_input = input('Enter scores separated by coma: ')

    numbers = string_to_list_converter(score_input)
    if numbers is None:
        print('Invalid input: all scores must be a number and between 0 and 100')
        continue

    a, g, s = average(numbers)

    content = f"""
    Average: {a}
    Letter: {g}
    Result: {s}
    """

    print(content)

    data_dict = {
        'name': [student_name],
        'average': [a],
        'grade': [g],
        'status': [s]
    }

    store(data_dict)

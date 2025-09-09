from datetime import datetime

def ordinal(date):
    if 10 <= date % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1:'st', 2:'nd', 3:'rd'}.get(date % 10, 'th')

    return str(date) + suffix


time_format_input = input('Chose time format(12/24): ')

if time_format_input == '12' or time_format_input == '24':
    now = datetime.now()

    datetime_format = '%A, %B %d, %Y - %I:%M %p' if time_format_input == '12' else '%A, %B %d, %Y - %H:%M'

    print(f'Current Local Time (Verbose): {now.strftime(datetime_format)}')
    print(f'Current Local Time (ISO): {now.strftime('%Y-%m-%d %H:%M:%S')}')
    print(f'ISO Week Number: {now.isocalendar().week}')
    print(f'Day of Year: {now.timetuple().tm_yday}')
    print(f'Date with Ordinal: {now.strftime('%B')} {ordinal(now.day)}, {now.strftime('%Y')}')

else:
    print('Please enter correct time format.')
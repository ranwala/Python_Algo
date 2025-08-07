import pandas as pd
import os

name = input('Enter name: ')
phone_number = input('Enter phone number: ')
email = input('Enter email address: ')

if name and phone_number.isdigit() and email:
    data = {
        'Name': [name.capitalize()],
        'Phone': [phone_number],
        'Email': [email]
    }

    df = pd.DataFrame(data)

    if os.path.exists('../../contacts.csv'):
        df.to_csv('../../contacts.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('../../contacts.csv', index=False)

    view_contacts = input('View all contacts: (Yes/No)')

    if view_contacts.lower() == 'yes':
        read_df = pd.read_csv('../../contacts.csv')

        data_list = read_df.to_dict(orient='records')

        for item in data_list:
            for key, value in item.items():
                print(f'{key}: {value}')
            print()

    else:
        print('No permission to display saved data!')

else:
    print('Invalid input, please check!')
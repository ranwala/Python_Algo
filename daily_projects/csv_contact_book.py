import pandas as pd
import os

file_path = '../contacts.csv'

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

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', index=False, header=False)
    else:
        df.to_csv(file_path, index=False)

    view_contacts = input('View all contacts: (Yes/No)')

    if view_contacts.lower() == 'yes':
        read_df = pd.read_csv(file_path)

        data_list = read_df.to_dict(orient='records')

        for item in data_list:
            for key, value in item.items():
                print(f'{key}: {value}')
            print()

    else:
        print('No permission to display saved data!')

else:
    print('Invalid input, please check!')
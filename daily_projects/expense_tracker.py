import pandas as pd
import os
from datetime import datetime

FILE_PATH = '../files/daily_project/'

expenses = []

def add_expenses(description, amount):
    expenses.append({
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'description': description,
        'amount': round(amount, 2)
    })
    print('Added!')

def list_expenses():
    print('Expenses:')
    for index, row in enumerate(expenses):
        print(f'{index + 1}. {row['description']}-{row['amount']} ')

def total_expenses():
    all_expenses = [row['amount'] for row in expenses]
    total = sum(all_expenses)
    print(f'Total expense ${total}')

def export_to_csv(file_name):
    df = pd.DataFrame(expenses)

    if not os.path.exists(f'{FILE_PATH}{file_name}.csv'):
        df.to_csv(f'{FILE_PATH}{file_name}.csv', index=False)
    else:
        df.to_csv(f'{FILE_PATH}{file_name}.csv', index=False, mode='a', header=False)

    print(f'Exported to {file_name}.csv')

action_content = """
What would you like to do:
1. Add expense
2. List expenses
3. Export to CSV
4. Quit
"""
print(action_content, end='')

while True:
    try:
        choice = input('\nEnter choice: ').strip()

        if choice == '1':
            description_input = input('Description: ')
            amount_input = float(input('Amount: '))
            add_expenses(description_input, amount_input)

        elif choice == '2':
            if len(expenses) > 0:
                list_expenses()
            else:
                print('Please add some expenses to display')

        elif choice == '3':
            total_expenses()

        elif choice == '4':
            if len(expenses) > 0:
                file_name_input = input('Enter file name: ')
                export_to_csv(file_name_input)
            print('Please add some expenses to store')

        elif choice == '5':
            print('Good Bye!')
            break

    except ValueError:
        print('Please enter a valid amount.')
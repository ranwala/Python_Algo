balance = 0.0

def deposit(amount: float):
    global balance
    balance += amount
    print(f'Deposited ${amount}')

def withdraw(amount):
    global balance
    if amount > balance:
        print("You do not have enough balance.")
    else:
        balance -= amount
        print(f'Withdraw ${amount}')

def check_balance():
    global balance
    print(f'Your balance is: ${balance}')


print('Welcome To Simple Bank Simulator!')
check_balance()

action_content = """
Choose an action:
1. Deposit
2. Withdraw
3. Check Balance
4. Quit
"""
print(action_content)

while True:
    choice = input("\nEnter Choice: ").strip()

    try:
        if choice == '1':
            amount_to_deposit = float(input('Enter the deposit amount: ').strip())
            if amount_to_deposit < 0:
                raise ValueError
            else:
                deposit(amount_to_deposit)

        elif choice == '2':
            amount_to_withdraw = float(input('Enter the withdraw amount: ').strip())
            if amount_to_withdraw < 0:
                raise ValueError
            else:
                withdraw(amount_to_withdraw)

        elif choice == '3':
            print(check_balance())

        elif choice == '4':
            print('Thank you for using the bank simulator'.title())
            break

        else:
            print('Please enter a valid choice')
            continue

    except ValueError:
        print('Please enter a valid amount: ')
        continue
income = float(input('Enter your income: '))

tax = None
if income < 0:
    tax = 0
elif income < 85528:
    tax = income * 0.18 - 556.2
else:
    surplus = income - 85528
    tax = surplus * 0.32 + 14839.2

tax = round(tax, 0)
print(f'Your income tax is {tax}')
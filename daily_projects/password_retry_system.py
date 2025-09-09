count = 0
max_attempts = 3

while count < max_attempts:
    password = input('Enter password: ')

    if password == 'python123':
        print('Access Granted!')
        break

    count += 1

    if count == 3:
        print('Too many attempts. You are locked out.')
        break
    else:
        print('Invalid Password. Retry.')
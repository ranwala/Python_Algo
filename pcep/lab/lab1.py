secret_exit = 'chupacabra'

while True:
    password = input('Enter the password: ')
    
    if password == secret_exit:
        break
print('You have successfully left the loop.')
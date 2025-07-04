user_input = int(input('Guess the secret number: '))

secret_number = 8
while user_input != secret_number:
    print('Haha You are stuck in my loop!')
    user_input = int(input('Guess the secret number: '))
print('Wel done, muggle! you are free now.')
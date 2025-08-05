quote = input('What is your quote: ')

if quote:
    with open('../../files/quote.txt', 'w') as file:
        file.write(quote)

    with open('../../files/quote.txt', 'r') as file:
        result = file.read()
        print(f'Saved and loaded quote: {result}')
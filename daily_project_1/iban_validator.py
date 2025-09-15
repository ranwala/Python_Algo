# mostly works for german iban
iban = input('Enter IBAN: ')

# Remove spaces
iban = iban.replace(" ", "")

# Chack whether user has entered all characters and numbers
if not iban.isalnum():
    print('Please enter a valid IBAN.')
# Check the length
elif len(iban) < 15:
    print('Entered IBAN is too short.')
elif len(iban) > 30:
    print('Entered IBAN is too long.')
else:
    # Move first for characters to end
    iban = iban[4:] + iban[:4]

    iban2 = ''
    # Replace letter D with 13 and letter E with 14
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch.upper()) - ord('A'))

    # Validate by chacking the mod value
    validate = int(iban2) % 97 == 1
    if validate:
        print('Entered IBAN is valid.')
    else:
        print('Entered IBAN is invalid.')
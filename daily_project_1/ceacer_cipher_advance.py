text = input('Enter a text: ')
shift_value = input('Enter the shift value: ')

cipher = ''

if not shift_value.isdigit():
    shift_value = input('Enter the shift value: ')
else:
    shift_value = int(shift_value)

    for ch in text:
        if not ch.isalpha():
            cipher += ch
        else:
            code = ord(ch) + shift_value
            last_ch = 'Z' if ch.isupper() else 'z'
            first_ch = 'A' if ch.isupper() else 'a'

            if code > ord(last_ch):
                code_dif = ord(last_ch) - ord(ch)
                balance = shift_value - code_dif

                code = ord(first_ch) + (balance - 1)
            cipher += chr(code)

print(cipher)
# abcxyzABCxyz 123 => 2
# cdezabCDEzab 123

# The die is cast => 25
# Sgd chd hr bzrs
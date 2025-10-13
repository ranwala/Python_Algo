import random
import string


def get_lower_character():
    while True:
        letter = random.choice(string.ascii_lowercase)
        if letter == 'l' or letter == 'o':
            continue
        return letter


def get_upper_character():
    while True:
        letter = random.choice(string.ascii_uppercase)
        if letter == 'O':
            continue
        return letter


def get_number():
    while True:
        letter = random.choice(string.digits)
        if letter == '0':
            continue
        return letter


def get_special_character():
    return random.choice('@#$%&*!?')


def main():
    try:
        password = ''
        print('=== Password Generator ===')

        pass_len = int(input('Enter password length (minimum 8)?: '))
        if pass_len < 8:
            print('Password length must be minimum 8.')
            return

        include_lower = input('Include lower case letter (y/n)?: ').lower()
        include_upper = input('Include upper case letter (y/n)?: ').lower()
        include_number = input('Include number (y/n)?: ').lower()
        include_special_character = input('Include special charactor (y/n)?: ').lower()

        actions = {
            'upper': {'include': include_upper, 'action': get_upper_character},
            'number': {'include': include_number, 'action': get_number},
            'lower': {'include': include_lower, 'action': get_lower_character},
            'special': {'include': include_special_character, 'action': get_special_character}
        }

        while len(password) < pass_len:
            for data in actions.values():
                if data['include'] == 'y':
                    password += data['action']()
                    if len(password) == pass_len:
                        break


        # while True:
        #     if include_upper == 'y':
        #         password += get_upper_charactor()
        #         if len(password) == pass_len: break
        #     if include_number == 'y':
        #         password += get_number()
        #         if len(password) == pass_len: break
        #     if include_lower == 'y':
        #         password += get_lower_charactor()
        #         if len(password) == pass_len: break
        #     if include_special_charactor == 'y':
        #         password += get_special_charactor()
        #         if len(password) == pass_len: break

        print(f'Generated password: {password}')

    except ValueError as e:
        print(f'Value Error. {e}')
    except Exception as e:
        print(f'Something went wrong {e}')


if __name__ == '__main__':
    main()



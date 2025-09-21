text = input('Enter a text: ')
reversed_text = ''
true_list = []

text = text.replace(' ', '').lower()

# Shorten code
if text == '':
    print('Please enter a valid text.')
else:
    if text == text[::-1]:
        print("It's a palindrome")
    else:
        print("It is not a palindrome")


# My code
if text == '':
    print('Please enter a valid text.')
else:
    for i in range((len(text) - 1), 0, -1):
        reversed_text += text[i]

    for i in range(0, len(text) -1):
        if text[i].lower() == reversed_text[i].lower():
            true_list.append(True)
        else: true_list.append(False)

if all(true_list):
    print("It's a palindrome")
else:
    print("It is not a palindrome")

# Ten animals I slam in a net
# Eleven animals I slam in a net
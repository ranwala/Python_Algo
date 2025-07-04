word = input('Enter a word: ')

word_without_vowels = ''

for letter in word.upper():
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else: word_without_vowels += letter

print(word_without_vowels)
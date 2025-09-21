word1 = input('Enter a word: ')
word2 = input('Enter the second word: ')

true_list = []

word1 = word1.replace(' ', '').lower()
word2 = word2.replace(' ', '').lower()

if len(word1) == len(word2):

    freq1 = {}
    freq2 = {}

    for ch in word1:
        freq1[ch] = word1.count(ch)

    for ch in word2:
        freq2[ch] = word2.count(ch)

    if freq1 == freq2:
        print('Anagrams')
    else:
        print('Not Anagrams')
else:
    print('Not Anagrams')

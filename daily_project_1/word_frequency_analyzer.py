import string
import textwrap

from PCAP.oop_stack import AddingStack

clean_text = ''
total_words = 0
word_dict = {}

def get_common_words():
    for key, value in word_dict.items():
        if value['freq'] > 1:
            print(f'{key}: {value['freq']} times ({round((value['freq'] / total_words) * 100, 2)}%)')

print(string.__dict__)

input_text = input("Enter some text: ")

# Remove punctuations from the text
for char in input_text.lower():
    if char in string.punctuation:
        continue

    clean_text += char

# Generate unique dictionary
for word in clean_text.split(" "):
    if word in word_dict:
        word_dict[word]['freq'] += 1
    else:
        word_dict[word] = {'freq': 1, 'len': len(word)}


total_words = sum(value['freq'] for value in word_dict.values())

word_length_avg = sum(value['len'] for value in word_dict.values()) / len(word_dict)

sorted_word_dict = sorted(word_dict.items(), key=lambda item:item[1]['len'], reverse=True)

longest_word, longest_word_length = sorted_word_dict[0]
smallest_word, smallest_word_length = sorted_word_dict[-1]

content = f"""
=== Word Frequency Analysis ===
Total words: {total_words}
Unique words: {len(word_dict.keys())}
Average word length: {word_length_avg}

Top 5 most common words:
"""

print(textwrap.dedent(content))

get_common_words()

print(f'\nLongest word: {longest_word} ({longest_word_length['len']} letters)')
print(f'Longest word: {smallest_word} ({smallest_word_length['len']} letters)')
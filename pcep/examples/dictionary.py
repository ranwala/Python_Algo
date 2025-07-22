dic = {'dog':'I am a dog', 'horse':'I am a horse', 'cat': 'I am a cat'}
words = ['cat', 'lion', 'dog']

for word in words:
    if word in dic:
        print(f'{word} -> {dic[word]}')
    else:
        print(f'{word} can\'t find')


# Key method
print('############################Key#############################')
print(dic.keys())
for key in dic.keys():
    print(dic[key])

# Items method
print('############################Items#############################')
print(dic.items())
for key, value in dic.items():
    print(f'{key} -> {value}')

# Modify
print('############################Modify#############################')
dic['cat'] = 'This has been changed'
print(dic)

# Sort
print('############################Sort#############################')
for key, value in sorted(dic.items()):
    print(f'{key} -> {value}')

# Values method
print('############################Values#############################')
for value in dic.values():
    print(value)

# Add new Key
print('############################Add#############################')
dic['rabbit'] = 'I am a rabbit'

dic.update({'lion': 'I am a lion'})
print(dic)

# Remove item
print('############################Remove#############################')
del dic['cat']
print(dic)

# PopItem
print('############################PopItem#############################')
dic.popitem()
print(dic)
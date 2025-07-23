dic = {
    'a': '1',
    'b': '2',
    'c': '1',
    'd': '3',
    'e': '2',
    'f': '4',
    'g': '1',
}

# unique_dic = {}
#
# for key, value in dic.items():
#     if value in unique_dic.values():
#         continue
#     else:
#         unique_dic.update({key: value})

seen_values = set()
unique_dic = {}

for key, value in dic.items():
    if value not in seen_values:
        unique_dic[key] = value
        seen_values.add(value)

print(unique_dic)
print(len(unique_dic))
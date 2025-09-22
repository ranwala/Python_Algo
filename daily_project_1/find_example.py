def pos(sub_string, string):
    result = ''
    start = 0
    for ch in sub_string:
        index = string.find(ch, start)
        if index != -1:
            result += ch
            start = index + 1
        else:
            return False

    return sub_string == result

response = pos('donor', 'Nabucodonosor')

print('Yes' if response else 'No')
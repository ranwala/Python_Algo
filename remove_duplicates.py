def string_to_array_converter(lst):
    return [item.strip() for item in lst.split(',')]

def remove_duplicates(data_list):
    unique_list = []
    duplicates = []

    for item in data_list:
        if item in unique_list:
            duplicates.append(item)
        else:
            unique_list.append(item)

    return unique_list, len(duplicates)

new_list = input("Enter a list separated by a comma: ")
data = string_to_array_converter(new_list)
u, d = remove_duplicates(data)

print(u)
print(f"Removed duplicates: {d}")

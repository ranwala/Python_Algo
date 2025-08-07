from pathlib import Path
""" Used to generate txt files """
# folder_dict = {
#     'students': {
#         'math': {
#             'chandu.txt': "Chandu's maths notes here",
#             'malinga.txt': "Malinga's maths notes here",
#             'ranwala.txt': "Ranwala's maths notes here",
#             'methuja.txt': "Methuja's maths notes here",
#             'thiveith.txt': "Thiveith's maths notes here",
#         },
#         'science': {
#             'chandu.txt': "Chandu's science notes here",
#             'malinga.txt': "Malinga's science notes here",
#             'ranwala.txt': "Ranwala's science notes here",
#             'methuja.txt': "Methuja's science notes here",
#             'thiveith.txt': "Thiveith's science notes here",
#         },
#     }
# }
#
# for key1, values1 in folder_dict.items():
#     for key2, values2 in values1.items():
#         for key3, value3 in values2.items():
#             with open(f'../../files/{key1}/{key2}/{key3}', 'w') as file:
#                 file.write(value3)
#
# print('Folders are created!')

# {
#   "math": {
#     "alice.txt": "Alice's math notes here",
#     "bob.txt": "Bob's math notes here"
#   },
#   "science": {
#     "alice.txt": "Alice's science notes here"
#   }
# }

students = {}

main_path = Path('/Users/chanduranwala/sample-projects/python_projects/algorithems/files')

folders = main_path.rglob('*')

for file_path in folders:
    if file_path.is_file() and file_path.suffix.lower() in ['.txt']:
        subject = file_path.parent.name
        file = file_path.name
        content = file_path.read_text()

        # Initialize nested dict if subject not in students
        if subject not in students:
            students[subject] = {}

        # Now safely update
        students[subject][file] = content

print(students)


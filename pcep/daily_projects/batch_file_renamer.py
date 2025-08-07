import os

file_path = '../../files/students/math'

file_name = input('Enter file name: ')

files = os.listdir(file_path)

for index, file in enumerate(files):
    _, extension = os.path.splitext(file)
    os.rename(f'{file_path}/{file}', f'{file_path}/{file_name}{index + 1}{extension}')
import os

def generate_file_names_list(names: str):
    return names.split(',')

def is_file_exist(file_name: str):
    return os.path.exists(f'files/{file_name}.txt')

def get_text(name: str):
    if is_file_exist(name):
        with open(f'files/{name}.txt', 'r') as file:
            return file.readline()
    else:
        return None


def get_words_count(text: str):
    words = text.split(" ")
    return len(words)


def main():
    try:
        file_names = input('Enter file names by comma separated eg:(file1,file2): ')

        file_names_list = generate_file_names_list(file_names)

        for file_name in file_names_list:
            content = get_text(file_name)

            if content is None:
                print('There is no file to read text')
            else:
                number_of_words = get_words_count(content)
                os.rename(f'files/{file_name}.txt', f'files/{file_name}_{number_of_words}.txt')
                print(f'{file_name} changed to {file_name}_{number_of_words}')

    except FileNotFoundError as e:
        print(f'File not found {e}')
    except Exception as e:
        print(f'Something went wrong {e}')


if __name__ == '__main__':
    main()
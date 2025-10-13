import os

FILE_PATH = 'files'

def read_text(file_name: str):
    with open(f'{FILE_PATH}/{file_name}', 'r') as file:
        return file.readline()


def write_text(content: str):
    with open(f'{FILE_PATH}/merge.txt', 'a') as file:
        file.writelines(content)


def main():
    try:
        files = [file_name for file_name in os.listdir(FILE_PATH) if file_name.endswith('.txt')]

        for file_name in files:
            text = read_text(file_name)
            write_text(f'{text}\n')

        print('Successfully merged')
    except FileNotFoundError as e:
        print(f'File not found error. {e}')
    except Exception as e:
        print(f'Something went wrong. {e}')


if __name__ == '__main__':
    main()




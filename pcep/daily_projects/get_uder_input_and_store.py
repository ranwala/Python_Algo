while True:
    note = input('What do you need to write: ')

    if note.lower() == 'exit':
        break

    with open('../../files/notes.txt', 'a') as file:
        file.write(f'{note} \n')
sample_list = [1,2,3,4,5,6,7,8,9]

metrix = [
    [2,9,5,7,4,3,8,6,1],
    [4,3,1,8,6,5,9,2,7],
    [8,7,6,1,9,2,5,4,3],
    [3,8,7,4,5,9,2,1,6],
    [6,1,2,3,8,7,4,9,5],
    [5,4,9,2,1,6,7,3,8],
    [7,6,3,5,2,4,1,8,9],
    [9,2,8,6,7,1,3,5,4],
    [1,5,4,9,3,8,6,7,2]
]

sub_metrix = []

response = ''

def check_row(row):
    sorted_list = sorted(row)
    if sorted_list == sample_list:
        return True
    else:
        return False

# def generate_sub_matrix(original_metrix):
    


for row in metrix:
    result = check_row(row)
    if not result:
        response = 'No'
        break
    else:
        response = 'Yes'

columns = [[row[col] for row in metrix] for col in range(len(metrix[0]))]

for col in columns:
    result = check_row(col)
    if not result:
        response = 'No'
        break
    else:
        response = 'Yes'

print(response)
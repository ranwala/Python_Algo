days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time_blocks = ['Morning', 'Afternoon', 'Evening']

schedule = {}

for day in days:
    schedule[day] = {}
    for time_block in time_blocks:
        task_input = input(f'Enter your task for {day} - {time_block}: ')
        schedule[day][time_block] = task_input

# Calculate col widths
col_widths = {'Day': max(len('Day'), max(len(d) for d in days))}

for tb in time_blocks:
    col_widths[tb] = max(len(tb), max(len(d) for d in days))

print(col_widths)

def make_row(values):
    return ('|' + '|'.join(f"{val.center(col_widths[col_width] + 1)} " for val, col_width in zip(values, col_widths))
            + '|')

headers = ['Day'] + time_blocks
line = '+' + '+'.join('-' * (col_widths[h] + 2)  for h in headers) + '+'

print(line)
print(make_row(headers))
print(line)

# Print content
for day in days:
    row = [day] + [schedule[day][time_block] for time_block in time_blocks]
    print(make_row(row))

print(line)

# print('Your weekly schedule')
# header = """
# +-----------+-----------+-----------+-----------+
# | Day       | Morning   | Afternoon | Evening   |
# +-----------+-----------+-----------+-----------+
# """
#
# print(header.strip())
#
# for day, time_block_dict in schedule.items():
#     print(f'|{day.center(11, ' ')}', end='|')
#     for time_block in time_block_dict.values():
#         print(f'{time_block.center(11, ' ')}', end='|')
#     print()
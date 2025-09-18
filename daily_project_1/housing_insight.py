import pandas as pd

FILE_PATH = "files/california_housing_test.csv"
total_median_income = 0
total_median_house_value = 0
total_population = 0
group = {}

df = pd.read_csv(FILE_PATH)

housing_dict = df.to_dict(orient='records')
NUMBER_OF_ROWS = len(housing_dict)

def group_by_median_age():
    for row in housing_dict:
        median_age = row['housing_median_age']
        if median_age not in group:
            group[median_age] = []
        group[median_age].append(row)

    for median_age, group_items in group.items():
        print(f'Housing Median Age: {median_age}')

        avg_house_value = get_avg_house_value_per_age(group_items)
        print(f'Average House Value per Age: {avg_house_value}')
        print()


def get_avg_house_value_per_age(grouped_item_dict):
    total = 0
    for row_item in grouped_item_dict:
        total += row_item['median_house_value']

    avg = total / len(grouped_item_dict)
    return round(avg, 2)


def filter_by_income():
    income_group = {}
    income_input = float(input("Please enter your income: "))

    print(f'Minimum Income: {income_input}')

    for row in housing_dict:
        house_value = row['median_house_value']
        if house_value <= income_input:
            if house_value not in income_group:
                income_group[house_value] = []
            income_group[house_value].append(row)

    print('Houses in your income grange')
    for house_value, group in income_group.items():
        print(f'House Value: {house_value}')

        for row in group:
            print(f'Total Rooms: {row["total_rooms"]}', end=' ')
            print(f'Total Bedrooms: {row["total_bedrooms"]}')

        print()


for row in housing_dict:
    total_median_income += row['median_income']
    total_median_house_value += row['median_house_value']

    if row['median_income'] > 6:
        total_population += row['population']


# By using a list
all_income = [row['median_income'] for row in housing_dict]
max_income = max(all_income)
max_income_index = next((i for i, row in enumerate(housing_dict) if row['median_income'] == max_income), -1)

# By using a data frame
max_value = df['median_income'].max()
max_index = df['median_income'].idxmax()

content = f"""
Loaded {NUMBER_OF_ROWS} rows.
Average Median Income: {round(total_median_income/NUMBER_OF_ROWS, 2)}
Average Median House Value: ${round(total_median_house_value/NUMBER_OF_ROWS, 2)}
Highest Income(Optional): {max_income} (Row {max_income_index})
Highest Income: {max_value} (Row {max_index})
Total population (income > 6): {total_population}
"""

print(content)

# Group by
# group_by_median_age()

filter_by_income()

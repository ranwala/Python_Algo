import pandas as pd

FILE_PATH = "files/california_housing_test.csv"
total_median_income = 0
total_median_house_value = 0
total_population = 0

df = pd.read_csv(FILE_PATH)

housing_dict = df.to_dict(orient='records')
NUMBER_OF_ROWS = len(housing_dict)

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

print(content.strip())

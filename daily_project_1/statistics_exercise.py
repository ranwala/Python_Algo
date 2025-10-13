import textwrap

def generate_string_to_number(numbers: str):
    return [float(number) for number in numbers.split(',')]


def calculate_variance(numbers: list[float]):
    mean = sum(numbers) / len(numbers)

    squared_differences = [(number - mean) ** 2 for number in numbers]

    variance = sum(squared_differences) / (len(squared_differences) - 1)
    return variance

def main():
    try:
        input_numbers = input('Enter a list of numbers (comma separated): ')

        number_list = generate_string_to_number(input_numbers)

        variance = calculate_variance(number_list)

        standard_deviation = variance ** (1/2)

        content = f"""
        Number Statistics Report
        ------------------------
        Count: {len(number_list)}
        Min: {min(number_list)}
        Max: {max(number_list)}
        Average: {sum(number_list) / len(number_list)}
        Variance: {round(variance, 2)}
        Standard Deviation: {round(standard_deviation, 2)}
        """

        print(textwrap.dedent(content))

    except ValueError as e:
        print(f'Value error {e}')
    except ZeroDivisionError as e:
        print(f'Zero division error {e}')


if __name__ == '__main__':
    main()
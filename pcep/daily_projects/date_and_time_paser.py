from datetime import datetime
from dateutil.relativedelta import relativedelta

FORMAT_LIST = ['%Y-%m-%d %H:%M', '%d/%m/%Y %H:%M', '%b %d, %Y %H:%M']

# Validate input date and return the type of datetime
def validate_datetime(date_time, time):
    for fmt in FORMAT_LIST:
        try:
            # parse string to datetime
            converted_datetime = datetime.strptime(f"{date_time} {time}", fmt)

            # Check the format
            valid_datetime = converted_datetime.strftime(f'{fmt} {time}')

            if valid_datetime:
                return converted_datetime

        except ValueError:
            continue
    return None

# Check the current year with the user provided year
# If user provided year is less than the current year
# Date calculate for one year ahead to current year
# Return type datetime
def calculate_expected_year(date_time, current_datetime):
    if date_time < current_datetime:
        year_to_add = current_datetime.year - date_time.year + 1
        return date_time + relativedelta(years=year_to_add)
    else: return date_time

# Calculate the remaining time
def remaining_datetime(date_time, current_datetime):
    time_remaining = date_time - current_datetime
    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds // 60) % 60
    seconds = time_remaining.seconds % 60

    return days, hours, minutes, seconds


input_date = input("Enter your target date (eg., 2025-08-12, 12/08/2025 or Aug 12, 2025): ")
input_time = input("(Optional) Enter the time of the day (eg., 14:30) or press enter to skip: ")

converted_dt = validate_datetime(input_date, input_time or '00:00')

if converted_dt is not None:
    now = datetime.now()
    expected_year = calculate_expected_year(converted_dt, now)
    d, h, m, s = remaining_datetime(expected_year, now)

    # Print the target date
    dt = datetime.strftime(expected_year, '%A, %B %d, %Y')
    t = datetime.strftime(expected_year, '%H:%M')
    print(f"Target: {dt} at {t}")

    # Check the date is weekend
    is_weekend = 'Yes' if expected_year.weekday() in [5, 6] else 'No'
    print(f"Weekend: {is_weekend}")

    print(f"Time remaining: {d} days, "
          f"{h} hours, "
          f"{m}, minutes, "
          f"{s} seconds")

else:
    print("""
    Couldn't parse that. Try format like.
    - 2025-08-12
    - 12/08/2025
    - Aug 12, 2025""")
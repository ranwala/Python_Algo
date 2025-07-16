def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_of_month(year, month):
    if month == 2:
        if leap_year(year):
            return 29
        else: return 28
    else:
        if month in [1,3,5,7,8,9,10,12]:
            return 31
        else:
            return 30


test_years = [1900, 2000, 2024, 1987]
test_months = [2, 2, 11, 12]
test_days = [28, 29, 30, 31]

for i in range(len(test_years)):
    yr = test_years[i]
    mn = test_months[i]
    result = days_of_month(yr, mn)

    if result == test_days[i]:
        print(f"{yr} month {mn} has {result} days")
    else:
        print('Somthing went wrong')
class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.__days = {
            1: 'Mon',
            2: 'Tue',
            3: 'Wed',
            4: 'Thu',
            5: 'Fri',
            6: 'Sat',
            7: 'Sun'
        }
        if day.title() not in self.__days.values():
            raise WeekDayError()

        self.__day = day.title()


    def __str__(self):
        return f'{self.__day}'

    def add_days(self, n):
        number = n % 7
        current_day_key = next((k for k, v in self.__days.items() if v == self.__day), None)
        current_day_key = (current_day_key + number - 1) % 7 + 1
        self.__day = self.__days.get(current_day_key)

    def subtract_days(self, n):
        number = n % 7
        current_day_key = next((k for k, v in self.__days.items() if v == self.__day), None)
        current_day_key = (current_day_key - number - 1) % 7 + 1

        self.__day = self.__days.get(current_day_key)


try:
    weekday = Weeker('sun')
    print(weekday)
    weekday.add_days(10)
    print(weekday)
    weekday.subtract_days(2)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

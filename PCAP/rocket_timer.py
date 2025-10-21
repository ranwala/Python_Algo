def format_time(h, m, s):
    return f'{h:02d}:{m:02d}:{s:02d}'

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def __str__(self):
        return format_time(self.__hours, self.__minutes, self.__seconds)


    def next_second(self):
        self.__seconds = (self.__seconds + 1) % 60

        if self.__seconds == 0:
            self.__minutes = (self.__minutes + 1) % 60

            if self.__hours == 0:
                self.__hours = (self.__hours + 1) % 24


        # Old Logic
        # if self.__seconds == 60:
        #     self.__seconds = 0
        #     self.__minutes += 1
        #
        #     if self.__minutes == 60:
        #         self.__minutes = 0
        #         self.__hours += 1
        #
        #         if self.__hours == 24:
        #             self.__hours = 0
        #             self.__minutes = 0
        #             self.__seconds = 0


    def prev_second(self):
        self.__seconds = (self.__seconds - 1) % 60

        if self.__seconds == 59:
            self.__minutes = (self.__minutes - 1) % 60

            if self.__hours == 59:
                self.__hours = (self.__hours - 1) % 24

        # Old Logic
        # if self.__seconds == 0:
        #     self.__seconds = 59
        #
        #     if self.__minutes == 0:
        #         self.__minutes = 59
        #
        #         if self.__hours == 0:
        #             self.__hours = 23
        #         else:
        #             self.__hours -= 1
        #
        #     else:
        #         self.__minutes -= 1
        #
        # else:
        #     self.__seconds -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            print('Please enter a number between 1 and 100.')
        else:
            self.grades.append(grade)
            print('Grades added')

    def average(self):
        try:
            return round(sum(self.grades) / len(self.grades), 2)
        except ZeroDivisionError:
            return 0

    def status(self):
        avg = self.average()
        if avg > 60:
            print('Pass')
        else:
            print('Fail')

    def __str__(self):
        return f'Student {self.name}, Average grade: {self.average()}'

if __name__ == '__main__':
    student = Student('Chandu')
    student.add_grade(95)
    student.add_grade(80)
    student.add_grade(85)
    print()

    print(f'Average grade: {student.average()}')
    print()

    student.status()
    print()

    print(student)
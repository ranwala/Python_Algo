import pandas as pd
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f'Added {grade} to student {self.name}')

    def calculate_average(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def get_grade_letter(self):
        avg = self.calculate_average()
        if 75 <= avg <= 100:
            return 'A'
        elif avg >= 65:
            return 'B'
        elif avg >= 55:
            return 'C'
        elif avg >= 35:
            return 'D'
        else:
            return 'F'


    def display(self):
        content = f"""
        Student: {self.name}
        Grades: {[grade for grade in self.grades]}
        Average: {self.calculate_average()}
        Letter Grade: {self.get_grade_letter()}
        Total Assignments: {len(self.grades)}
        Highest Grade: {max(self.grades)}
        Lowest Grade: {min(self.grades)}
        """

        print(content)

    def save(self):
        data_dict = {
            'name': [self.name],
            'grades': [self.grades],
            'avg': [self.calculate_average()],
            'letter_grade': [self.get_grade_letter()],
            'highest_grade': [max(self.grades)],
            'lowest_grade': [min(self.grades)],
        }

        df = pd.DataFrame(data_dict)
        if not os.path.exists('files/grade_tracker_data.csv'):
            df.to_csv('files/grade_tracker_data.csv', index=False)
        else:
            df.to_csv('files/grade_tracker_data.csv', mode='a', header=False, index=False)

        print('Data saved to file')

print('===== Student Grade Tracker =====')

student1 = Student('Chandu Ranwla')

# Add grades
student1.add_grade(95)
student1.add_grade(80)
student1.add_grade(70)
student1.add_grade(60)

student1.display()
student1.save()

# Second student
student2 = Student('Methuja Ranwala')
student2.add_grade(80)
student2.add_grade(70)
student2.display()
student2.save()


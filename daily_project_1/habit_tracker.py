import pandas as pd
import os

class Store:
    @staticmethod
    def save(habits):
        data = []
        for habit in habits:
            data.append({
                'name': habit.name,
                'streak': habit.streak,
            })

        df = pd.DataFrame(data)
        if not os.path.exists('files/habits.csv'):
            df.to_csv('files/habits.csv', index=False)
        else:
            df.to_csv('files/habits.csv',header=False, mode='a', index=False)

        print('Data saved to files')

    @staticmethod
    def update(habit):
        df = pd.read_csv('files/habits.csv')
        df.loc[df['name'] == habit.name, 'streak'] = habit.streak
        df.to_csv('files/habits.csv', index=False)

        print('Data updated')


class Habit:
    def __init__(self, name, streak, last_done):
        self.name = name
        self.streak = streak
        self.last_done = last_done


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)
        print("Added a new habit.")

    def mark_done(self, habit):
        if habit in self.habits:
            habit.streak += 1

        print('Marked the habit.')

        # Update date in csv file
        Store.update(habit)

    def get_streak(self):
        for habit in self.habits:
            print(f'{habit.name} - Streak: {habit.streak}')

habit_tracker = HabitTracker()

habit_tracker.add_habit(Habit('Run', 0, False))
habit_tracker.add_habit(Habit('Learn Deutsch', 0, False))
habit_tracker.add_habit(Habit('Learn Python', 0, False))
habit_tracker.add_habit(Habit('Drink Water', 0, False))
print()

# Save dato to csv file
Store.save(habit_tracker.habits)
print()

habit_tracker.get_streak()
print()

habit_tracker.mark_done(habit_tracker.habits[1])
print()

habit_tracker.get_streak()
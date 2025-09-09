from datetime import datetime, timedelta
import pandas as pd
import os

FILE_PATH = '../files/daily_project/stopwatch_sessions.csv'

# Globals
start_time = None
pause_time = None
lap_count = 0
laps = {}

def store(data_dict):
    df = pd.DataFrame(data_dict)

    if not os.path.exists(FILE_PATH):
        df.to_csv('../files/daily_project/stopwatch_sessions.csv', index=False)
    else:
        df.to_csv('../files/daily_project/stopwatch_sessions.csv', mode='a', header=False, index=False)

def time_converter(time_difference: timedelta):
    total_seconds = time_difference.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) / 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 100)

    time_diff = f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}'
    return time_diff


while True:
    command = input("Command (start/lap/pause/resume/stop/restart/quit): ").strip().lower()

    if command == 'start':
        start_time = datetime.now()
        print(f'Started at {start_time.strftime('%H:%M:%S')}')

    elif command == 'lap':
        if start_time is None:
            print("Stopwatch has not start yet.")
            continue

        lap_count += 1
        now = datetime.now()
        total_time_duration = now - start_time if pause_time is None else pause_time - start_time
        lap_time_duration = total_time_duration if lap_count == 1 \
            else total_time_duration - sum(laps.values(), timedelta())

        laps[f'Lap {lap_count}'] = lap_time_duration
        print(f'Lap {lap_count} - {time_converter(lap_time_duration)} (Total: {time_converter(total_time_duration)})')

    elif command == 'pause':
        if pause_time is None:
            pause_time = datetime.now()
            print(f'Pause at {time_converter(pause_time - start_time)}')
        else:
            print("Already paused")

    elif command == 'resume':
        if pause_time is not None:
            pause_duration = datetime.now() - pause_time
            start_time = start_time + pause_duration
            pause_time = None
            print('Resumed.')
        else:
            print("Stopwatch has not paused")

    elif command == 'stop':
        if start_time is None:
            print("Stopwatch has not start yet.")
            continue

        end_time = pause_time if pause_time else datetime.now()
        total_duration = end_time - start_time

        fastest = min(laps, key=laps.get)
        slowest = max(laps, key=laps.get)
        average = sum(laps.values(), timedelta()) / len(laps)

        content = f"""
        Summery
        -------
        
        Total Time: {time_converter(total_duration)}
        Laps: {lap_count}
        Fastest Lap: {time_converter(laps[fastest])} ({fastest})
        Slowest Lap: {time_converter(laps[slowest])} ({slowest})
        Average Lap: {time_converter(average)}
        """

        print(content)

        data = {
            'date': [start_time.strftime('%Y-%m-%d')],
            'start_time': [start_time.strftime('%H:%M:%S')],
            'total_duration': [time_converter(total_duration)],
            'laps': [lap_count],
            'fastest': [time_converter(laps[fastest])],
            'slowest': [time_converter(laps[slowest])],
            'average': [time_converter(average)]
        }

        store(data)
        break

    elif command == "reset":
        start_time = None
        paused_time = None
        lap_count = 0
        laps = []
        print("Stopwatch reset.")

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print('Please enter valid command...')


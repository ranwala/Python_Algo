from datetime import datetime, timedelta
import pandas as pd
import os

FILE_PATH = '../files/daily_project/stopwatch_sessions.csv'
datetime_start = None
lap_count = 0
total_time_duration = timedelta(0)
lap_duration_dict = {}

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
    command = input("Command (start/lap/pause/resume/stop/restart/quit): ")

    if command.lower() == 'start':
        datetime_start = datetime.now()
        print(f'Started at {datetime_start.strftime('%H:%M:%S')}')

    elif command.lower() == 'lap':
        lap_count += 1
        now = datetime.now()
        time_duration = time_converter(now - datetime_start)
        total_time_duration += time_duration
        lap_duration_dict[f'Lap {lap_count}'] = time_duration
        print(f'Lap {lap_count} - {time_duration} (Total: {total_time_duration})')

    elif command.lower() == 'pause':
        print(f'Pause at {total_time_duration}')

    elif command.lower() == 'resume':
        print('Resumed.')
        datetime_start = datetime.now()

    elif command.lower() == 'stop':
        fastest_key = min(lap_duration_dict, key=lap_duration_dict.get)
        slowest_key = max(lap_duration_dict, key=lap_duration_dict.get)
        average = total_time_duration / lap_count

        content = f"""
        Summery
        -------
        
        Total Time: {total_time_duration}
        Laps: {lap_count}
        Fastest Lap: {lap_duration_dict[fastest_key]} ({fastest_key})
        Slowest Lap: {lap_duration_dict[slowest_key]} ({slowest_key})
        Average Lap: {average}
        """

        print(content)

        data = {
            'date': [datetime_start.strftime('%Y-%m-%d')],
            'start_time': [datetime_start.strftime('%H:%M:%S')],
            'total_duration': [str(total_time_duration)],
            'laps': [lap_count],
            'fastest': [lap_duration_dict[fastest_key]],
            'slowest': [lap_duration_dict[slowest_key]],
            'average': [average]
        }

        store(data)

        break

    else:
        print('Please enter valid command...')


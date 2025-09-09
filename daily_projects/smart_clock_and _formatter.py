from datetime import datetime

# Generate verbose suffix
def ordinal(n: int) -> str:
    if 11 <= (n % 100) <=13:
        suffix = 'th'
    else:
        suffix = {1:'st', 2:'nd', 3:'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

# Find the correct date and time format
def format_verbose(dt, mode):
    return dt.strftime("%A, %B %d, %Y - %I:%M %p" if mode == '12' else "%A, %B %d, %Y - %H:%M")

def dashboard(date_time_format):
    now = datetime.now()
    verbose = format_verbose(now, date_time_format)

    print(f'Current Local Time (Verbose): {verbose}')
    print(f'Current Local Time (ISO): {now.strftime('%Y-%m-%d %H:%M:%S')}')
    print(f'ISO week number: {now.isocalendar().week}')
    print(f'Day of year: {now.timetuple().tm_yday}')
    print(f'Date with ordinal: {now.strftime('%B')}, {ordinal(int(now.strftime('%d')))} {now.year}')

time_format = input('Choose time format (12/24): ').strip()
if time_format not in ('12', '24'):
    print('Please enter the correct format!')
else:
    dashboard(time_format)


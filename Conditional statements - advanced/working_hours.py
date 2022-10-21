time_of_day = int(input())
day_of_week = input()

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    if 10 <= time_of_day <= 18:
        print("open")
    else:
        print("closed")
if day_of_week == "Sunday":
    print('closed')

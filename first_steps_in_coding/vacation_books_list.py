number_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_needed = number_pages // pages_per_hour
daily_hours = time_needed // days

print(daily_hours)
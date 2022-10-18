init_hour = int(input())
init_min = int(input())

total_time_min = init_hour * 60 + init_min + 15

hour = total_time_min // 60
min = total_time_min % 60

if hour > 23:
    hour = 0

if min < 10:
    print(f"{hour}:0{min}")
else:
    print(f"{hour}:{min}")

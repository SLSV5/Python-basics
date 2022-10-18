from math import floor
first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time
min = total_time // 60
sec = total_time % 60

min = floor(min)

if sec < 10:
    print(f"{min}:0{sec}")
else:
    print(f"{min}:{sec}")

from math import ceil
tv_series = input()
episode_duration = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4
time_left = break_length - lunch_time - relax_time

diff = abs(episode_duration - time_left)
rounded_diff = ceil(diff)
if episode_duration <= time_left:
    print(f"You have enough time to watch {tv_series} "
          f"and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series}, you need {rounded_diff} more minutes.")

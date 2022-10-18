from math import floor
world_record_sec = float(input())
distance_m = float(input())
time_for_m = float(input())

time_in_sec = distance_m * time_for_m
time_with_drag = floor(distance_m / 15) * 12.5
total_time = time_in_sec + time_with_drag

diff = abs(world_record_sec - total_time)
if total_time >= world_record_sec:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
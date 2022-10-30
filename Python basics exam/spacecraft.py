from math import floor
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_astronaut = float(input())

ship_volume = ship_height * ship_length * ship_width
room_volume = ((average_astronaut + 0.40) * 2) * 2
number_astro_possible = (floor(ship_volume/room_volume))

if 3 <= number_astro_possible <= 10:
    print(f"The spacecraft holds {number_astro_possible} astronauts.")
elif number_astro_possible < 3:
    print(f"The spacecraft is too small.")
elif number_astro_possible > 10:
    print(f"The spacecraft is too big.")
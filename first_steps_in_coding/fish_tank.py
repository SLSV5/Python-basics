length_cm = int(input())
height_cm = int(input())
width_cm = int(input())
percertage = float(input())

volume = length_cm * width_cm * height_cm
volume_litre = volume / 1000
used_space = percertage / 100
litres_needed = volume_litre * (1 - used_space)

print (litres_needed)


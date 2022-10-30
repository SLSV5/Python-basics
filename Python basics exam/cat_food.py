number_cats = int(input())
total_grams = 0
group1 = 0
group2 = 0
group3 = 0

for _ in range(number_cats):
    grams_food = int(input())
    total_grams += grams_food
    if 100 <= grams_food < 200:
        group1 += 1
    elif 200 <= grams_food < 300:
        group2 += 1
    elif 300 <= grams_food < 400:
        group3 += 1

in_kg = total_grams / 1000
full_price = in_kg * 12.45

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {full_price:.2f} lv.")

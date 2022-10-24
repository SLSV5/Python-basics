flowers = input()
flower_count = int(input())
budget = float(input())
price = 0

if flowers == "Roses":
    price = flower_count * 5.00
    if flower_count > 80:
        price = price * 0.90

elif flowers == "Dahlias":
    price = flower_count * 3.80
    if flower_count > 90:
        price = price * 0.85

elif flowers == "Tulips":
    price = flower_count * 2.80
    if flower_count > 80:
        price = price * 0.85

elif flowers == "Narcissus":
    price = flower_count * 3.00
    if flower_count < 120:
        price = price * 1.15

elif flowers == "Gladiolus":
    price = flower_count * 2.50
    if flower_count < 80:
        price = price * 1.20

diff = abs(price - budget)
if price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
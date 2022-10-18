budget = float(input())
num_statists = int(input())
clothing_price_stat = float(input())

decor = budget * 0.1
clothing_price = num_statists * clothing_price_stat

if num_statists > 150:
    clothing_price = clothing_price * 0.9
film_price = decor + clothing_price

diff = abs(budget - film_price)
if budget >= film_price:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
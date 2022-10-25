group_budget = int(input())
season = input()
num_fisherman = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season in ["Summer", "Autumn"]:
    price = 4200
elif season == "Winter":
    price = 2600

if num_fisherman <= 6:
    price = price * 0.9
elif 7 <= num_fisherman <= 11:
    price = price * 0.85
elif num_fisherman > 11:
    price = price * 0.75

if num_fisherman % 2 == 0 and season != "Autumn":
    price = price * 0.95

diff = abs(price - group_budget)
if price <= group_budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
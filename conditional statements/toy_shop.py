trip_price = float(input())
puzzle = int(input())
doll = int(input())
teddy = int(input())
minion = int(input())
truck = int(input())
puzzle_price = puzzle * 2.60
doll_price = doll * 3
teddy_price = teddy * 4.10
minion_price = minion * 8.20
truck_price = truck * 2

total_toys = puzzle + doll + teddy + minion + truck
total_price = puzzle_price + doll_price + teddy_price + minion_price + truck_price

if total_toys >= 50:
    total_price = total_price * 0.75

rent = total_price * 0.1
income = total_price - rent

diff = abs(trip_price - income)
if trip_price <= income:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")


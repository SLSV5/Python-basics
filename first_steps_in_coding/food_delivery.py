chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.40
price_vegan = vegan_menu * 8.15
total_menu_prices = price_vegan + price_fish + price_chicken
dessert = total_menu_prices * (20 /100)
full_order_price = total_menu_prices + dessert + 2.50

print(full_order_price)
number_pens = int(input())
markers = int(input())
litre_detergend = int(input())
discount = int(input())

price_pens = number_pens * 5.80
price_markers = markers * 7.20
price_detergent = litre_detergend * 1.20
full_price = price_pens + price_detergent + price_markers
discount_2 = full_price * (discount / 100)
total = full_price - discount_2

print(total)



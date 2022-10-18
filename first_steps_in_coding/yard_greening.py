yard_square_meters = float(input())
price_for_landscaping = yard_square_meters * 7.61
discount = price_for_landscaping * 0.18
price_with_discount = price_for_landscaping - discount

print(f'The final price is: {price_with_discount} lv.')
print(f"The discount is: {discount} lv.")
square_m_nylon = int(input())
litre_paint = int(input())
litre_thinner = int(input())
work_time = int(input())

price_nylon = (square_m_nylon + 2) * 1.50
price_paint = (litre_paint + (litre_paint * 10/100)) * 14.50
price_thinner = litre_thinner * 5.00
materials_price = price_paint + price_nylon + price_thinner + 0.40
workers_price = (materials_price*(30/100)) * 8
full_price = workers_price + materials_price


print(full_price)

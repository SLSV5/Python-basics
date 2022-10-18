training_price = int(input())
price_shoes = training_price - (training_price * 0.40)
price_jersey = price_shoes - (price_shoes * 0.20)
price_ball = price_jersey / 4
price_acessoaries = price_ball / 5
full_price = training_price + price_shoes + price_jersey + price_ball +\
             price_acessoaries
print(full_price)

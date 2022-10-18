deposit = float(input())
months = int(input())
rate_of_interest = float(input())

annual_rate = deposit * (rate_of_interest / 100)
monthly_rate = annual_rate / 12
total_sum = deposit + months * monthly_rate

print (total_sum)
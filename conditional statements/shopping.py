budget = float(input())
videocard = int(input())
processor = int(input())
memory = int(input())

video_price = videocard * 250
processor_price = video_price * 0.35
memory_price = video_price * 0.10
total_price = video_price + (processor * processor_price) + (memory * memory_price)

if videocard > processor:
    total_price = total_price - (total_price * 0.15)


diff = abs(budget - total_price)
if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

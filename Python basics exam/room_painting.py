from math import ceil
from math import floor
paint = int(input())
wallpaper_rolls = int(input())
gloves_price_1 = float(input())
paint_brush_price_1 = float(input())

paint_price = paint * 21.50
wallpaper_rolls_price = wallpaper_rolls * 5.20

glove_count = (ceil(wallpaper_rolls * 0.35))
brush_count = (floor(paint * 0.48))

glove_price = glove_count * gloves_price_1
brush_price = brush_count * paint_brush_price_1

full_price = glove_price + brush_price + paint_price + wallpaper_rolls_price

delivery = full_price / 15

print(f"This delivery will cost {delivery:.2f} lv.")
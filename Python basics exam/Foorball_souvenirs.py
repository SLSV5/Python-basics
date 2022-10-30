city = input()
souvenirs = input()
souvenirs_sold = int(input())
price = 0
country = True
souv = True


if city == "Argentina":
        if souvenirs == "flags":
            price = souvenirs_sold * 3.25
        elif souvenirs == "caps":
            price = souvenirs_sold * 7.20
        elif souvenirs == "posters":
            price = souvenirs_sold * 5.10
        elif souvenirs == "stickers":
            price = souvenirs_sold * 1.25
        else:
            souv = False
elif city == "Brazil":
        if souvenirs == "flags":
            price = souvenirs_sold * 4.20
        elif souvenirs == "caps":
            price = souvenirs_sold * 8.50
        elif souvenirs == "posters":
            price = souvenirs_sold * 5.35
        elif souvenirs == "stickers":
            price = souvenirs_sold * 1.20
        else:
            souv = False
elif city == "Croatia":
        if souvenirs == "flags":
            price = souvenirs_sold * 2.75
        elif souvenirs == "caps":
            price = souvenirs_sold * 6.90
        elif souvenirs == "posters":
            price = souvenirs_sold * 4.95
        elif souvenirs == "stickers":
            price = souvenirs_sold * 1.10
        else:
            souv = False
elif city == "Denmark":
        if souvenirs == "flags":
            price = souvenirs_sold * 3.10
        elif souvenirs == "caps":
            price = souvenirs_sold * 6.50
        elif souvenirs == "posters":
            price = souvenirs_sold * 4.80
        elif souvenirs == "stickers":
            price = souvenirs_sold * 0.90
        else:
            souv = False
else:
    country = False

if country and souv:
    print(f"Pepi bought {souvenirs_sold} {souvenirs} of {city} for {price:.2f} lv.")

if not country:
    print("Invalid country!")

if not souv:
    print("Invalid stock!")
from math import pi
figure = str(input())
area = 0

if figure == "square":
    a = float(input())
    area = a * a
if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
if figure == "circle":
    r = float(input())
    area = pi * (r ** 2)
if figure == "triangle":
    a = float(input())
    b = float(input())
    area = 1/2 * a * b

print(f'{area:.3f}')
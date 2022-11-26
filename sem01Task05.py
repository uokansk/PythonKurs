"""
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
"""
ax = float(input('Enter X point A: '))
ay = float(input('Enter Y point A: '))
bx = float(input('Enter X point B: '))
by = float(input('Enter Y point B: '))
print(round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 2))

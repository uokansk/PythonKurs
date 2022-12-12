"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""
from random import choice
from random import randint

playersList = ['комп', input('введи имя игрока: ')]
player1 = choice(playersList)
playersList.insert(0, player1)

if playersList[0] == playersList[1]:
    del playersList[1]
else:
    del playersList[2]

print(f'Согласно справедливого жребия, первым ходит {playersList[0]}')

player = playersList[0]
candy2 = candy1 = 0
candy = 100
while candy > 0:
    print(f'в игре {candy} конфет')
    if player == 'комп':
        if candy < 29:
            num = candy
        else:
            num = 29
        candyPl = randint(1, num)
    else:
        candyPl = int(input(f'{player} забери конфету '))
    if candyPl in range(1, 29) and candyPl <= candy:
        candy -= candyPl
        if candy == 0:
            break
        elif player == playersList[0]:
            candy1 += candyPl
            print(f'у {playersList[0]} уже {candy1} конфет')
            player = playersList[1]
        else:
            player = playersList[0]
            candy2 += candyPl
            print(f'у {playersList[1]} уже {candy2} конфет')
    else:
        print(f'{player} - ты не прав, проверь сколько берешь')
print(f'победитель {player} ')

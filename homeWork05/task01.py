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

playersList = []
i = 1
while len(playersList) < 2:
    playersList.append(input(f'введи имя {i} игрока: '))
    i += 1

player1 = choice(playersList)
if player1 == playersList[0]:
    player2 = playersList[1]
else:
    player2 = playersList[0]

print(f'первым ходит {player1}')
print(f'вторым ходит {player2}')
player = player1
candy2 = candy1 = 0
candy = 100
while candy > 0:
    print(f'в игре {candy} конфет')
    candyPl = int(input(f'{player} забери конфету '))
    if candyPl in range(1, 29) and candyPl <= candy:
        candy -= candyPl
        if candy == 0:
            break
        elif player == player1:
            candy1 += candyPl
            print(f'у {player1} уже {candy1} конфет')
            player = player2
        else:
            player = player1
            candy2 += candyPl
            print(f'у {player2} уже {candy2} конфет')
    else:
        print(f'{player} - ты не прав, проверь сколько берешь')
print(f'победитель {player} ')

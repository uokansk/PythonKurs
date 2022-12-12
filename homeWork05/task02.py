"""
Создайте программу для игры в ""Крестики-нолики""
"""
a = [[' ', 1, 2, 3], [1, '*', '*', '*'], [2, '*', '*', '*'], [3, '*', '*', '*']]

playerList = ['player1', 'player2']
player = 'X_gamer'
count = 0
while count < 9:
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
            # if a[1][1] != '*' and a[1][1] == a[1][2] == a[1][3] or a[2][1] == a[2][2] == a[2][1
            # ] or a[3][1] == a[3][2] == a[3][1] or a[1][1] == a[2][1] == a[3][1
            # ] or a[1][2] == a[2][2] == a[3][2] or a[1][3] == a[2][3] == a[3][3
            # ] or a[1][1] == a[2][2] == a[3][3] or a[1][3] == a[2][2] == a[3][1]:
            #     break
            # print(f'победил {player}')
        print()
    row, col = int(input(f'{player} введи ряд: ')), int(input(f'{player} введи столбец: '))
    if a[row][col] != '*' or row == 0 or col == 0:
        print(f'{player} - проверь что вводишь')
    else:
        if player == 'X_gamer':
            a[row][col] = 'X'
            player = 'O_gamer'
        else:
            a[row][col] = 'O'
            player = 'X_gamer'
        count += 1
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    #         if a[1][1] != '*' and a[1][1] == a[1][2] == a[1][3] or a[2][1] == a[2][2] == a[2][1
    #         ] or a[3][1] == a[3][2] == a[3][1] or a[1][1] == a[2][1] == a[3][1
    #         ] or a[1][2] == a[2][2] == a[3][2] or a[1][3] == a[2][3] == a[3][3
    #         ] or a[1][1] == a[2][2] == a[3][3] or a[1][3] == a[2][2] == a[3][1]:
    #             break
    #         print(f'победил {player}')
print('игра окончена')

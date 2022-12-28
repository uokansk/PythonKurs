from tkinter import *

game = 0
game_left = list(range(9))
wins_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def check_win():
    global game
    global winner
    for i in wins_coord:
        if game_left[i[0]] == game_left[i[1]] == game_left[i[2]]:
            winner = game_left[i[0]]
            return True


def stop_game():
    game_board = list(range(9))
    for i in game_board:
        buttons[i].config(bg='white', state='disabled')


def push(b):
    global game
    global game_left
    global x_or_o

    if game % 2 == 0:
        game_left[b] = 'X'
        buttons[b].config(text='X', bg='white', state='disabled')
    else:
        game_left[b] = 'O'
        buttons[b].config(text='O', bg='white', state='disabled')
    game += 1
    if check_win():
        lbl['text'] = f'Победа {winner}!'
        stop_game()
    elif game == 9:
        lbl['text'] = 'Ничья'
        stop_game()


window = Tk()
lbl = Label(width=30, text="X крестики нолики O", font=("Arial Bold", 12))
lbl.grid(column=0, row=0, columnspan=3, stick='wens')

buttons = [Button(width=5, height=2, bg='green', font=("Arial Bold", 20), command=lambda x=i: push(x)) for i in
           range(9)]

row = 1
col = 0
for i in range(9):
    buttons[i].grid(column=col, row=row, stick='wens')
    col += 1
    if col == 3:
        row += 1
        col = 0

window.mainloop()

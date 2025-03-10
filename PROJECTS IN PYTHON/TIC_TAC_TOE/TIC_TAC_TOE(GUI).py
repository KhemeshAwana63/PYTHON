import tkinter as tk
from tkinter import messagebox

#creating the main window
root = tk.Tk()
root.title("tic-tac-toe")

#create boards and a empty list for our buttons
board = [" "]*9
buttons = []
current_player = 'X'

def determining_winner():
    win_case = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (2,4,6),(1,4,7)]
    for a , b, c in win_case:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def on_clicks(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text = current_player)

    winner = determining_winner()
    if winner:
        messagebox.showinfo("Game Over",f'player {current_player} won')
        root.quit()
    elif " " not in board:
        messagebox.showinfo("Game over","Match Drawn")
        root.quit()

    current_player = 'O' if current_player == 'X' else 'X'

#creating functional 3 cross 3 grid
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Arial",24), width=5 , height= 2, command= lambda i = i:on_clicks(i))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)

#to run the main window
root.mainloop()


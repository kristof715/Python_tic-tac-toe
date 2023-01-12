from customtkinter import CTk, CTkLabel, CTkFrame, CTkButton


global played, board, game_over
player = "O"
board = [[' ' for _ in range(3)] for _ in range(3)]
game_over = False

def create_widgets():
    for row in range(3):

        for col in range(3):
            button = CTkButton(master=frame,
                               width=100,
                               height=100,
                               text=" ",
                               font=("Arial", 50),
                               command=lambda r = row, c = col: TicTacToe(r, c))
            button.grid(row=row,
                        column=col,
                        padx=8,
                        pady=8)      
 

def new_game():
    global player, board, game_over
    player = "O"
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False
    label_3.configure(text="")

    widget_update()

    for widget in root.grid_slaves():
        widget.destroy()

    create_widgets()
    game_over = False

def check_game_over():
    global game_over
    for row in range(3):
        if board[row][0] != " " and board[row][0] == board[row][1] == board[row][2]:
            label_3.configure(text=f"{player} won!")
            game_over = True
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            label_3.configure(text=f"{player} won!")
            game_over = True
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        label_3.configure(text=f"{player} won!")
        game_over = True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        label_3.configure(text=f"{player} won!")
        game_over = True
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        label_3.configure(text="It's a tie")
        game_over = True    
        
def widget_update():
    for row in range(3):
                for col in range(3):
                    button = frame.grid_slaves(row=row, column=col)[0]
                    button.configure(text=board[row][col])  # type: ignore

def switch_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    label_2.configure(text=f"It's {player}'s turn")

def TicTacToe(row, col):

    if not game_over and board[row][col] == " ":
        board[row][col] = player
        check_game_over()
        widget_update()
        if not game_over:
            switch_player()
    if game_over:
        restart_button.pack(pady=12, padx=12)

root = CTk()
root.resizable(width=False, height=False)
root.title("Tik-Tac-Toe")


label_1 = CTkLabel(master=root,
                   text="Welcome to Tic-Tac-Toe!",
                   font=("Ariel", 30))

label_2 = CTkLabel(master=root,
                   text=f"It's {player}'s turn",
                   font=("Ariel", 20))

label_1.pack(pady=14, padx=20)
label_2.pack(pady=14, padx=20)

frame = CTkFrame(master=root,
                 width=350,
                 height=350,
                 corner_radius=10)
frame.pack(padx=20, pady=20)

for row in range(3):

    for col in range(3):
        button = CTkButton(master=frame,
                           width=100,
                           height=100,
                           text=" ",
                           font=("Arial", 50),
                           command=lambda r = row, c = col: TicTacToe(r, c),
                           
                           )
        button.grid(row=row,
                    column=col,
                    padx=8,
                    pady=8)     

label_3 = CTkLabel(master=root,
                    text="",
                    font=("Ariel", 34))

label_3.pack(pady=20, padx=20)

global restart_button
restart_button = CTkButton(master=root, text="new game", command=new_game)

if __name__ == '__main__':
    root.mainloop()
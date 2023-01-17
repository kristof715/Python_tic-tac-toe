import tkinter as tk


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(width=False, height=False)

        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.player = 'X'
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self,
                                   width=10,
                                   height=4,
                                   font=("Arial", 16),
                                   command=lambda r=row, c=col: self.play(r, c))
                button.grid(row=row,
                            column=col,
                            padx=5,
                            pady=5)

    def update_widgets(self):
        for row in range(3):
            for col in range(3):
                button = self.grid_slaves(row=row, column=col)[0]
                button.configure(text=self.board[row][col])  # type: ignore

    def check_game_over(self):
        for row in range(3):
            if self.board[row][0] != ' ' and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                self.game_over = True
                self.show_game_over_message(f"{self.player} wins!")
                return
        for col in range(3):
            if self.board[0][col] != ' ' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                self.game_over = True
                self.show_game_over_message(f"{self.player} wins!")
                return
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.game_over = True
            self.show_game_over_message(f"{self.player} wins!")
            return
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            self.game_over = True
            self.show_game_over_message(f"{self.player} wins!")
            return
        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            self.game_over = True
            self.show_game_over_message("It's a tie!")
            return

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def show_game_over_message(self, message):
        label = tk.Label(self,
                         text=message,
                         font=("Arial", 16))
        label.grid(row=3,
                   column=0,
                   columnspan=3)

        new_game_button = tk.Button(self,
                                    text="New Game",
                                    font=("Arial", 14),
                                    command=self.new_game)
        new_game_button.grid(row=4,
                             column=0,
                             columnspan=3)

    def new_game(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.player = 'X'
        self.game_over = False
        self.update_widgets()

        for widget in self.grid_slaves():
            widget.destroy()

        self.create_widgets()

    def play(self, row, col):
        if not self.game_over and self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.update_widgets()
            self.check_game_over()
            if not self.game_over:
                self.switch_player()


if __name__ == '__main__':
    TicTacToe().mainloop()
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in range(3):
            print(' | '.join(self.board[row]))
            if row < 2:
                print('--+---+--')

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if self.board[0][0] == self.current_player and self.board[1][1] == self.current_player and self.board[2][2] == self.current_player:
            return True
        if self.board[0][2] == self.current_player and self.board[1][1] == self.current_player and self.board[2][0] == self.current_player:
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.display_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
            except ValueError:
                print("Invalid input. Enter two numbers separated by space.")
                continue
            if self.make_move(row - 1, col - 1):
                if self.check_win():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.check_draw():
                    self.display_board()
                    print("It's a draw!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

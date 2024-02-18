import random
import time

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class HumanPlayer(Player):
    def get_move(self, game):
        while True:
            try:
                move = int(input(f"{self.symbol}'s turn. Input move (0-8): "))
                if move in game.available_moves():
                    return move
                else:
                    print('Invalid square. Try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')

class RandomComputerPlayer(Player):
    def get_move(self, game):
        return random.choice(game.available_moves())

class SmartComputerPlayer(Player):
    def get_move(self, game):
        return self.minimax(game, self.symbol)['position']

    def minimax(self, state, player):
        if state.current_winner:
            return {'position': None, 'score': 1 if state.current_winner == self.symbol else -1}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        best = {'position': None, 'score': float('-inf') if player == self.symbol else float('inf')}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, 'O' if player == 'X' else 'X')
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if (player == self.symbol and sim_score['score'] > best['score']) or (player != self.symbol and sim_score['score'] < best['score']):
                best = sim_score
        return best

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def make_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def winner(self, square, symbol):
        row_ind, col_ind = divmod(square, 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        col = [self.board[col_ind+i*3] for i in range(3)]

        if all(s == symbol for s in row) or all(s == symbol for s in col):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(s == symbol for s in diagonal1) or all(s == symbol for s in diagonal2):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def play(print_game=True):
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()

    if print_game:
        print_board_nums()

    current_symbol = 'X'
    while t.empty_squares():
        if current_symbol == 'O':
            move = o_player.get_move(t)
        else:
            move = x_player.get_move(t)

        if t.make_move(move, current_symbol):
            if print_game:
                print(f"{current_symbol} makes a move to square {move}")
                print_board(t)
                print('')

            if t.current_winner:
                if print_game:
                    print(f"{current_symbol} wins!")
                return current_symbol
            current_symbol = 'O' if current_symbol == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

def print_board(t):  
    for i in range(0, 9, 3):
        print('| ' + ' | '.join(t.board[i:i+3]) + ' |')

def print_board_nums():
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')

if __name__ == '__main__':
    play(print_game=True)

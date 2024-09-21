import random as r
class Node:
    def __init__(self, board, current_level, alpha, beta):
        self.board = board
        self.current_level = current_level
        self.alpha = alpha
        self.beta = beta

def make_draw(pz, pos, value):
    row = pos // 3
    col = pos % 3
    if pz[row][col] == -1:
        pz[row][col] = value
        return pz
    else:
        return None  # Return None when the cell is already filled

def check_solution(pz, value):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if all(cell == value for cell in pz[row]):
            return True
    for col in range(3):
        if all(pz[i][col] == value for i in range(3)):
            return True
    if all(pz[i][i] == value for i in range(3)) or all(pz[i][2 - i] == value for i in range(3)):
        return True
    return False

def is_full(pz):
    return all(cell != -1 for row in pz for cell in row)

def evaluate(board, player):
    # Evaluation function for the current player ('X' or 'O')
    for i in range(3):
        if any(cell != player for cell in board[i]):
            return 0  # No win in rows
        if any(board[j][i] != player for j in range(3)):
            return 0  # No win in columns
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return 1  # Win in diagonals
    return 0  # No win

def minimax_alpha_beta(board, player, alpha, beta, maximizing):
    if check_solution(board, 'X'):
        return 1  # Maximizer wins
    elif check_solution(board, 'O'):
        return -1  # Minimizer wins
    elif is_full(board):
        return 0  # It's a draw


    if maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 'X'
                    eval = minimax_alpha_beta(board, 'O', alpha, beta, False)
                    board[i][j] = -1
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 'O'
                    eval = minimax_alpha_beta(board, 'X', alpha, beta, True)
                    board[i][j] = -1
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def choose_best_move(board):
    best_eval = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                board[i][j] = 'X'
                move_eval = minimax_alpha_beta(board, 'O', -float('inf'), float('inf'), False)
                board[i][j] = -1
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    print(best_move)
    return best_move


def game():
    board = [[-1 for i in range(3)] for j in range(3)]
    player1 = 'Computer'
    player2 = input('Enter a Name of Second Player: ')
    toss = r.randint(0, 1)
    players = [player1, player2] if toss == 0 else [player2, player1]
    
    print(f'{players[0]} won the toss, and will drqw  first ')
    attempts = 0

    while True:

        for plr in range(len(players)):
            attempts += 1
            if players[plr] == 'Computer':
                pos = choose_best_move(board)
                if pos is not None:
                    board[pos[0]][pos[1]] = 'X'
            
            else:
                print('\nCurrent Board:')
                for row in board:
                    print(' '.join([str(cell) if cell != -1 else ' ' for cell in row]))
                while True:
                    try:
                        pos = int(input(f"{players[plr]}, enter your move (0-8): "))
                        if 0 <= pos < 9 and board[pos // 3][pos % 3] == -1:
                            board = make_draw(board, pos, 'O')
                            break
                        else:
                            print("Invalid move. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 8.")
            if check_solution(board, 'X'):
                print(f'{players[plr]} wins!')
                return

            if attempts >= 9:
                print('Match Draw')
                return

if __name__ == "__main__":
    game()

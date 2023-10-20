def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---|---|---")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f'Player {current_player}, enter row (0, 1, or 2): '))
        col = int(input(f'Player {current_player}, enter column (0, 1, or 2): '))

        if board[row][col] != ' ':
            print("Invalid move! Cell is already occupied.")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f'Player {current_player} wins!')
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()

# Simple Tic Tac Toe Game (2 Players)

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("--+---+--")
    print()

def check_win(player):
    win_states = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_states)

def play():
    player = "X"
    for turn in range(9):
        print_board()
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if board[pos] != ' ':
            print("Invalid move! Try again.")
            continue

        board[pos] = player

        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board()
    print("It's a draw!")

play()

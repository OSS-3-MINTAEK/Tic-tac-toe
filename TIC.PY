# 챗gpt를 사용한 간단한 구현
def print_board(board):
    for row in board:
        print("|".join(row))

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("That spot is taken!")
            continue
        board[row][col] = player
        if check_win(board, player):
            print_board(board)
            print(player, "wins!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("Tie!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()

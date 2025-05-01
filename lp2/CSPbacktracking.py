def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    
    for i in range(row):
        if board[i][col] == 'Q':
            return False

 
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

   
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print("Solution:")
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, n)
            board[row][col] = '.'  

n = 4 
board = [['.' for _ in range(n)] for _ in range(n)]

print(f"Solutions for {n}-Queens Problem:")
solve_n_queens(board, 0, n)

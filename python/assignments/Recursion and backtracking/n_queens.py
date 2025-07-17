def solve_n_queens(n):
    board = [['.'] * n for _ in range(n)]
    res = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q': return False
            if col-(row-i) >= 0 and board[i][col-(row-i)] == 'Q': return False
            if col+(row-i) < n and board[i][col+(row-i)] == 'Q': return False
        return True

    def backtrack(row=0):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack()
    return res

# Example
solutions = solve_n_queens(4)
for s in solutions:
    print(s, end="\n---\n")

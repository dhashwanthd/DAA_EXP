"""Experiment 7: N-Queens using Backtracking"""


def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col:
            return False
        if abs(prev_row - row) == abs(placed - col):
            return False
    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]


def board_str(solution, n):
    lines = []
    border = '+' + '---+' * n
    lines.append(border)
    for row in range(n):
        line = '|'
        for col in range(n):
            line += ' Q |' if solution[row] == col else ' . |'
        lines.append(line)
        lines.append(border)
    return '\n'.join(lines)


def solve(n_str, max_display_str='10'):
    n = int(n_str)
    max_display = int(max_display_str) if max_display_str else 10
    if n < 1 or n > 12:
        raise ValueError('Please choose N between 1 and 12 (larger boards take too long).')
    solutions, backtracks = solve_n_queens(n)
    displayed = solutions[:max_display]
    boards = [board_str(sol, n) for sol in displayed]
    return {
        'n': n,
        'num_solutions': len(solutions),
        'backtracks': backtracks,
        'displayed_count': len(displayed),
        'boards': list(zip(range(1, len(displayed) + 1), displayed)),
    }

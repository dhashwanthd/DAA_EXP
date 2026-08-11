"""Experiment 6: Matrix Chain Multiplication using Dynamic Programming"""


def matrix_chain_order(dims):
    n = len(dims) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f'A{i}'
    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)
    return f'({left} x {right})'


def solve(dims_str):
    dims = [int(x.strip()) for x in dims_str.split(',') if x.strip() != '']
    n = len(dims) - 1
    m, s = matrix_chain_order(dims)
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append('---' if j < i else m[i][j])
        table.append(row)
    return {
        'dims': dims,
        'n': n,
        'min_cost': m[1][n],
        'parenthesization': print_optimal_parens(s, 1, n),
        'table': table,
        'labels': [f'A{i}' for i in range(1, n + 1)],
    }

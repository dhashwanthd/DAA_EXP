"""Experiment 8: Travelling Salesman Problem using Branch and Bound"""
import heapq

INF = float('inf')


def reduce_matrix(mat):
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0
    for i in range(n):
        row_min = min(m[i])
        if row_min and row_min != INF:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min and col_min != INF:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min
    return m, cost


class Node:
    __slots__ = ('bound', 'cost', 'path', 'visited', 'matrix')

    def __init__(self, bound, cost, path, visited, matrix):
        self.bound = bound
        self.cost = cost
        self.path = path
        self.visited = visited
        self.matrix = matrix

    def __lt__(self, other):
        return self.bound < other.bound


def tsp_branch_and_bound(cost, n):
    reduced, initial_bound = reduce_matrix(cost)
    root = Node(initial_bound, 0, [0], {0}, reduced)
    pq = [root]
    best_cost = INF
    best_path = None
    nodes_explored = 0

    while pq:
        node = heapq.heappop(pq)
        nodes_explored += 1
        if node.bound >= best_cost:
            continue
        if len(node.path) == n:
            tour_cost = node.cost + cost[node.path[-1]][0]
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_path = node.path + [0]
            continue
        last = node.path[-1]
        for c in range(n):
            if c in node.visited:
                continue
            new_matrix = [row[:] for row in node.matrix]
            for k in range(n):
                new_matrix[last][k] = INF
                new_matrix[k][c] = INF
            new_matrix[c][0] = INF
            reduced_child, reduction_cost = reduce_matrix(new_matrix)
            new_cost = node.cost + cost[last][c]
            new_bound = new_cost + reduction_cost
            if new_bound < best_cost:
                heapq.heappush(pq, Node(new_bound, new_cost, node.path + [c],
                                         node.visited | {c}, reduced_child))
    return best_path, best_cost, nodes_explored


def solve(matrix_str, city_names_str=''):
    rows = [r.strip() for r in matrix_str.strip().splitlines() if r.strip()]
    n = len(rows)
    if n > 10:
        raise ValueError('Please use at most 10 cities (branch and bound is exponential in the worst case).')
    cost = []
    for r in rows:
        vals = []
        for x in r.split(','):
            x = x.strip()
            vals.append(INF if x.upper() in ('INF', 'X', '-') else int(x))
        cost.append(vals)
    if any(len(r) != n for r in cost):
        raise ValueError('Cost matrix must be square (same number of rows and columns).')

    cities = [c.strip() for c in city_names_str.split(',') if c.strip()]
    if len(cities) != n:
        cities = [chr(65 + i) if i < 26 else str(i) for i in range(n)]

    best_path, best_cost, nodes_explored = tsp_branch_and_bound(cost, n)
    tour = ' -> '.join(cities[i] for i in best_path) if best_path else 'No tour found'
    cost_matrix_display = [['INF' if v == INF else v for v in row] for row in cost]
    return {
        'n': n,
        'cities': cities,
        'cost_matrix': cost_matrix_display,
        'best_path': best_path,
        'tour': tour,
        'best_cost': best_cost,
        'nodes_explored': nodes_explored,
    }

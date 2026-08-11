"""Experiment 3: Kruskal's and Prim's Minimum Spanning Tree"""
import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(n, edges):
    edges = sorted(edges)
    uf = UnionFind(n)
    mst, cost = [], 0
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == n - 1:
                break
    return mst, cost


def prim(n, adj, start=0):
    INF = float('inf')
    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n
    key[start] = 0
    pq = [(0, start)]
    mst, cost = [], 0
    while pq:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w
        for v, wt in adj.get(u, []):
            if not in_mst[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))
    return mst, cost


def solve(n_str, edges_str):
    n = int(n_str)
    edges = []
    for line in edges_str.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        u, v, w = [x.strip() for x in line.split(',')]
        edges.append((int(w), int(u), int(v)))

    adj = {}
    for w, u, v in edges:
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))

    k_mst, k_cost = kruskal(n, edges[:])
    p_mst, p_cost = prim(n, adj)
    return {
        'n': n,
        'edges': edges,
        'kruskal': {'mst': k_mst, 'cost': k_cost},
        'prim': {'mst': p_mst, 'cost': p_cost},
    }

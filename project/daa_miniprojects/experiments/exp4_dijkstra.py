"""Experiment 4: Dijkstra's Single Source Shortest Path"""
import heapq


def dijkstra(graph, source, n):
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)]
    visited = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev


def reconstruct_path(prev, source, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if path and path[0] == source:
        return path
    return []


def solve(n_str, edges_str, source_str):
    n = int(n_str)
    source = int(source_str)
    graph = {i: [] for i in range(n)}
    for line in edges_str.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        u, v, w = [x.strip() for x in line.split(',')]
        u, v, w = int(u), int(v), int(w)
        graph[u].append((v, w))

    dist, prev = dijkstra(graph, source, n)
    rows = []
    for v in range(n):
        path = reconstruct_path(prev, source, v)
        rows.append({
            'vertex': v,
            'distance': dist[v] if dist[v] != float('inf') else 'INF',
            'path': ' -> '.join(map(str, path)) if path else 'No path',
        })
    return {'n': n, 'source': source, 'rows': rows}

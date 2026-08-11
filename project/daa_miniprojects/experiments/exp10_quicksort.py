"""Experiment 10: Deterministic vs Randomized Quick Sort"""
import random
import time
import sys

sys.setrecursionlimit(20000)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons


def deterministic_quicksort(arr, low, high, counter):
    if low < high:
        pi, c = partition(arr, low, high)
        counter[0] += c
        deterministic_quicksort(arr, low, pi - 1, counter)
        deterministic_quicksort(arr, pi + 1, high, counter)


def randomized_quicksort(arr, low, high, counter):
    if low < high:
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        pi, c = partition(arr, low, high)
        counter[0] += c
        randomized_quicksort(arr, low, pi - 1, counter)
        randomized_quicksort(arr, pi + 1, high, counter)


def run_test(sort_fn, arr):
    a = arr[:]
    counter = [0]
    start = time.perf_counter()
    sort_fn(a, 0, len(a) - 1, counter)
    elapsed = (time.perf_counter() - start) * 1000
    return counter[0], elapsed, a


def build_array(kind, n):
    if kind == 'random':
        return [random.randint(1, 100000) for _ in range(n)]
    if kind == 'sorted':
        return list(range(n))
    if kind == 'reverse':
        return list(range(n, 0, -1))
    if kind == 'nearly_sorted':
        arr = list(range(n))
        for _ in range(max(1, n // 20)):
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    raise ValueError('Unknown input type')


def solve(n_str, kind):
    n = int(n_str)
    if n < 1 or n > 20000:
        raise ValueError('Please choose N between 1 and 20000.')
    arr = build_array(kind, n)
    d_comps, d_time, d_sorted = run_test(deterministic_quicksort, arr)
    r_comps, r_time, r_sorted = run_test(randomized_quicksort, arr)
    preview = arr if n <= 30 else arr[:30]
    return {
        'n': n,
        'kind': kind,
        'preview': preview,
        'truncated': n > 30,
        'deterministic': {'comparisons': d_comps, 'time_ms': round(d_time, 3)},
        'randomized': {'comparisons': r_comps, 'time_ms': round(r_time, 3)},
    }

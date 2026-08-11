"""Experiment 5: Min-Max using Divide and Conquer"""


def min_max_dc(arr, low, high):
    """Returns (min, max, comparisons)"""
    if low == high:
        return arr[low], arr[low], 0
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high], 1
        return arr[high], arr[low], 1
    mid = (low + high) // 2
    lmin, lmax, lc = min_max_dc(arr, low, mid)
    rmin, rmax, rc = min_max_dc(arr, mid + 1, high)
    overall_min = lmin if lmin < rmin else rmin
    overall_max = lmax if lmax > rmax else rmax
    return overall_min, overall_max, lc + rc + 2


def min_max_naive(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        comps += 1
        if x > mx:
            mx = x
    return mn, mx, comps


def solve(array_str):
    arr = [int(x.strip()) for x in array_str.split(',') if x.strip() != '']
    mn, mx, dc_comps = min_max_dc(arr, 0, len(arr) - 1)
    _, _, naive_comps = min_max_naive(arr)
    formula = 3 * len(arr) // 2 - 2
    return {
        'array': arr,
        'min': mn,
        'max': mx,
        'dc_comps': dc_comps,
        'naive_comps': naive_comps,
        'formula': formula,
    }

"""Experiment 1: Interpolation Search vs Binary Search"""


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons
        if arr[high] == arr[low]:
            pos = low
        else:
            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if pos < low or pos > high:
            break
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def solve(array_str, target_str):
    arr = sorted(int(x.strip()) for x in array_str.split(',') if x.strip() != '')
    target = int(target_str)
    is_idx, is_comps = interpolation_search(arr, target)
    bs_idx, bs_comps = binary_search(arr, target)
    return {
        'array': arr,
        'target': target,
        'is_idx': is_idx,
        'is_comps': is_comps,
        'bs_idx': bs_idx,
        'bs_comps': bs_comps,
    }

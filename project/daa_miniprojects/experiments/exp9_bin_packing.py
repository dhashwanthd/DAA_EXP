"""Experiment 9: Bin Packing approximation algorithms"""


def first_fit(items, capacity=1.0):
    bins = []
    bin_contents = []
    for item in items:
        placed = False
        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        for i, space in enumerate(bins):
            if space >= item and space - item < best_space:
                best_space = space - item
                best_idx = i
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def summarize(bins, capacity):
    return [{
        'items': [round(x, 2) for x in b],
        'used': round(sum(b), 2),
        'pct': round(sum(b) / capacity * 100, 1),
    } for b in bins]


def solve(items_str, capacity_str):
    items = [float(x.strip()) for x in items_str.split(',') if x.strip() != '']
    capacity = float(capacity_str)
    lower_bound = -(-sum(items) // capacity)

    ff = first_fit(items, capacity)
    ffd = first_fit_decreasing(items, capacity)
    bfd = best_fit_decreasing(items, capacity)

    return {
        'item_list': items,
        'item_sum': round(sum(items), 2),
        'capacity': capacity,
        'lower_bound': int(lower_bound),
        'ff': {'bins': summarize(ff, capacity), 'count': len(ff)},
        'ffd': {'bins': summarize(ffd, capacity), 'count': len(ffd)},
        'bfd': {'bins': summarize(bfd, capacity), 'count': len(bfd)},
    }

import random

comparison_count = 0  # Global counter


def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: Single element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


def min_max_naive(arr):
    mn = mx = arr[0]
    comps = 0

    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps


# -------- Demonstration on a New Array --------
arr = [45, 12, 78, 34, 99, 23, 67, 5, 81, 56, 14, 90]

comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count

_, _, naive_comps = min_max_naive(arr)

print("Input Array:", arr)
print("Minimum Element:", mn)
print("Maximum Element:", mx)
print("Divide & Conquer Comparisons:", dc_comps)
print("Naive Comparisons:", naive_comps)

# -------- Performance Analysis --------
print("\n{:>8} {:>12} {:>14} {:>18}".format(
    "Size", "DC Comps", "Naive Comps", "Formula (3n/2-2)"
))
print("-" * 60)

for size in [12, 60, 600, 6000]:
    arr = [random.randint(100, 9999) for _ in range(size)]

    comparison_count = 0
    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = (3 * size) // 2 - 2

    print("{:>8} {:>12} {:>14} {:>18}".format(
        size, dc, naive, formula
    ))

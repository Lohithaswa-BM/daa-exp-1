import time
import random


# ---------- Interpolation Search ----------
def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    Time Complexity:
        Average : O(log log n)
        Worst   : O(n)
    Space Complexity: O(1)
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:

        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Avoid division by zero
        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# ---------- Binary Search ----------
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
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


# ---------- Performance Analysis ----------
def performance_analysis():

    sizes = [2000, 8000, 15000, 30000, 60000]

    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
          f"{'IS Comp':>12} {'BS Comp':>12}")

    print("-" * 68)

    for size in sizes:

        arr = sorted(random.sample(range(size * 20), size))
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search
        start = time.perf_counter()

        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)

        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search
        start = time.perf_counter()

        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} "
              f"{comp_is:>12} {comp_bs:>12}")


# ---------- Main Program ----------

arr = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
target = 81

index, comparisons = interpolation_search(arr, target)

print("Array :", arr)
print("Target :", target)
print("Element found at index :", index)
print("Comparisons :", comparisons)

print()
performance_analysis()

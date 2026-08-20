import random
import time
import sys

sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Deterministic Quick Sort
def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# Randomized Quick Sort
def randomized_quicksort(arr, low, high):
    if low < high:

        # Select a random pivot
        rand_idx = random.randint(low, high)

        # Move random pivot to the end
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def run_test(sort_fn, arr):
    global comparisons

    # Copy original array
    a = arr[:]

    comparisons = 0

    start = time.perf_counter()

    sort_fn(a, 0, len(a) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


# Number of elements
N = 5000


# Test cases
test_cases = {
    "Random": [random.randint(1, 100000) for _ in range(N)],

    "Sorted": list(range(N)),

    "Reverse": list(range(N, 0, -1)),

    "Nearly Sorted": list(range(N))
}


# Make Nearly Sorted array slightly shuffled
ns = test_cases["Nearly Sorted"]

for _ in range(N // 20):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)

    ns[i], ns[j] = ns[j], ns[i]


# Print table heading
print(
    f"{'Input Type':<16}"
    f"{'DQS Comps':>12}"
    f"{'DQS Time(ms)':>14}"
    f"{'RQS Comps':>12}"
    f"{'RQS Time(ms)':>14}"
)

print("-" * 68)


# Run all test cases
for case, arr in test_cases.items():

    d_comps, d_time = run_test(
        deterministic_quicksort, arr
    )

    r_comps, r_time = run_test(
        randomized_quicksort, arr
    )

    print(
        f"{case:<16}"
        f"{d_comps:>12}"
        f"{d_time:>14.2f}"
        f"{r_comps:>12}"
        f"{r_time:>14.2f}"
    )
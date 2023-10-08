def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

def main():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([1, 2, 3, 2, 1], [1, 1, 2, 2, 3]),
    ]
    for arr, expected in test_cases:
        result = quicksort(arr)
        assert result == expected, f"quicksort({arr}) returned {result}, but expected {expected}"

if __name__ == "__main__":
    main()
def is_sorted(arr):
    """Check if the array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def generate_permutations(arr, start, end):
    """Generate all permutations of the array."""
    if start == end:
        yield arr[:]  # Return a copy of the current permutation
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]  # Swap
            yield from generate_permutations(arr, start + 1, end)  # Recur
            arr[start], arr[i] = arr[i], arr[start]  # Swap back

def bogo_sort(arr):
    """Sort the array using Bogo Sort by generating all permutations."""
    for perm in generate_permutations(arr, 0, len(arr) - 1):
        if is_sorted(perm):
            return list(perm)  # Return as a list
    return arr  # In case no permutation is found (theoretically impossible)

# Example usage

arr = [3, 2, 5, 1, 4]
print("Original array:", arr)
sorted_arr = bogo_sort(arr)
print("Sorted array:", sorted_arr)

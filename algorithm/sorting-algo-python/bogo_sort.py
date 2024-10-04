from itertools import permutations

def is_sorted(arr):
    # Check if the array is sorted.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    # Sort the array using a deterministic Bogo Sort algorithm.
    attempts = 0
    for perm in permutations(arr):
        attempts += 1
        if is_sorted(perm):
            print(f"Array sorted in {attempts} attempts")
            return list(perm)

arr = [3, 2, 5, 1, 4]
print("Original array:", arr)
sorted_arr = bogo_sort(arr)
print("Sorted array:", sorted_arr)

def is_sorted(arr):
    # Check if the array is sorted.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def shuffle(arr):
    
    for i in range(len(arr)):
        swap_idx = (i + 1) % len(arr)
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

def bogo_sort(arr):
    # Sort the array using a non-deterministic Bogo Sort algorithm.
    attempts = 0
    while not is_sorted(arr):
        attempts += 1
        shuffle(arr)
    print(f"Array sorted in {attempts} attempts")
    return arr

arr = [3, 2, 5, 1, 4]
print("Original array:", arr)
sorted_arr = bogo_sort(arr)
print("Sorted array:", sorted_arr)

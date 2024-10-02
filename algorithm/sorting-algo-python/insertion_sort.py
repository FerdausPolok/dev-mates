# Insertion Sort builds the sorted array one element at a time by inserting the current element into the correct position.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Insertion Sorted array:", arr)

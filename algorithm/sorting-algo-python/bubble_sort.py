#  Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Bubble Sorted array:", arr)

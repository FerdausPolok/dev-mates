# Shell Sort is an extension of insertion sort that allows the exchange of elements that are far apart.

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Shell Sorted array:", arr)

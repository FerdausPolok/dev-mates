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
    return arr
# Example
    sample_array = [12, 34, 54, 2, 3]
    print("Original array:", sample_array)
    sorted_array = shell_sort(sample_array)
    print("Sorted array:", sorted_array)
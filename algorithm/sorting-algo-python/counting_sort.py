# Counting Sort is efficient for sorting integers within a specific range by counting the frequency of each element.

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# Example
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Counting Sorted array:", arr)

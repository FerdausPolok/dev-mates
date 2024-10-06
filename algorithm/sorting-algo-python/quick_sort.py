def quickSort(arr):
    # base case for recursive call
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # choosing middle element as pivot
        left_arr = [x for x in arr if x < pivot]  # all elements less than pivot
        middle_arr = [x for x in arr if x == pivot]  # all elements equal to pivot
        right_arr = [x for x in arr if x > pivot]  # all elements greater than pivot

        # Recursively sorting left and right arrs
        return quickSort(left_arr) + middle_arr + quickSort(right_arr)


input_string = input("Please enter the unsorted arr separated by spaces: ")
arr1 = list(map(int, input_string.split()))
print("Unsorted arr:", arr1)
print("Sorted arr:", quickSort(arr1))

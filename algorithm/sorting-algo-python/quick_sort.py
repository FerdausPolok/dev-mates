def quickSort(list):
    #base case for recursive call
    if len(list) <= 1:
        return list
    else:
        pivot = list[len(list) // 2]  # choosing middle element as pivot
        left_list = [x for x in list if x < pivot]   # all elements less than pivot
        middle_list = [x for x in list if x == pivot]  # all elements equal to pivot
        right_list = [x for x in list if x > pivot]  # all elements greater than pivot

        # Recursively sorting left and right lists
        return quickSort(left_list) + middle_list + quickSort(right_list)

# Driver Code
list = [10, 2, 7, 3, 5, 8, 1, 5, 74, 2, 2, 7, 2, 8, 52, 6, 74, 2]
print("Unsorted list:", list)
print(quickSort(list))


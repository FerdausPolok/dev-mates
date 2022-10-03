def mergeSort(list):
    #divide part
    if len(list) > 1: #base case for recursive call
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        #merge part
        i, j, k = 0, 0, 0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i +=1
                k +=1
            else:
                list[k] = right_list[j]
                j += 1
                k +=1

        while i<len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    return list

list= [10,2,7,3,5,8,1,5,74,2,2,7,2,8,52,6,74,2]
print("Unsorted list:", list)
print(mergeSort(list))